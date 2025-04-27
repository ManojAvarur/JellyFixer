from typing import List, TypedDict, NotRequired

class DeleteConfigType(TypedDict):
    name: str
    formats: NotRequired[List[str]]
    match_type: NotRequired[str]