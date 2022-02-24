import parse
import sys
from dataclasses import dataclass
from typing import Dict, List
from scipy.stats import logistic
import collections


def project_value(project, today):
    # alfa = 1
    # beta = 1
    if project.best_before - project.duration >= today:
        real_score = project.score
    else:
        # CUIDADO
        excess_days = today + project.duration - project.best_before
        real_score = min(project.score - excess_days, 0)

    # print("PS: ", project.score)
    # print("RS: ", real_score)

    if real_score == 0:
        return 0

    value = real_score*logistic.cdf(today+project.duration-project.best_before)

    # TODO: INCLUIR COSTE DE PERSONAL
    return value


def solvable(project, people_dict):
    pass

@dataclass
class Assignment:
    name: str
    assignees: List[str]

@dataclass
class Solution:
    projects : List[Assignment]

    def __init__(self, projs):
        self.projects = projs

    def write_to_file(self, path: str, inp: parse.Input):
        with open(path, 'w') as f:
            print(len(self.projects), file=f)

            for assignment in self.projects:
                print(assignment.name, file=f)
                print(" ".join(assignment.assignees), file=f)


if __name__ == '__main__':
    inp = parse.read_file(sys.argv[1])

    today = 0
    projects = inp.projects.copy()

    people_dict = collections.defaultdict(set)
    for person in inp.contributors:
        for skill, level in person.skills:
            for level_counter in range(level+1):
                people_dict[(skill, level_counter)].add(person.name)

    while projects:
        projects.sort(key=lambda x: project_value(x, today), reverse=True)

        for p in projects:
            if solvable(p, people_dict):


            # Eliminar proyectos resueltos de projects

        today += 1

    solution = Solution([
        Assignment("WebServer", ["Bob", "Anna"]),
        Assignment("Logging", ["Anna"]),
        Assignment("WebChat", ["Maria", "Bob"]),
    ])

    solution.write_to_file('../outputs/{}'.format(sys.argv[1]), inp)