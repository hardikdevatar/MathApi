from pydantic import BaseModel
from typing import (
    Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union
)


# Create ToDo Schema (Pydantic Model)
class mathCreate(BaseModel):
    listOfNumbers: List[int] = [1,3,4,5,6]
    quantifier : int