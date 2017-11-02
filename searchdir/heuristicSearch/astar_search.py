#import sys
#sys.path.append('C:\\Users\\Christine\\Documents\\Year4\\CSI4106\\Bonus Assignment\\waterjugproblem-master\\waterjugproblem-master\\')

from operator import attrgetter
from searchdir.node import *
from searchdir.util import PriorityQueue
## This method must implement A* search
## It must return the solution node and the number of visited nodes
def astar_search(initialState):
    print('A* ------------------------------------')
    # create the inital queue/list to look through nodes
    frontierPQ = PriorityQueue(fct="A*")
    #add the inital state as a node to the priority queue
    initialNode = Node(initialState)
    frontierPQ.enqueue(initialNode)
    #Initiate exploredNodes list
    exploredNodes = []

    # loop through nodes as long as long as queue is not empty
    while not frontierPQ.isEmpty():
        # we store current node after dequeuing from our priority queue, with the lowest priority
        currentNode = frontierPQ.dequeue(None)
        # explore the node to see if it is the goal
        if not currentNode.state.isGoal():
            #add it to closed since it is not the goal
            exploredNodes.append(currentNode)

            #Create child nodes from current node
            for childNodes in currentNode.expand():
                #Remove a duplicate of successor node if it's in frontier with a higher cost
                #################
                #not sure what this does and not sure if we need to keep it for or case?? 
                if frontierPQ.__contains__(childNodes):
                    checkNodeOpen = frontierPQ.dequeue(childNodes)
                    #if new path is not less than old path, leave the frontier unchanged
                    if childNodes.f >= checkNodeOpen.f:
                        frontierPQ.enqueue(checkNodeOpen)

                #If Successor Node in closed list and successorNode has lower f than node in closed, remove node from closed
                checkNodeClosed = inexploredNodes(childNodes,exploredNodes)
                if (checkNodeClosed):
                    if (childNodes.f < checkNodeClosed.f ):
                        exploredNodes.remove(checkNodeClosed)
                ################################

                #if not already in frontier or not alreadt in explored nodes, add to frontier 
                if not inexploredNodes(childNodes,exploredNodes) and not frontierPQ.__contains__(childNodes):
                    frontierPQ.enqueue(childNodes)
        else:
            #### dontt hink we need this 
            #print("Nodes remaining in Frontier",frontierPQ.size()) 
            return currentNode, len(exploredNodes) # add one to length for the current node being checked

###################### this looks so obviously fishy but i dunno what to do to make it look unstoled
def inexploredNodes(childNode,exploredNodes):
    for node in exploredNodes:
        if childNode.state.equals(node.state):
            return node
    return False

