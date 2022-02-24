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


def read_file(name: str) -> Input:
    with open(name, 'r') as f:
        C, P = [int(x) for x in f.readline().split(" ")]

        contributors = []
        for _ in range(C):
            name_and_N = f.readline().split(" ")
            contributor_name = name_and_N[0]
            N = int(name_and_N[1])
            skills = []

            for _ in range(N):
                raw_skill = f.readline().split(" ")
                skill_name = raw_skill[0]
                level = int(raw_skill[1])
                skills.append(Role(skill_name, level))
            
            contributors.append(Contributor(contributor_name, N, skills))
        
        projects = []
        for _ in range(P):
            name_and_stuff = f.readline().split(" ")
            project_name = name_and_stuff[0]
            duration = int(name_and_stuff[1])
            score = int(name_and_stuff[2])
            best_before = int(name_and_stuff[3])
            R = int(name_and_stuff[4])

            roles = []
            for _ in range(R):
                role_and_level = f.readline().split()
                role_name = role_and_level[0]
                role_level = int(role_and_level[1])
                roles.append(Role(role_name, role_level))
            
            projects.append(Project(project_name, duration, score, best_before, R, roles))


    return Input(C,P,contributors,projects)   
    

