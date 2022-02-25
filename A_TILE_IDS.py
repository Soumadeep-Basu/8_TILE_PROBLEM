#IDS ALGO FOR SOLVING THE A-TILE PROBLEM
import sys


#Store the Initial and Final States in a Variable
global Initial
global Final

#Initialize the matrices to the given Dimensions
Initial = [[0 for j in range(3)] for i in range(3)]
Final = [[0 for j in range(3)] for i in range(3)]


#Here we are defining the initial tile state, this can also be taken as an input from the user
A_TILE_INIT_BOARD = Initial


#Here we are defining the Final tile state, this can also be taken as an input from the user
A_TILE_GOAL_STATE = Final


#Definition of max depth, the visited list and the sequence list
global DEPTH
global Visited
global Sequence




#Definition of variable to keep count of all possible states, this could be different from all the states that is visited
global possible_states
possible_states = 0
# This is important as if the goal state is reached, the total number of states possible or enqueued might not be equal to the number of states that have been visited



#This list keeps track of the states that have been enqueued
Visited = []
#This list keeps track of the states that belong in the path to the goal state
Sequence = []




#Definition of the IDS search function
def Find_Path(State, k, Final = A_TILE_GOAL_STATE):

    #set max depth
    global DEPTH
    Max_Depth = DEPTH


    #Set the scope for all the global variables
    global Visited
    global Sequence
    global possible_states

    #Code to obtain index of * , at every state
    x, y = 0, 0
    

    #Find the position of * in each state
    for i in range(len(State)):
        for j in range(len(State[0])):
            if State[i][j] == "*":
                x,y = i,j    


    # Find the boundaries of the matrix to get admissible states
    row_len = len(State)
    col_len = len(State[0])
    

    #Initialize a variale to get the next states
    temp =[[0 for j in range(len(State[0]))] for i in range(len(State))]

  
    # Stopping Conditions for Recurssion
    if State == Final or k > Max_Depth:
        #checking if the state reached is the final state
        if State == Final:
            print()
            print("****--------------------------------****")
            print(" GOAL STATE REACHED")
            print()
            print("Report for the following execution of the exhaustive search : ")
            print()
            print(f" Number of nodes in path (Number of Nodes that have been expanded) : {len(Sequence) + 1}")
            print()
            print(" All the possible nodes (Enqueued) :",possible_states)
            print()
            print("========")
            print()
            print("Path : ")
            print()

            #Adding Final state to the path
            Sequence.append(State)

            

            for i in Sequence:
                show(i)
            exit()
        else:
            
            return State
 
    else:

        for i in range(len(State)):
            for j in range(len(State[0])):
                temp[i][j] = State[i][j] 
        #Adding the state to the visited and path sequence
        Visited.append(State)
        Sequence.append(State)
        

        #check for the number of possible states that can be enqued
        if(x != row_len -1):
            possible_states+=1

        if(y != col_len -1):
            possible_states+=1

        if(x > 0):
            possible_states+=1

        if(y > 0):
            possible_states+=1


       
        #Move left        
        if (y > 0):
            
            temp[x][y], temp[x][y-1] = temp[x][y-1], temp[x][y]
            
               
            S = Find_Path(temp,  k+1)
            
            
            
            temp[x][y], temp[x][y-1] = temp[x][y-1], temp[x][y]


    
        # Move right           
        if(y != col_len - 1):
            
            temp[x][y], temp[x][y+1] = temp[x][y+1], temp[x][y]
            
            
            S = Find_Path(temp,  k+1)
            
            
            
            temp[x][y], temp[x][y+1] = temp[x][y+1], temp[x][y]



        #Move up
        if (x > 0):

                
            temp[x][y],temp[x-1][y] = temp[x-1][y], temp[x][y]
            
            
            S = Find_Path(temp,  k+1)
            
            
            
            temp[x][y],temp[x-1][y] = temp[x-1][y], temp[x][y]



        
        #Move Down
        if(x != row_len -1):
            
            temp[x][y], temp[x+1][y] = temp[x+1][y], temp[x][y]
            
            
            S = Find_Path(temp,  k+1)
            
            
                  

            temp[x][y], temp[x+1][y] = temp[x+1][y], temp[x][y]



        #Remove unwanted states from the path sequence. The path Sequence will be empty if the node is not reached. 
        Sequence.pop()


#Function that gets Input Matrix from input file
def processinp(fn):

    with open(fn,'r') as f:
        data=f.readline()
    grid=[]
    data=data.split()
    cnt=0
    for i in range(3):
        x=[]
        for j in range(3):
            x.append(data[0][cnt])
            cnt+=1
        grid.append(x)
    return grid

        
#Definition of the Function that displays the states that lead to the goal in a presentable manner
def show(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end= " ")
        print()
        
    print("=========")
              

#Definition for the main Function that controls the flow of information
def main():
    #Set the scope for all the global variables that were defined
    global Initial
    global Final
    

    #Define Final State
    end = [[1,2,3],[8,"*",4],[7,6,5]]

    for i in range(3):
        for j in range(3):
            Final[i][j] = end[i][j]
    #Code that gets input matrix from the input file mentioned in the directory

    fname = sys.argv[1]

    input_matrix = processinp(fname)

    for i in range(3):
        for j in range(3):
            if input_matrix[i][j] == "*":
                Initial[i][j] = input_matrix[i][j]
            else:
                Initial[i][j] =  int(input_matrix[i][j])  
    
    #Result of the DFS method that has been called

    for i in range(15) :
        global DEPTH
        DEPTH = i


        #clear out visited so you can start a fresh Iteration
        global Visited
        del Visited[:]

        #clear out possible states
        global possible_states
        possible_states = 0
        


        res = Find_Path(A_TILE_INIT_BOARD,  0)

        print("Depth : " ,DEPTH)
        print()
        #Indicate that there was no solution found.
        print("No solution found by the DFS algorithm and the proposed maximum depth")
        print()
        print("Report for the following execution of the exhaustive search : ")
        print()
        print(f" Number of visited nodes that are enqueued : {possible_states}")
        print()






if __name__ == "__main__":
    main()










