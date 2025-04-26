import os
import os.path as os_path
from typing import List
from interface.base_interface import Base
from interface.delete_config_type import DeleteConfigType
from utility.config_reader import load_config

class DeleteImages(Base):
    def __init__(self, file_loc: str):
        self.__files_to_delete: List[str]       = []
        self.__configs: List[DeleteConfigType]  = load_config(file_loc)

    def process(self, file_loc: str) -> None:
        for config in self.__configs:
            name: str               = config['name']
            types: List[str]        = config['types'] if 'types' in config else []
            complete_match: bool    = config['complete_match'] if 'complete_match' in config else True

            
            


    def close(self) -> None:
        print("Closed")



