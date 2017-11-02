## Author: Amal Zouaq
### azouaq@uottawa.ca
### Author: Hadi Abdi Ghavidel
###habdi.cnlp@gmail.com

from operator import attrgetter

#Queue - Implementation of the data structure Queue
class Queue:
    # initializes the current data structure
    def __init__(self):
        # initialize items (our queue) as empty list
        self.items = []

    # returns the elements of the current data structure
    def show(self):
        # return its items
        return self.items

    # returns a boolean indicating whether the current data structure is empty or not
    def isEmpty(self):
        # check if items (our queue) is empty
        return self.items == []

    # add the element item to the current data structure
    def enqueue(self, item):
        # add to back of queue (left-most), LIFO
        self.items.insert(0,item)

    # removes an element from the current data structure
    def dequeue(self):
        # remove right-most item of queue, LIFO
        return self.items.pop()

    # returns the size of the current data structure (the number of elements)
    def size(self):
        # return length of queue as size
        return len(self.items)

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        # if not empty, return item in items
        if (len(self.items) == 0):
            return False
        return item in self.items


#Priority Queue Implementation of the data structure PriorityQueue
class PriorityQueue:
    # initializes the data structure
    def __init__(self, fct):
        # initialize priority queue using list to hold items
        self.items = []
        self.fct = fct

    # returns the elements of the current data structure
    def show(self):
        # return items
        return self.items

    # returns a boolean indicating whether the current data structure is empty or not
    def isEmpty(self):
        # return true/false if items is empty
        return self.items == []

    # add the element item to the current data structure
    def enqueue(self, item):
        # insert to back of priority queue (left-most)
        self.items.insert(0,item)

    # removes an element from the current data structure
    def dequeue(self):
        return self.items.pop()

    # returns the size of the current data structure (the number of elements)
    def size(self):
        # return length of priority queue as size
        return len(self.items)

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        # return item in items
        return item in self.items

#Stack - Implementation of the data structure Stack
class Stack:
    # initializes the data structure
    def __init__(self):
        # set stack to be empty list items
        self.items = []

    # returns the elements of the current data structure
    def show(self):
        # return stack
        return self.items

    # returns a boolean indicating whether the current data structure is empty or not
    def isEmpty(self):
        # check if stack is empty, boolean true or false
        return self.items == []

    # add the element item to the current data structure
    def push(self, item):
        # push to front of stack, FIFO
        self.items.append(item)

    # removes an element from the current data structure
    def pop(self):
        # pop from front of stack, FIFO
        return self.items.pop()

    # returns the size of the current data structure (the number of elements)
    def size(self):
        # return length of list as stack size
        return len(self.items)

    # returns a boolean value that indicates if the element item is contained in the current data structure
    def __contains__(self, item):
        # return item in items
        return item in self.items


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