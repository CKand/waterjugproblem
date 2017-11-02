### Author: Amal Zouaq
### azouaq@uottawa.ca
## Author: Hadi Abdi Ghavidel
## habdi.cnlp@gmail.com
import timeit

import numpy as np
import random
from searchdir.blindSearch.breadthfirst_search import *
from searchdir.blindSearch.depthfirst_search import *
from searchdir.heuristicSearch.astar_search import *
from searchdir.state import *

#global goal state
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

class EightPuzzleState(State):

    #initializes the eight puzzle with the configuration passed in parameter (numbers)
    def __init__(self, numbers):
        # TO COMPLETE
        #receives list of nine numbers, set attribute items accordingly
        self.items = [numbers[0], numbers[1], numbers[2],
                      numbers[3], numbers[4], numbers[5],
                      numbers[6], numbers[7], numbers[8]]


    #returns a boolean value that indicates if the current configuration is the same as the goal configuration
    def isGoal(self):
        # TO COMPLETE
        # if items match goal_state, then we have a solution and return true
        if self.items == goal_state:
            return True
        # else we return false
        else:
            return False


    # returns the set of legal actions in the current state
    def possibleActions(self):
        # TO COMPLETE

        # instantiate list
        validMoves = []

        # add moves to list that are valid based on position in grid
        if self.items.index(0) == 0:
            validMoves.append([self.items[1], self.items[0], self.items[2],
                               self.items[3], self.items[4], self.items[5],
                               self.items[6], self.items[7], self.items[8]])
            validMoves.append([self.items[3], self.items[1], self.items[2],
                               self.items[0], self.items[4], self.items[5],
                               self.items[6], self.items[7], self.items[8]])

        elif self.items.index(0) == 1:
            validMoves.append([self.items[0], self.items[2], self.items[1],
                               self.items[3], self.items[4], self.items[5],
                               self.items[6], self.items[7], self.items[8]])
            validMoves.append([self.items[0], self.items[4], self.items[2],
                               self.items[3], self.items[1], self.items[5],
                               self.items[6], self.items[7], self.items[8]])
            validMoves.append([self.items[1], self.items[0], self.items[2],
                               self.items[3], self.items[4], self.items[5],
                               self.items[6], self.items[7], self.items[8]])

        elif self.items.index(0) == 2:
            validMoves.append([self.items[0], self.items[2], self.items[1],
                               self.items[3], self.items[4], self.items[5],
                               self.items[6], self.items[7], self.items[8]])
            validMoves.append([self.items[0], self.items[1], self.items[5],
                               self.items[3], self.items[4], self.items[2],
                               self.items[6], self.items[7], self.items[8]])

        elif self.items.index(0) == 3:
            validMoves.append([self.items[3], self.items[1], self.items[2],
                               self.items[0], self.items[4], self.items[5],
                               self.items[6], self.items[7], self.items[8]])
            validMoves.append([self.items[0], self.items[1], self.items[2],
                               self.items[4], self.items[3], self.items[5],
                               self.items[6], self.items[7], self.items[8]])
            validMoves.append([self.items[0], self.items[1], self.items[2],
                               self.items[6], self.items[4], self.items[5],
                               self.items[3], self.items[7], self.items[8]])

        elif self.items.index(0) == 4:
            validMoves.append([self.items[0], self.items[4], self.items[2],
                               self.items[3], self.items[1], self.items[5],
                               self.items[6], self.items[7], self.items[8]])
            validMoves.append([self.items[0], self.items[1], self.items[2],
                               self.items[4], self.items[3], self.items[5],
                               self.items[6], self.items[7], self.items[8]])
            validMoves.append([self.items[0], self.items[1], self.items[2],
                               self.items[3], self.items[5], self.items[4],
                               self.items[6], self.items[7], self.items[8]])
            validMoves.append([self.items[0], self.items[1], self.items[2],
                               self.items[3], self.items[7], self.items[5],
                               self.items[6], self.items[4], self.items[8]])

        elif self.items.index(0) == 5:
            validMoves.append([self.items[0], self.items[1], self.items[5],
                               self.items[3], self.items[4], self.items[2],
                               self.items[6], self.items[7], self.items[8]])
            validMoves.append([self.items[0], self.items[1], self.items[2],
                               self.items[3], self.items[5], self.items[4],
                               self.items[6], self.items[7], self.items[8]])
            validMoves.append([self.items[0], self.items[1], self.items[2],
                               self.items[3], self.items[4], self.items[8],
                               self.items[6], self.items[7], self.items[5]])

        elif self.items.index(0) == 6:
            validMoves.append([self.items[0], self.items[1], self.items[2],
                               self.items[6], self.items[4], self.items[5],
                               self.items[3], self.items[7], self.items[8]])
            validMoves.append([self.items[0], self.items[1], self.items[2],
                               self.items[3], self.items[4], self.items[5],
                               self.items[7], self.items[6], self.items[8]])

        elif self.items.index(0) == 7:
            validMoves.append([self.items[0], self.items[1], self.items[2],
                               self.items[3], self.items[4], self.items[5],
                               self.items[7], self.items[6], self.items[8]])
            validMoves.append([self.items[0], self.items[1], self.items[2],
                               self.items[3], self.items[7], self.items[5],
                               self.items[6], self.items[4], self.items[8]])
            validMoves.append([self.items[0], self.items[1], self.items[2],
                               self.items[3], self.items[4], self.items[5],
                               self.items[6], self.items[8], self.items[7]])

        else:
            validMoves.append([self.items[0], self.items[1], self.items[2],
                               self.items[3], self.items[4], self.items[8],
                               self.items[6], self.items[7], self.items[5]])
            validMoves.append([self.items[0], self.items[1], self.items[2],
                               self.items[3], self.items[4], self.items[5],
                               self.items[6], self.items[8], self.items[7]])

        # return list of number lists (for usage to create new puzzle states)
        return validMoves

    # applies the result of the move on the current state
    def executeAction(self, move):
        # TO COMPLETE
        # Create new puzzle based on move and return it
        self.items = move
        """newPuzzle = EightPuzzleState(move)
        return newPuzzle"""

    # returns true if the current state is the same as other, false otherwise
    def equals(self, other):
        # TO COMPLETE
        # if items of both states are the same, then they are the same state and return true
        if self.items == other.items:
            return True
        # otherwise they are not and return false
        else:
            return False


    # prints the grid representing the current state
    # e.g. -----------
        # |   | 1 | 2 |
        # -----------
        # | 3 | 4 | 5 |
        # -----------
        # | 6 | 7 | 8 |
        # -----------
    def show(self):
        # TO COMPLETE
        # print as items as formatted as example above
        i=0
        print('-----------')
        while i < len(self.items):
            if (i!=2 and i != 5 and i != 8):
                if self.items[i] == 0:
                    print('|   ', end='')
                else:
                    print('|', self.items[i], '', end='')
            else:
                if self.items[i] == 0:
                    print('|   |')
                    print('-----------')
                else:
                    print('|', self.items[i], '|')
                    print('-----------')
            i=i+1

            # returns the cost of the action in parameter
    def cost(self, action):
        # TO COMPLETE
        # all costs in 8 puzzle game are cost 1
        return 1

    # returns the value of the heuristic for the current state
    # note that you can alternatively call heuristic1() and heuristic2() to test both heuristics with A*
    def heuristic(self):
        return self.heuristic1()
        #return self.heuristic2(self.items, goal_state)


    ## returns the value of your first heuristic for the current state
    # make sure to explain it clearly in your comment
    def heuristic1(self):
        # TO COMPLETE
        #the first heuristic is a double heuristic function on the number of misplaced tiles
        misplacedCount=0
        # 9 possible tiles
        for i in range(9):
            #this will match to see if the number in the given list matches its goal, from 0 to 8
            if i+1 != self.items[i]:
                misplacedCount +=1
                #returns the count od misplaced tiles
        return misplacedCount


    # returns the value of your first heuristic for the current state
    # make sure to explain it clearly in your comment
    def heuristic2(self, matrix, goal):
        #where matrix is the given state and goal is the final state
        #manhattan distance is calculated, i.e. the sum of tiles distances
        #compared to their target position
        return sum(abs(a-b) for a,b in zip(matrix,goal))


