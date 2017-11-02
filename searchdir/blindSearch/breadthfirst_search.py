#import sys
#sys.path.append('C:\\Users\\Christine\\Documents\\Year4\\CSI4106\\Bonus Assignment\\waterjugproblem-master\\waterjugproblem-master\\')

from searchdir.node import *
from searchdir.util import *

## This method must implement Breadth-first search (BFS)
## It must return the solution node and the number of visited nodes
def breadthfirst_search(initialState):
	print('BFS------------------------------')
    # initialize frontier as FIFO queue
	frontier = Queue()

	#create the first node from the initialstate
	tempNode = Node(initialState)
    # we enqueue the initial node
	frontier.enqueue(tempNode)
    # create empty list explored to represent set of explored nodes
	explored = []

	#as long as there is an item in the frontier, loop through
	while (not frontier.isEmpty()):
        # we store current nodes after dequeuing from our FIFO queue
		currentNode = frontier.dequeue()

		# if the initial node is the goal node, then we are done and we return it
		if (currentNode.state.isGoal()):
			return currentNode, 1
        # we add it to our explored nodes as we have now visited it
		#look through the children nodes of the current node
		for childNode in currentNode.expand():

			#if childnode has not already been seen, check if it matches the goal nodes
			if (childNode not in frontier and childNode.state.show() not in explored):
				# add action to explored
				explored.append(childNode.state.show())
				#if childnode is the goal node, exit and algorithm is done
				if childNode.state.isGoal():
					#returns the goal node and the number of visited nodes as required
					return childNode, len(explored)
                # add childNode to frontier
				frontier.enqueue(childNode)

	# if frontier is empty, then the search has failed, we return appropriately
	if (frontier.isEmpty()):
		return [],len(explored)


