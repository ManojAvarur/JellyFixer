from typing import List, TypedDict, NotRequired

class DeleteConfigType(TypedDict):
    name: str
    formats: NotRequired[List[str]]
    complete_match: NotRequired[bool]