from operator import attrgetter
from searchdir.node import *
from searchdir.util import PriorityQueue
## This method must implement A* search
## It must return the solution node and the number of visited nodes
def astar_search(initialState):
    print('A* ------------------------------------')
    #Initiate Priority Queue with A* function and push initial node
    pqueue = PriorityQueue(fct="A*")
    initNode = Node(initialState)
    pqueue.enqueue(initNode)
    #Initiate explored list
    explored = []
    # Initialize visited counter to count number of visited nodes
    visited = 1

    while not pqueue.isEmpty():
        #Pop the node from Queue with highest priority (smallest cost + heauristic property)
        currentNode = pqueue.dequeue(None)
        # While node dequeued explore node
        if not currentNode.state.isGoal():
            visited += 1
            #If node is not Goal, add it to closed
            explored.append(currentNode)

            #Generate successors from current node
            for successorNodes in currentNode.expand():
                #Remove a duplicate of successor node if it's in frontier with a higher cost
                if pqueue.__contains__(successorNodes):
                    nodeInOpen = pqueue.dequeue(successorNodes)
                    #if new path is not less than old path, leave the frontier unchanged
                    if successorNodes.f >= nodeInOpen.f:
                        pqueue.enqueue(nodeInOpen)

                #If Successor Node in closed list and successorNode has lower f than node in closed, remove node from closed
                inClosedNode = inExplored(successorNodes,explored)
                if (inClosedNode):
                    if (successorNodes.f < inClosedNode.f ):
                        explored.remove(inClosedNode)

                if not inExplored(successorNodes,explored) and not pqueue.__contains__(successorNodes):
                    pqueue.enqueue(successorNodes)
        else:
            print("Nodes remaining in Frontier",pqueue.size())
            return currentNode, visited

def inExplored(nodeUnderStudy,explored):
    for node in explored:
        if nodeUnderStudy.state.equals(node.state):
            return node
    return False

