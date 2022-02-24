
import parse
import sys
from dataclasses import dataclass
from typing import Dict, List


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



inp = parse.read_file(sys.argv[1])
solution = Solution([
    Assignment("WebServer", ["Bob", "Anna"]),
    Assignment("Logging", ["Anna"]),
    Assignment("WebChat", ["Maria", "Bob"]),
])
solution.write_to_file('../outputs/{}'.format(sys.argv[1]), inp)