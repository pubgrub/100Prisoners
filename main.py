from random import random, sample

num_prisoners = 4
num_runs = 5

TESTS = { random:0}

boxes = sample(range(num_prisoners), k=num_prisoners)


def run( num_prisoners, num_runs, tests):
  boxes_to_open = num_prisoners / 2
  
  
  for r in range(num_runs):
    for p in range(num_prisoners):



