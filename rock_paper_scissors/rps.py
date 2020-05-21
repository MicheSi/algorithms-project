#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here
  # make list for all possible moves
  all_moves = []
  # make list of move options
  options = ['rock', 'paper', 'scissors']

  pass


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')