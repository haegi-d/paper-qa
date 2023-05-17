# Todo
1. Test paper-qa with my own papers
2. Can I restrict on using information from only one paper?
   1. Ask for experimental ect.
   2. Use the other papers and the paper to determine which previous paper it cited for its work and why?
      1. Hard because citations always change
3. Split paper into pages OR (Title, authors, abstract) and content in pages, bibliography, supplements
   1. Find similar papers and check if they are cited and where
   2. Approach the problem from behind! Go through the cited references and find the ones that are discussing a specific topic, e.g. previous similar work



## Code Snippets
If regular experession could be a solution:
```python
# Define the topic you want to search for
topic = 'machine learning'

# Define the regular expression pattern to search for the topic and its corresponding reference
pattern = r'\[(\d+)\]\s+(.*?)\.\s*(%s)' % re.escape(topic)

# Search for the pattern in the text and print the results
for match in re.findall(pattern, text):
    reference_number = match[0]
    reference_text = match[1]
    print(f'Reference [{reference_number}]: {reference_text}')
```


