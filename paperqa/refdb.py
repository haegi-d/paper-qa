# This file contains functions to extract relevant information from the reference database
import re
from datetime import datetime, timedelta
import os
import logging
from langchain.document_loaders.base import BaseLoader
from typing import Any, Iterator, List, Mapping, Optional 
from langchain.docstore.document import Document

logger = logging.getLogger(__name__)

class BibtexLoader(BaseLoader):
    """Loads a bibtex file into a list of Documents.

    Each document represents one entry from the bibtex file.

    If a PDF file is present in the `file` bibtex field, the original PDF
    is loaded into the document text.
    """
    
    def __init__(
        self,
        keys: List[str],
        file_path: str =  r'C:\Users\domin\Documents\ETH\qudev\RefDB\QudevRefDB.bib',
        pdf_dir = "//group-data.phys.ethz.ch/qudev/PaperArchive/",
        owners_delimiter = r" *[/,]+ *", 
        encoding="utf8",
        *optional_fields: Optional[str],
    ):
        """Initialize the BibtexParser.

        Args:
            keys: List of keys to extract from the bibtex file.
            file_path: Path to the bibtex file.
            pdf_dir: Path to saved PDFs.
            owners_delimiter: Regex-type separation between multiple owners.
            encoding: Encoding of the bibtex file.
            optional_fields: List of optional fields to include in the document dictionary.

        """
        self.keys = keys
        self.file = file_path
        self.pdf_dir = pdf_dir
        self.owners_delimiter = owners_delimiter
        self.encoding = encoding
        self.fields = ['ID', 'author', 'title', 'journal', 'year', 'file', 'creationdate', 'owner'] + list(optional_fields)
        

    def _parse_entry(raw_string):
        """ Copied from JCcombi.ipynb 
        Manual parsing of bibtex file.
        (bibtex libraries are either slow or fail because of our bad database formatting)

        Relatively reliant on having a nice formatting
        Expected file format:
        some lines...
        @Entrytype{EntryID
        key = { Some {possibly weirdly formatted} stuff}
        ...
        }
        ...
        @Comment{Some Jabref information, useless for us}

        Takes a raw string and tries to extract a python dictionary from it
        If fails, either raises an exception or returns None which will be ignored
        """
        
        if raw_string.count('{') != raw_string.count('}'):
            raise Exception(f"The entry is badly formatted. Ignoring this entry...")
        #Could add additional checks

        start_index = raw_string.find('{')
        
        entry_type = raw_string[0:start_index]
        if entry_type=="Comment":
            return
        
        entry_list = raw_string[start_index+1:].split(',\n')

        entry_ID = entry_list[0]

        entry_dict = {}
        for item in entry_list:
            res = re.match("^\s*(\S*)\s*\=\s*\{(.*)\}$", item)
            if res is not None:
                entry_dict.update({res.groups()[0]: res.groups()[1]})
        
        #for debugging, could be commented out otherwise
        entry_dict['ID'] = entry_ID

        return entry_dict




    #Lambda functions to get custom data from entry dictionary

    #Function to get creationdate as time object
    def extract_time(entry):
        try:
            return datetime.strptime(entry['creationdate'],"%Y-%m-%d")
        except ValueError:
            return datetime.strptime(entry['creationdate'],"%Y-%m-%dT%H:%M:%S")
            
    #Owner to lowercase to be able to compare them
    extract_owner = lambda entry: entry['owner'].lower()
    #1st owner
    extract_first_owner = lambda entry: re.split(owners_delimiter, entry['owner'].lower())[0]
    #Author
    extract_author = lambda entry: entry['author'].lower()
    extract_first_author = lambda entry: re.split(owners_delimiter, entry['author'])[0]
    #Journal
    extract_journal = lambda entry: entry['journal'].lower()
    #Key
    extract_key = lambda entry: entry['key']


    def keys_to_citations(self) -> list[dict]:
        """ Input a list of keys and return a list of dictionaries containing the relevant information 
            from the corrsponding citation in the referenence database.
        """
        with open(self.file_path, "r", encoding=self.encoding) as f:
            file_contents = f.read()
            
        database_list = []
        remaining_keys = self.keys.copy()
        
        for raw_string in file_contents.split('\n@')[1:]:
            try:
                entry = self._parse_entry(raw_string) #Parse raw string as a dictionary
                
                if entry==None:
                    continue
                
                if entry['ID'] not in self.keys: #check if entry is in keys
                    continue
                
                #Check pdfs (to do: could also check that it's not the online pdf)
                if 'file' in entry:
                    entry['file'] = os.path.join(self.pdf_dir + entry['file'].replace('\\\\','/').split(':')[1])
                else:
                # print(f"Warning: file {entry['ID']} by {entry['owner']} does not have a pdf attached and will be ignored.")
                    entry['file'] = None #Will be shown as None in the merged pdf
                    
                #Keep useful fields for citation (use to simplify database for debugging)
                entry = {f: entry.get(f, "") for f in self.fields} #If field not filled, defaults to ""
                database_list.append(entry)
                remaining_keys.remove(entry['ID'])         
            except:
                continue
        print(f"{len(remaining_keys)} key(s) not found in database: {remaining_keys}")
        return database_list

    def create_mla_citation(citation_dict: dict
                            ) -> str:
        citation_parts = []
        citation_parts.append(f"{extract_first_author(citation_dict)} et al.,")
        citation_parts.append(f"\"{citation_dict['title']}\",")
        citation_parts.append(f"*{citation_dict['journal']}*,")
        citation_parts.append(f"({citation_dict['year']}),")
        citation_parts.append(f"{citation_dict['creationdate']},")
        citation_parts.append(f"{citation_dict['owner']}")

        mla_citation = " ".join(citation_parts)

        return mla_citation

if __name__=="__main__":
    keys = ['Storz2023', 'Zhong2019']
    citations = keys_to_citations(keys)
    print(citations)