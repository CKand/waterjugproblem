from operator import attrgetter
from searchdir.node import *
from searchdir.util import PriorityQueue

## This method must implement A* search
## It must return the solution node and the number of visited nodes
def astar_search(initialState):
	print('A*------------------------------')

	# create the inital queue/list to look through nodes
	priorityQueue = PriorityQueue(0)
	#add the inital state as a node to the priority queue
	tempNode = Node(initialState)
	priorityQueue.enqueue(tempNode)
	closed = []
	# used for the requirement to return number ofnodes checked
	visitedNodesList = []
	# loop through nodes as long as long as queue is not empty
	while (not priorityQueue.isEmpty()):
		# we store current nodes after dequeuing from our priority queue
		currentNode = priorityQueue.dequeue()
		if (currentNode.state.isGoal()):
			# return goal node and number of nodes looked at as expected
			return currentNode, len(visitedNodesList)
		# add nodes to lists for checking purposes later
		closed.append(currentNode)
		visitedNodesList.append(currentNode.state.items)
		# loop through children and calculate cost using cost and heuristic,
		# to determine if its the appripriate path
		#print(currentNode.state.show())
		for child in currentNode.expand():
			#depending on the heuristic, determine what should happen to the childnode 
			cost = currentNode.g + child.h
			if child in priorityQueue.show() and cost < child.g:
				priorityQueue.dequeue()
			if child in closed and cost < child.g:
				closed.remove(child)
			if child not in priorityQueue.show() and child not in closed and child.state.items not in visitedNodesList:
				priorityQueue.enqueue(child)

	if (priorityQueue.isEmpty()):
		return None, 0


