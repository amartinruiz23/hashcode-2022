#!/bin/bash
set -e

pushd input_data
time python3 ../solution.py a_an_example.in.txt
time python3 ../solution.py b_better_start_small.in.txt
time python3 ../solution.py c_collaboration.in.txt
time python3 ../solution.py d_dense_schedule.in.txt
time python3 ../solution.py e_exceptional_skills.in.txt
time python3 ../solution.py f_find_great_mentors.in.txt
popd

zip ohno -r *.py