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


def assign_people(project, skills, people):
    selected_people = []
    for skill, level in project.roles.items():
        available_people = list(skills[(skill, level)])
        available_people.sort(key=lambda x: person_cost(x, skill))
        selected_people.append(available_people[0])
        if people[available_people[0]][skill] == level:
            people[available_people[0]][skill] = level + 1
    return selected_people


def person_cost(person, skill):
    #cost = 1
    #for skill, level in person.skills:
    return 1


def update_skills(people_assigned, skills, people):
    for person in people_assigned:
        for skill, level in people[person].items():
            for level_counter in range(level + 1):
                if skills[(skill, level_counter)].__contains__(person):
                    skills[(skill, level_counter)].remove(person)


def solvable(project: parse.Project, skills):
    for role, level in project.roles.items():
        people_in_current_level = skills[(role, level)]
        if people_in_current_level:
            continue
        return False
    return True


def update_current_projects(current_projects, skills, today, people):
    for project, end_date in current_projects:
        if end_date == today:
            current_projects.remove((project, end_date))
            for person in project.assignees:
                for skill, level in people[person].items():
                    for level_counter in range(level + 1):
                        skills[(skill, level_counter)].add(person)


def initialize_skills(inp):
    skills = collections.defaultdict(set)
    for person in inp.contributors:
        for skill, level in person.skills.items():
            for level_counter in range(level + 1):
                skills[(skill, level_counter)].add(person.name)
    return skills


def initialize_people(inp):
    people = {}
    for person in inp.contributors:
        people[person.name] = person.skills
    return people


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

    assignments = []
    current_projects = []

    today = 0
    projects = inp.projects.copy()

    skills = initialize_skills(inp)
    people = initialize_people(inp)

    while projects and today < 100:
        print(today)
        # Free the people that has already finished a project

        projects.sort(key=lambda x: project_value(x, today), reverse=True)

        for project in projects:
            #print(solvable(project, skills))
            if solvable(project, skills):
                people_assigned = assign_people(project, skills, people)
                #print(people_assigned)
                update_skills(people_assigned, skills, people)
                #print(skills)
                projects.remove(project)
                assignment = Assignment(project.name, people_assigned)
                assignments.append(assignment)
                current_projects.append((assignment, today+project.duration))

        # print("PROJECTS: ", projects)
        print("CURRENT PROJECTS: ", current_projects)

        update_current_projects(current_projects, skills, today, people)
        today += 1


    # solution = Solution([
    #     Assignment("WebServer", ["Bob", "Anna"]),
    #     Assignment("Logging", ["Anna"]),
    #     Assignment("WebChat", ["Maria", "Bob"]),
    # ])

    solution = Solution(assignments)

    solution.write_to_file('../outputs/{}'.format(sys.argv[1]), inp)