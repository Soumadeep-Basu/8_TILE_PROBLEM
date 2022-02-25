# ARTIFICIAL INTELLIGENCE SOLUTION TO THE A_TILE PROBLEM

The purpose of this document is to serve as a guide and report for the tasks given in HW1

***RUNNING THE CODE***

Note that for this particular HW, the output sequence is always fixed, that is 1238*4765, the input on the other hand is obtained fron the input file, input.txt. 
If the user wishes to change the input, they can simple paste their start sequence here. 

Note that the sequence should be a single string not separated by any spaces. (No trailing spaces either)
Further, the blank tile is denoted as *

Examples of valid inputs : 

1. 364*12875

2. 12384*765


Once the user has configured the Input file, here are some other pointers to make sure of: 

1. All the files, A_TILE_ASTAR / A_TILE_DFS / A_TILE_IDS / Driver / input are in the same level of a folder

2. You are able to run command line arguments


***COMMMAND TO RUN THE CODE***

python3 Driver.py <ALGO_NAME> <INPUT_FILE>


<ALGO_NAME> : DFS / IDS / ASTAR1 / ASTAR2

> Here, ASTAR1 is for the Manhattan Distance and ASTAR2 is for the Misplaced Tile Hueristic. 

> The input file should be the one that holds the input. If the user changes it here, they must also change it in the main


And thats it ! We now have a program that can solve a given configuraton of an A TILE puzzle using the DFS, IDS and the A-STAR algorithm!

:)


***GENERAL OBSERVATIONS ABOUT THE DFS AND THE IDS ALGORITHMS***

1. To start of with, DFS is not complete. Since there is no track of previous nodes visited as well, sometimes you may go into a    loop. Thus, a solution is not guaranteed. Further, even if you do get a solution almost certainly it is not the optimal solution. 

2. IDS is however, complete. If there is a solution at a depth of or before the depth of 15, the IDS will find it. This algorithm is slow though. Plus the overhead gives a lot of added run time. 

A common finding for both IDS and DFS is that the search tree depends greatly on the order of the moves that you have defined. If someone set up the possible moves as [Up, Right, Left, Down], their search tree would greatly vary frorm a person who is perhaps defining another order. This means that the same solution may or may not be found at a given depth based on the order of the possible moves defined.


***ASTAR HEURISTIC COMPARISON***

Lastly, we can compare the two different Heuristics that are being used.

1. Manhattan Distance  ( H1 ): 

This is the First Heuristic that we are using. Here, at every node we compute the absolute distance that needs to be traversed from the given point in the state to the corresponding point in the Goal. 

Ie : abs(X_Target - X_Goal) + abs(Y_Target - Y_Goal)

This is summed over tiles 1 through 9. The value is not technically bounded, and can cross the value of 9

2. Misplaced Tiles (H2 ) : 

This is the Second Heuristic that we are using. Here we simple tally the number of misplaced tiles in a given state vs the goal state. This value is bouded by the value of 9. 


> When we are comparing the 2 Heuristics, we can take two trains of thought. Firstly, since the value of the Manhattan Distance is not bounded, we can say that it is greater than that of the Misplaced tiles. This implies H1 > H2. Thus we can say that the Manhattan heuristic is more informed that the Misplaced tiles heuristic and thus is more desired. 

> Secondly, since we are only comapring the number of misplaced tiles , there can be a lot of cases where multiple paths have the same value for the heuristic. Even if the algorithm can converge to a correct solution , this heuristic will slow it down. 

> Thus, for all practical purposes, the Manhattan Distance is a better heuristic than the Eucledian Distance. 



***SAMPLE INPUTS AND OUTPUTS***

> Note that for DFS and IDS, I have used a recursive method. This might slightly hinder running times and make outputs slower by a few seconds. 
> A-Star is done using a stack however. 



INITIAL_STATE : 364*12875

GOAL_STATE : 1238*4765


Using this Input we can look at the result it generates in the the folder tiltled INPUTS_OUTPUTS, for all the algorithms mentioned above. 





