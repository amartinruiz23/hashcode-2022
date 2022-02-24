from dataclasses import dataclass
from collections import defaultdict
from typing import Dict, List, Any

@dataclass
class Role:
    language: str
    level: int

@dataclass
class Contributor:
    name: str
    N: int
    skills: List[Role]

@dataclass
class Project:
    name: str
    duration: int
    score: int
    best_before: int
    R: int
    roles: List[Role]

@dataclass
class Input:
    C: int
    P: int
    contributors: List[Contributor]
    projects: List[Project]


def read_file(_: str) -> Input:
    return Input(0,0,[],[])   
    

