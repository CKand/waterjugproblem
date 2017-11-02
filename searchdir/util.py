## Author: Amal Zouaq
### azouaq@uottawa.ca
### Author: Hadi Abdi Ghavidel
###habdi.cnlp@gmail.com

from operator import attrgetter

#Queue - Implementation of the data structure Queue
#Queue - Implementation of the data structure Queue
class Queue:
    # initializes the current data structure
    def __init__(self):
        self.nodes = []

    # returns the elements of the current data structure
    def show(self):
        return self.nodes

    # returns a boolean indicating whether the current data structure is empty or not
    def isEmpty(self):
        return len(self.nodes) == 0

    # add the element item to the current data structure
    def enqueue(self, item):
        self.nodes.append(item)

    # removes an element from the current data structure
    def dequeue(self):
        return self.nodes.pop(0)

    # returns the size of the current data structure (the number of elements)
    def size(self):
        return len(self.nodes)

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        return item in self.nodes


#Priority Queue Implementation of the data structure PriorityQueue
class PriorityQueue:
    # initializes the data structure
    def __init__(self, fct):
        self.queue = []
        self.sortFct=fct

    # returns the elements of the current data structure
    def show(self):
        return self.queue

    # returns a boolean indicating whether the current data structure is empty or not
    def isEmpty(self):
        return len(self.queue) == 0

    # add the element item to the current data structure
    def enqueue(self, item):
        if self.sortFct == "A*":
            self.queue.append(item)
            self.queue.sort(key=lambda x: x.f,reverse=True)


    # removes an element from the current data structure
    def dequeue(self,item):
        if item is None:
            return self.queue.pop()
        else:
            for i,node in enumerate(self.queue):
                if node.state.equals(item.state):
                    return self.queue.pop(i)


    # returns the size of the current data structure (the number of elements)
    def size(self):
        return len(self.queue)

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        for nodes in self.queue:
            if nodes.state.equals(item.state):
                return True
        return False

#Stack - Implementation of the data structure Stack
class Stack:
    # initializes the data structure
    def __init__(self):
        self.stack = []

    # returns the elements of the current data structure
    def show(self):
        return self.stack

    # returns a boolean indicating whether the current data structure is empty or not
    def isEmpty(self):
        return len(self.stack) == 0

    # add the element item to the current data structure
    def push(self, item):
        self.stack.append(item)

    # removes an element from the current data structure
    def pop(self):
        return self.stack.pop()

    # returns the size of the current data structure (the number of elements)
    def size(self):
        return len(self.stack)

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        for nodes in self.stack:
            if nodes.state.equals(item.state):
                return True
        return False

#Prints results for search alorithms
def printResults(alg, solution, start, stop, nbvisited):
    try:
        result, depth = solution.extractSolutionAndDepth()
        if result != []:
            print("The Solution is  ", (result))
            print("The Solution is at depth ", depth)
            print("The path cost is ", solution.getcost())
            print('Number of visited nodes:', nbvisited)
            time = stop - start
            print("The execution time is ", time, "seconds.")
            print("Done!")
    except AttributeError:
        print("No solution")
    except MemoryError:
        print("Memory Error!")
