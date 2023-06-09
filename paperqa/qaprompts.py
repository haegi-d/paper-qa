import copy
from datetime import datetime
from typing import Any, Dict, List, Optional
import re

import langchain.prompts as prompts
from langchain.callbacks.manager import AsyncCallbackManagerForChainRun
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import LLMResult, SystemMessage

summary_prompt = prompts.PromptTemplate(
    input_variables=["question", "context_str", "citation"],
    template="Summarize the text below to help answer a question. "
    "Do not directly answer the question, instead summarize "
    "to give evidence to help answer the question. Include direct quotes. "
    'Reply "Not applicable" if text is irrelevant. '
    "Use around 100 words. At the end of your response, provide a score from 1-10 on a newline "
    "indicating relevance to question. Do not explain your score. "
    "\n\n"
    "{context_str}\n"
    "Extracted from {citation}\n"
    "Question: {question}\n"
    "Relevant Information Summary:",
)
# level: str = "pyhsics student with some prior knowledge but no expertise in this topic"
qa_prompt = prompts.PromptTemplate(
    input_variables=["question", "context_str", "length"],
    template="Write an answer ({length}) "
    "for the question below based on the provided context. "
    "If the context provides insufficient information, "
    'reply "I cannot answer". '
    "If you can answer use the following structure:"
    "1. Start with 'Confidence Level:' and state your self-assessed confidence level in your answer: high, medium, or low. "
    " (high: consice answer based on many sources, medium: answer has uncertainties and is based on fewer references"
    " , low: significant uncertainties and based on limited references)."
    "2. Give your answer and for each statement in your answer indicate which sources most support it " #changed sentence to statement
    "via valid citation markers at the end of sentences, like (Example2012). Try to use base your answer on multiple sources. "
    "Answer in an unbiased, comprehensive, and scholarly tone. "
    "Bear in mind you answer to a pyhsics student with some prior knowledge but no expertise in this topic."
    "3. Finish of with 'In short:' and conclude your answer in 1-2 sentences."
    "Use Markdown for formatting code or text, and try to use direct quotes to support arguments.\n\n"
    "Context: {context_str}\n"
    "Question: {question}\n"
    "Answer: ",
)

# qa_prompt = prompts.PromptTemplate(
#     input_variables=["question", "context_str", "length"],
#     template="Write an answer ({length}) "
#     "for the question below based on the provided context. "
#     "If the context provides insufficient information, "
#     'reply "I cannot answer". '
#     "For each sentence in your answer, indicate which sources most support it " 
#     "via valid citation markers at the end of sentences, like (Example2012). "
#     "Answer in an unbiased, comprehensive, and scholarly tone. "
#     "Complete your answer with a concluding 1-2 sentences, which may be opinionated. "
#     "Use Markdown for formatting code or text, and try to use direct quotes to support arguments.\n\n"
#     "{context_str}\n"
#     "Question: {question}\n"
#     "Answer: ",
# )

#TODO check with Simon what he thinks about this changes
# They changed it to " For each part of your answer, indicate which sources most support it"
# and "If the question is subjective, provide an opinionated answer in the concluding 1-2 sentences. "


search_prompt = prompts.PromptTemplate(
    input_variables=["question"],
    template="We want to answer the following question: {question} \n"
    "Provide three keyword searches (one search per line) "
    "that will find papers to help answer the question. Do not use boolean operators. "
    "Provide some broad and some specific searches. "
    "Recent years are 2021, 2022, 2023.\n\n"
    "1.",
)


select_paper_prompt = prompts.PromptTemplate(
    input_variables=["question", "papers"],
    template="Select papers to help answer the question below. "
    "Papers are listed as $KEY: $PAPER_INFO. "
    "Return a list of keys, separated by commas. "
    'Return "None", if no papers are applicable. '
    "Choose papers that are relevant, from reputable sources, and timely. \n\n"
    "Question: {question}\n\n"
    "{papers}\n\n"
    "Selected keys:",
)


def _get_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y")


citation_prompt = prompts.PromptTemplate(
    input_variables=["text"],
    template="Provide the citation for the following text in MLA Format. Today's date is {date}\n"
    "{text}\n\n"
    "Citation:",
    partial_variables={"date": _get_datetime},
)


class FallbackLLMChain(LLMChain):
    """Chain that falls back to synchronous generation if the async generation fails."""

    async def agenerate(
        self,
        input_list: List[Dict[str, Any]],
        run_manager: Optional[AsyncCallbackManagerForChainRun] = None,
    ) -> LLMResult:
        """Generate LLM result from inputs."""
        try:
            return await super().agenerate(input_list, run_manager=run_manager)
        except NotImplementedError as e:
            return self.generate(input_list, run_manager=run_manager)


def make_chain(prompt, llm, skip_system=False):
    if type(llm) == ChatOpenAI:
        system_message_prompt = SystemMessage(
            content="Answer in an unbiased, concise, scholarly tone. "
            "You may refuse to answer if there is insufficient information. "
            "If there are ambiguous terms or acronyms, first define them. ",
        )
        human_message_prompt = HumanMessagePromptTemplate(prompt=prompt)
        if skip_system:
            prompt = ChatPromptTemplate.from_messages([human_message_prompt])
        else:
            prompt = ChatPromptTemplate.from_messages(
                [system_message_prompt, human_message_prompt]
            )
    return FallbackLLMChain(prompt=prompt, llm=llm)


def get_score(text):
    score = re.search(r"[sS]core[:is\s]+([0-9]+)", text)
    if score:
        return int(score.group(1))
    if len(text) < 100:
        return 1
    return 5
