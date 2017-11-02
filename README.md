# Water Jug Problem (Subject 8) 
## Students: Arthur Leung (6766207) and Christine Kandalaft (7216942)

Subject S8: You are given two jugs, a 4-gallon one and a 3-gallon one, a pump which has unlimited water which you can use to fill the jugs, and the ground on which water may be poured. Neither jug has any measuring markings on it. The objective is to get exactly 2 gallons of water in the 4-gallon jug. Use blind search and informed search. 

Assumption: Each move has a cost of 1 (i.e. arc length).

For this blind search, we have used BFS, which does not gives the optimal path (as our move costs are the same as the arc length), but explores in 'breadth' (so it visits extra states).

For informed search, we have used A star with heuristic h(s) where s is a state (x,y):
h(s) = |x-G| + |y-G| ; such that x,y are jugOne (4G) and jugTwo (3G) respectively and G is the goal value (2 gallons)

The heuristic is relaxing the condition of needing exactly 2 gallons in the 4 gallon jug as the goal state. Instead, we will try to reach 2 gallons of total water in *either* of the two jugs (4 gallon and 3 gallon jugs). This can be seen in h(s) as we minimize h(s) as the distance between both x (the 4 gallon jug) and y (the 3 gallon jug) with the goal state (2 gallon) respectively.

This is admissible and therefore optimal for A star as the real cost c(s) to the goal is always the sum of arc lengths, while the estimated cost is the distance is the calculated distance h(s). 

For the final move, the actual arc length cost to goal is 1, while the estimated cost h(s) is 0.

h(s) <= c(s)
_____________________________________________________________________________________________________________________________________________

Output for jugs of 4 gallons and 3 gallons, with a goal state of 2 gallons in the 4 gallon jug:

BFS: 
We are at  0 , 0
[(0, 3)]
[(0, 3), (0, 0)]
[(0, 3), (0, 0), (4, 0)]
We are at  0 , 3
[(0, 0), (4, 0), (3, 0)]
[(0, 0), (4, 0), (3, 0), (4, 3)]
We are at  0 , 0
We are at  4 , 0
[(3, 0), (4, 3), (1, 3)]
We are at  3 , 0
[(4, 3), (1, 3), (3, 3)]
We are at  4 , 3
We are at  1 , 3
[(3, 3), (1, 0)]
We are at  3 , 3
[(1, 0), (4, 2)]
We are at  1 , 0
[(4, 2), (0, 1)]
We are at  4 , 2
[(0, 1), (0, 2)]
We are at  0 , 1
[(0, 2), (4, 1)]
We are at  0 , 2
[(4, 1), (2, 0)]
We are at  4 , 1
[(2, 0), (2, 3)]
We are at  2 , 0
You have reached the goal!

A* with heuristic: 
We are at  0 , 0
[(3, (0, 3))]
[(3, (0, 3)), (4, (4, 0))]
We are at  0 , 3
[(3, (3, 0)), (4, (4, 0))]
[(3, (3, 0)), (4, (4, 0)), (3, (4, 3))]
We are at  3 , 0
[(2, (3, 3)), (4, (4, 0)), (3, (4, 3))]
We are at  3 , 3
[(2, (4, 2)), (4, (4, 0)), (3, (4, 3))]
We are at  4 , 2
[(2, (0, 2)), (4, (4, 0)), (3, (4, 3))]
We are at  0 , 2
[(2, (2, 0)), (4, (4, 0)), (3, (4, 3))]
We are at  2 , 0
You have reached the goal!
