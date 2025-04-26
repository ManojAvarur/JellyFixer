from typing import List, TypedDict

class DeleteConfigType(TypedDict):
    name: str
    types: List[str]
    complete_match: bool