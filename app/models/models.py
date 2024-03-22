# Standard library imports
from typing import List, Optional
# from datetime import date

# Related third party imports
from pydantic import BaseModel, UUID4, Field

# Local application specific imports

class Moment(BaseModel):
    id: UUID4 = Field(default_factory=UUID4)
    title: str
    description: Optional[str] = None
    # Additional attributes can be defined here as needed.

class Mosaic(BaseModel):
    id: UUID4 = Field(default_factory=UUID4)
    title: str
    moments: List[Moment] = []
    description: Optional[str] = None
    # Mosaics can have additional attributes like themes or goals.

class Tapestry(BaseModel):
    id: UUID4 = Field(default_factory=UUID4)
    title: str
    narrative: str
    description: Optional[str] = None
    # Mythos may include a broader story or narrative that influences one's life.

# class Day(BaseModel):
#     id: UUID4 = Field(default_factory=UUID4)
#     date: date
#     moments: List[Moment] = []
#     mosaics: List[Mosaic] = []
#     mythos: Optional[List[Mythos]] = None
#     # Days can be associated with moments, mosaics, and potentially influenced by one's mythos.

# class Session(BaseModel):
#     id: UUID4 = Field(default_factory=UUID4)
#     title: str
#     description: Optional[str] = None
#     # Sessions can be used to group moments or mosaics together.
