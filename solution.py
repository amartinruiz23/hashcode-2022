
import parse
import sys
from dataclasses import dataclass
from typing import Dict

Intersection = int
Street = str

@dataclass
class Solution:
    def __init__(self):
        pass

    def write_to_file(self, path: str, inp):
        with open(path, 'w') as f:
            print("This is the output", file=f)

inp = parse.read_file(sys.argv[1])
solution = Solution()
solution.write_to_file('../outputs/{}'.format(sys.argv[1]), inp)