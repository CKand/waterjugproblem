### Author: Amal Zouaq
### azouaq@uottawa.ca
## Author: Hadi Abdi Ghavidel
## habdi.cnlp@gmail.com

## Modified from EightPuzzleState.py from Assignment 1

import timeit

import numpy as np
import random

from searchdir.blindSearch.depthfirst_search import *
from searchdir.heuristicSearch.astar_search import *
from searchdir.blindSearch.breadthfirst_search import *
from searchdir.state import *
from searchdir.util import *

class WaterJugPuzzleState(State):

    #initializes the eight puzzle with the configuration passed in parameter (puzzle state values)
    def __init__(self, numbers):
        self.jugs = numbers


    # returns a boolean value that indicates if the current configuration is the same as the goal configuration
    def isGoal(self):
        # double check that state[0] represents 4G jug
        return self.jugs[0] == 2;


    # returns the set of legal actions in the current state
    def possibleActions(self):
        # get current states for each jug
        #where jugOne and jugTwo are the size of the jugs
        jugOne=4
        jugTwo=3
        jugOneState = self.jugs[0]
        jugTwoState = self.jugs[1]

        # set of possible states from current state
        states = set()

        # fill jugOne completely
        states.add((jugOne, jugTwoState))
        # fill jug two completely
        states.add((jugOneState, jugTwo))
        # empty jug one
        states.add((0, jugTwoState))
        # empty jug two
        states.add((jugOneState, 0))
        # fill jug one using jug two
        if jugTwoState < jugOne - jugOneState:
            states.add((min(jugOne, jugTwoState + jugOneState), 0))
        else:
            states.add((min(jugOne, jugTwoState + jugOneState), jugTwoState - (jugOne - jugOneState)))
        # fill jug two using jug one
        if jugOneState + jugTwoState < jugTwo:
            states.add((0, min(jugTwoState + jugOneState, jugTwo)))
        else:
            states.add((jugOneState - (jugTwo - jugTwoState), min(jugTwoState + jugOneState, jugTwo)))

        # don't think it matters if we sort or not; sorted(states)
        return states


    # applies the result of the move on the current state
    def executeAction(self, move):
        # new states from 'move'
        newJugOneState = move[0]
        newJugTwoState = move[1]

        # replace the old states to execute action
        self.jugs[0] = newJugOneState
        self.jugs[1] = newJugTwoState

        return


    # returns true if the current state is the same as other, false otherwise
    def equals(self, other):
        #simple return
        return self.jugs == other.jugs

    # prints the values of the two water jugs
    def show(self):
        # simple print and return
        #print("We are at ", self.jugs[0], ", ", self.jugs[1])

        return self.jugs

    # returns the cost of the action in parameter
    def cost(self, action):
        # we assume cost of each action is the arc length
        return 1

    # returns the value of the heuristic for the current state
    # note that you can alternatively call heuristic1() and heuristic2() to test both heuristics with A*
    def heuristic(self):
        # return self.heuristic1()
        return self.heuristic1()

    ## returns the value of your first heuristic for the current state
    # make sure to explain it clearly in your comment
    def heuristic1(self):
        # we have no implementation for this one so far
        return abs(self.jugs[0] - 2) + abs(self.jugs[1] - 2)


    # returns the value of your first heuristic for the current state
    # make sure to explain it clearly in your comment
    def heuristic2(self, matrix, goal):
        # Distance from goal for both jugs, as described in the report
        # g(c) will always be 1.
        return


####################### SOLVABILITY ###########################

def issolvable(jugOne, jugTwo, goal):
    # if the goal state is more than the possible jug amount totals, an invalid problem is given.
    # therefore just return that it is a failure, as it cannot be computed
    if goal > jugOne + jugTwo:
        print("Fails, an invald problem provided.")
        return

#######  SEARCH ###########################

# We start with two empty jugs,
WATER_JUG_DATA = [[0,0]]

puzzle_choice = WATER_JUG_DATA[0]
puzzle = WaterJugPuzzleState(puzzle_choice)
print('Initial Config')
puzzle.show()

start = timeit.default_timer()
solution, nbvisited = depthfirst_search(puzzle)
stop = timeit.default_timer()
printResults('DFS', solution, start, stop, nbvisited)

start = timeit.default_timer()
solution, nbvisited = breadthfirst_search(puzzle)
stop = timeit.default_timer()
printResults('BFS', solution, start, stop, nbvisited)

start = timeit.default_timer()
solution, nbvisited = astar_search(puzzle)
stop = timeit.default_timer()
printResults('A*', solution, start, stop, nbvisited)
