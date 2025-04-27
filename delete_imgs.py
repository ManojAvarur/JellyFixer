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

    def __complete_match(self, file_loc: str, file_name: str, match_name: str) -> None:
        if file_name != match_name:
            return
        
        self.__files_to_delete.append(file_loc)

    def __end_match(self, file_loc: str, file_name: str, match_name: str) -> None:
        if not file_name.endswith(match_name):
            return
        
        self.__files_to_delete.append(file_loc)

    def process(self, file_loc: str) -> None:
        file_name: str = os_path.basename(file_loc)

        for config in self.__configs:
            name: str            = config['name']
            formats: List[str]   = config['formats'] if 'formats' in config else []
            match_type: str      = config['match_type'] if 'match_type' in config else 'complete_match'

            if not formats:
                if match_type == "complete_match":
                    self.__complete_match(file_loc, file_name, name)
                    continue
                
                if match_type == "end_match":
                    self.__end_match(file_loc, file_name, name)
                    continue

            for format in formats:
                match_name = f"{name}{format}"
                if match_type == "complete_match":
                    self.__complete_match(file_loc, file_name, match_name)
                    continue
                
                if match_type == "end_match":
                    self.__end_match(file_loc, file_name, match_name)
                    continue


    def close(self) -> None:
        if not self.__files_to_delete:
            print("No files found delete")
            return 
        
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Files to Delete:")
        for file_name in self.__files_to_delete:
            print(file_name)

        print(f"\n\t\tTotal files to delete: {len(self.__files_to_delete)}")

        if input("\nEnter [Y | Yes] to delete all the above mentioned files: ").lower() in ['y', 'yes']:
            for file_name in self.__files_to_delete:
                os.remove(file_name)


