# This file contains functions to extract relevant information from the reference database
import re
from datetime import datetime, timedelta
import os
import logging
from typing import Any, Iterator, List, Mapping, Optional 
from pydantic import BaseModel

logger = logging.getLogger(__name__)

"""Load a collection of references from
    a bibtex file and fetch document file_paths.
"""

def parse_entry(raw_string):
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
extract_first_owner = lambda entry, owners_delimiter= r" *[/,]+ *": re.split(owners_delimiter, entry['owner'].lower())[0]
#Author
extract_author = lambda entry: entry['author'].lower()
extract_first_author = lambda entry, owners_delimiter= r" *[/,]+ *": re.split(owners_delimiter, entry['author'])[0]
#Journal
extract_journal = lambda entry: entry['journal'].lower()
#Key
extract_key = lambda entry: entry['key']
    
def create_mla_citation(
    citation_dict: dict,
    owners_delimiter = r" *[/,]+ *",
) -> str:
    """Create a MLA citation from a dictionary containing the relevant information."""
    citation_parts = []
    citation_parts.append(f"{extract_first_author(citation_dict, owners_delimiter=owners_delimiter)} et al.,")
    citation_parts.append(f"\"{citation_dict['title']}\",")
    citation_parts.append(f"*{citation_dict['journal']}*,")
    citation_parts.append(f"({citation_dict['year']}),")
    citation_parts.append(f"{citation_dict['creationdate']},")
    citation_parts.append(f"{citation_dict['owner']}")

    mla_citation = " ".join(citation_parts)

    return mla_citation


def load_bibtex_entries(keys: List[str],
                        bib_path: str, # r'...\QudevRefDB.bib',
                        pdf_dir: str , # "Q:/PaperArchive/",
                        owners_delimiter = r" *[/,]+ *", 
                        encoding="utf8",
                        *optional_fields: Optional[str]):
    """ Input a list of keys and return a list of dictionaries containing the relevant information 
        from the corrsponding citation in the referenence database.
        Args:
            keys: List of keys to extract from the bibtex file.
            file_path: Path to the bibtex file.
            pdf_dir: Path to saved PDFs.
            owners_delimiter: Regex-type separation between multiple owners.
            encoding: Encoding of the bibtex file.
            optional_fields: List of optional fields to include in the document dictionary.
    """
    
    with open(bib_path, "r", encoding= encoding) as f:
        file_contents = f.read()
        
    citations = []
    remaining_keys = keys.copy()
    
    for raw_string in file_contents.split('\n@')[1:]:
        try:
            entry = parse_entry(raw_string) #Parse raw string as a dictionary
            
            if entry==None:
                continue
            
            if entry['ID'] not in keys: #check if entry is in keys
                continue
            
            #Check pdfs (to do: could also check that it's not the online pdf)
            if 'file' in entry:
                entry['file'] = os.path.join(pdf_dir + entry['file'].replace('\\\\','/').split(':')[1])
            else:
            # print(f"Warning: file {entry['ID']} by {entry['owner']} does not have a pdf attached and will be ignored.")
                entry['file'] = None #Will be shown as None in the merged pdf
                
            #Keep useful fields for citation (use to simplify database for debugging)
            fields = ['ID', 'author', 'title', 'journal', 'year', 'file', 'creationdate', 'owner'] + list(optional_fields)
            entry = {f: entry.get(f, "") for f in fields} #If field not filled, defaults to ""
            citations.append(entry)
            remaining_keys.remove(entry['ID'])         
        except:
            continue
    print(f"{len(remaining_keys)} key(s) not found in database: {remaining_keys}")
    return citations

if __name__=="__main__":
    keys = ['Storz2023', 'Zhong2019']
    bib_path = r'C:\Users\domin\Documents\ETH\qudev\RefDB\QudevRefDB.bib'
    pdf_dir = "//group-data.phys.ethz.ch/qudev/PaperArchive/"
    citations = load_bibtex_entries(keys, bib_path=bib_path, pdf_dir=pdf_dir)
    print(citations)
    print(create_mla_citation(citations[0]))
