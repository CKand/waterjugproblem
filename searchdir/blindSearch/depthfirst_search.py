from searchdir.node import *
from searchdir.util import *

## This method must implement depdth-first search (DFS)
## It must return the solution node and the number of visited nodes
def depthfirst_search(initialState):
    print('DFS ----------------------------------')

    # initialize a stack for open
    open = Stack()
    # initialize a list for close
    close = []

    # create new node from initial state
    newNode = Node(initialState)
    # push this node to our open stack
    open.push(newNode)

    # we want to execute as long as open is not empty
    while not open.isEmpty():
        # the current node is popped from open
        currentNode = open.pop()

        # uncomment if you want to see the algorithm working
        #print(currentNode.state.show())

        # if the current node if it is the goal state, then we just stop
        if currentNode.state.isGoal():
            return currentNode, len(close)
        else:
            # otherwise we expand from the current node to get its children nodes (the possible actions)
            childrenNodes = currentNode.expand()

            # we add the current node to the list of visited states (close)
            close.append(currentNode.state.show())
            # for all possible actions
            for c in childrenNodes:
                # we check that we haven't visited this state before or whether it is already on our stack
                if c not in open.show() and c.state.show() not in close:
                    # if it is not, then we want to add it to our open stack
                    open.push(c)
    # we reach here if open is empty and there is no solution
    return [],len(close)