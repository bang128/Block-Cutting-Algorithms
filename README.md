# COMP257-Final-Project

## Description
   The problem is to decide how to cut a block of gold into smaller pieces in order to maximize the profit when selling the gold, knowing that pieces with different weights cost differently. For this problem, I am provided with the weights of some pieces and their corresponding costs. If the weight of a certain piece is not given, I will not get any money for selling that piece. To solve this problem, I will develop three algorithms which are brute force, greedy and dynamic programming in Python. These algorithms take 2 inputs and return 2 outputs.

## Python files
- algorithms.py includes 3 functions for the 3 algorithms: Brute Force, Greedy and Dynamic Programming. These 3 functions take 2 arguments:
   - block_weight: the total weight of the given gold block
   - weight_cost: a dictionary in which keys are weights and values are the corresponding costs (missing weights cost 0).
- main_test.py includes 2 functions:
   - The test function takes an input file as its argument (the input file contains the total weight of the given gold block, and a list of weights and corresponding costs). This function is to test the 3 algorithms with each test case. 
   - The main function is to run the test function with 5 test cases.

## Text files
- There are 5 .txt files that contains all information for the 5 test cases. The test function will take each of these .txt files as the argument.

## How to run
`python3 main_test.py`