####################### SOLVABILITY ###########################

def issolvable(puzzle):
    puzzle_str = np.array(list(map(int, puzzle)))
    print("Puzzle string: ", puzzle_str)
    if inversions(puzzle_str) % 2:
        return False
    else : return True

def inversions(s):
    k = s[s != 0]
    return sum(
        len(np.array(np.where(k[i + 1:] < k[i])).reshape(-1))
        for i in range(len(k) - 1)
    )

def randomize(puzzle):
    puzzle = puzzle.shuffle_ran(puzzle, 1)
    puzzle_choice = []
    for sublist in puzzle.cells:
        for item in sublist:
            puzzle_choice.append(item)
    return puzzle, puzzle_choice

def shuffle_ran(self,board, moves):
    newState = board
    if moves==100:
        return newState
    else:
        newState.executeAction(random.choice(list(board.possibleActions())))
        moves= moves+1
    return self.shuffle_ran(newState, moves)

#######  SEARCH ###########################
EIGHT_PUZZLE_DATA = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
                     [1, 0, 2, 3, 4, 5, 6, 7, 8],
                     [1, 0, 2, 3, 4, 5, 8, 7, 6],
                     [4, 0, 6, 1, 2, 8, 7, 3, 5],
                     [1, 2, 8, 7, 3, 4, 5, 6, 0],
                     [5, 1, 3, 4, 0, 2, 7, 6, 8],
                     [1, 2, 5, 7, 6, 8, 0, 4, 3],
                     [4, 6, 0, 7, 2, 8, 3, 1, 5]]

#temporary
puzzle_choice = EIGHT_PUZZLE_DATA[6]
puzzle = EightPuzzleState(puzzle_choice)
#puzzle, puzzle_choice = randomize(puzzle)
print('Initial Config')
puzzle.show()
if not issolvable(puzzle_choice):
    print("NOT SOLVABLE")
else:
    start = timeit.default_timer()
    solution, nbvisited = breadthfirst_search(puzzle)
    stop = timeit.default_timer()
    printResults('BFS', solution, start, stop, nbvisited)

    #start = timeit.default_timer()
    #solution, nbvisited = depthfirst_search(puzzle)
    #stop = timeit.default_timer()
    #printResults('DFS', solution, start, stop, nbvisited)

    #start = timeit.default_timer()
    #solution, nbvisited = astar_search(puzzle)
    #stop = timeit.default_timer()
    #printResults('A*', solution, start, stop, nbvisited)

