import queue as Q


# where jugOne is an integer for the amount the first jug can fill,
# jugTwo is an integer for the amount the second jug can fill,
# goal is goal amount to be reached for one just to have
def twoJugProblemBFS(jugOne, jugTwo, goal):
    # if the goal state is more than the possible jar amount totals, an invalid problem is given.
    # therefore just return that it is a failure, as it cannot be computed
    if goal > jugOne + jugTwo:
        print("Fails, an invald problem provided.")
        return

    # set the initial state in the queue with two empty jugs
    queue = [(0, 0)]
    # keep visited node path, with initial node within
    visited = set((0, 0))

    # as long as the queue of states is not empty, loop
    while len(queue) > 0:
        # pop the values for the jugOne and jugTwo from the current state
        jugOneState, jugTwoState = queue.pop(0)
        print("We are at ",jugOneState,", ",jugTwoState)
        # the goal is when only 2 gallons (in this case) is filled in jugOne (i.e. the 4G jug), once this is found, exit
        if jugOneState == goal:
            print("You have reached the goal!")
            return
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

        # loop through states
        for state in states:
            # if state has already been visited, do not add to queue
            if state in visited:
                continue
            # add state to queue and visited
            queue.append(state)
            visited.add(state)
            # print queue to see progress
            print(queue)

    return


def twoJugProblemAStar(jugOne, jugTwo, goal):
    priorityQueue = Q.PriorityQueue()
    visitedStates = []
    # enqueue initial state
    priorityQueue.put((0, (0, 0)))
    visitedStates.append((0, 0))

    while priorityQueue.qsize() > 0:
        # pop the values for the jugOne and jugTwo from the current state
        jugOneState, jugTwoState = priorityQueue.get(0)[1]
        print("We are at ",jugOneState,", ",jugTwoState)
        # the goal is when only 2 gallons (in this case) is filled in jugOne (i.e. the 4G jug), once this is found, exit
        if jugOneState == goal:
            print("You have reached the goal!")
            return
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

        # loop through states
        for state in states:
            # if state has already been visited, do not add to queue
            if state in visitedStates:
                continue
            priorityQueue.put((heuristic(state[0], state[1], goal), state))
            visitedStates.append(state)
            # print queue to see progress
            print(priorityQueue.queue)
    return


def heuristic(jugOne, jugTwo, goal):
    # g(c) will always be 1.
    return abs(jugOne - goal) + abs(jugTwo - goal)


# run main, select the appropriate method to run either BFS solution or heuristic solution
if __name__ == "__main__":
    print("BFS: ")
    twoJugProblemBFS(4, 3, 2)
    print("\nA* with heuristic: ")
    twoJugProblemAStar(4, 3, 2)
