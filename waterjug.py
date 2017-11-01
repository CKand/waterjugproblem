#where jugOne is an integer for the amount the first jug can fill,
#jugTwo is an integer for the amount the second jug can fill, 
#goal is goal amount to be reached for one just to have
def twoJugProblemBFS(jugOne, jugTwo, goal):
     
    #if the goal state is more than the possible jar amount totals, an invalid problem is given.
    #therefore just return that it is a failure, as it cannot be computed         
    if goal > jugOne + jugTwo:
        print("Fails, an invald problem provided.")
        return False;
        
    # set the initial state in the queue with two empty jugs;
    queue = [(0, 0)];
    #keep visited node path, with initail node within
    visited = set((0, 0))

    #as long as the queue of states is not empty, loop
    while len(queue) > 0:
        #pop the values for the jugOne and jugTwo from the current state
        jugOneState, jugTwoState = queue.pop(0);
        #the goal is when only 2 litres is filled between the two jugs, once this is found, exit
        if jugOneState + jugTwoState == goal:
            print("You have reached the goal!")    
            return True;
        #set of possible states from current state     
        states = set()

        # fill jugOne completely    
        states.add((jugOne, jugTwoState))
        #fill jug two completely 
        states.add((jugOneState, jugTwo)) 
        #empty jug one
        states.add((0, jugTwoState))
        #empty jug two
        states.add((jugOneState, 0))
        #fill jug one using jug two
        if jugTwoState < jugOne - jugOneState:
            states.add((min(jugOne, jugTwoState + jugOneState), 0))
        else:
            states.add((min(jugOne, jugTwoState + jugOneState), jugTwoState - (jugOne - jugOneState)))
        #fill jug two using jug one
        if jugOneState + jugTwoState < jugTwo:
            states.add((0,min(jugTwoState + jugOneState, jugTwo)))
        else:
            states.add((jugOneState - (jugTwo - jugTwoState),min(jugTwoState + jugOneState, jugTwo)))
       
        #loop through states
        for state in states:
            #if state has already been visited, do not add to queue
            if state in visited:
                continue;
            #add state to queue and visited 
            queue.append(state)
            visited.add(state);
            #print queue to see progress
            print(queue)
     
    return False;

#run main, select the appropriate method to run either BFS solution or heuristic solution 
if __name__ == "__main__":
    twoJugProblemBFS(4, 3, 2);
