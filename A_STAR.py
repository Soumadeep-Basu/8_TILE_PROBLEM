#Define Variables to store Number of nodes Possible
global State_Tracker
State_Tracker = 0

#Here we are defining the initial tile state, this can also be taken as an input from the user
A_TILE_INIT_BOARD = [[8,1,3],[7,2,4],["*",6,5]]




#Here we are defining the Final tile state, this can also be taken as an input from the user
A_TILE_GOAL_STATE = [[1,2,3],[8,4, "*"],[7,6,5]]






#Define the function that calculates the Manhattan Distance between the tiles in the Initial and Final State
def Calc_Huristic1(States):
  
    Huristic_Cost = []

    for M in States:
        target = {}
        state = {}

        sum = 0
        
        #Create a dictionary that contains, index and value pairs for easy computation. 
        for i in range(len(M)):
            for j in range(len(M[0])):
                
                target[A_TILE_GOAL_STATE[i][j]] = [i,j]
                state[M[i][j]] = [i,j]
        # Calculate the Distance between the tiles in the Final and Initial Position
        for i in range(1,9):

            x = target[i]
            y = state[i]

            sum = sum + abs(x[0]-y[0]) + abs(x[1]-y[1])
        #Sum is for each state
        Huristic_Cost.append(sum)
    
    #return an array, that gives us huristic of each state, given an array of states.
    return Huristic_Cost

#Define the Function that calculates the number of Mismatched
def Calc_Huristic2(States):

    Huristic_Cost = []

    for M in States:

        sum = 0
        
        #Calculate the number of mismatched tiles in each state
        for i in range(len(M)):
            for j in range(len(M[0])):

                if(M[i][j]!=A_TILE_GOAL_STATE[i][j] and M[i][j]!="*"):
                    sum+=1
            
        #Sum is for each state
        Huristic_Cost.append(sum)
    #return an array, that gives us huristic of each state, given an array of states.
    return Huristic_Cost





#Definition of Tree Structure that is used to store the states
class Tree:
    def __init__(self,State, d):
        self.val = State
        self.next_state = 0
        self.depth = d


#Show function that lets us print a matrix in a presentable manner
def show(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end= " ")
        print()
        
    print("=========")



#Definition of Function that Finds the path based on Huristics to given optimal possible path
def FindPath(Node,final = A_TILE_GOAL_STATE):
    #Initialize Temp array so that given a state, you can find all possible next states that are admissible through manipulation
    temp =[[0 for j in range(len(A_TILE_GOAL_STATE[0]))] for i in range(len(A_TILE_GOAL_STATE))]

    #Current State 
    state = Node.val

    #All possible next states stored here
    possible_states = []

    row_len = len(A_TILE_GOAL_STATE)
    col_len = len(A_TILE_GOAL_STATE[0])
    

    #Set the Value of Temp to the state that you are currently in
    for i in range(len(state)):
        for j in range(len(state[0])):
            temp[i][j] = state[i][j] 

    #Stopping Conditions for Reccursion
    if(Node.depth > 10):
        print("Max Depth Reached, solution not Found.")
        Node.next_state = "NONE"
        return Node
    elif(Node.val == final):
        print(" Goal State Reached !!")
        Node.next_state = "NONE"
        return Node
    else:

        #Get the Value of "*" in the given state
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] == "*":
                    x,y = i,j    
         
        #Move down
        if(x != row_len -1):
            temp[x][y], temp[x+1][y] = temp[x+1][y], temp[x][y]
            
            

            a = [[0 for i in range(len(temp[i]))] for j in range(len(temp))]
            for i in range(len(temp)):
                for j in range(len(temp[0])):
                    a[i][j] = temp[i][j] 
            possible_states.append(a)

            temp[x][y], temp[x+1][y] = temp[x+1][y], temp[x][y]

        #Move right
        if(y != col_len - 1):

            temp[x][y], temp[x][y+1] = temp[x][y+1], temp[x][y]
            
            
            b = [[0 for i in range(len(temp[i]))] for j in range(len(temp))]
            for i in range(len(temp)):
                for j in range(len(temp[0])):
                    b[i][j] = temp[i][j] 
            possible_states.append(b)
            
            
            temp[x][y], temp[x][y+1] = temp[x][y+1], temp[x][y]

            
        #Move up
        if (x > 0):             
            temp[x][y],temp[x-1][y] = temp[x-1][y], temp[x][y]
            
            
            c = [[0 for i in range(len(temp[i]))] for j in range(len(temp))]
            for i in range(len(temp)):
                for j in range(len(temp[0])):
                    c[i][j] = temp[i][j] 
            possible_states.append(c)
            
            
            temp[x][y],temp[x-1][y] = temp[x-1][y], temp[x][y]

            
  
                        
        #Move left        
        if (y > 0):               
            temp[x][y], temp[x][y-1] = temp[x][y-1], temp[x][y]
            
            
            d = [[0 for i in range(len(temp[i]))] for j in range(len(temp))]
            for i in range(len(temp)):
                for j in range(len(temp[0])):
                    d[i][j] = temp[i][j] 
            possible_states.append(d)
            
            
            temp[x][y], temp[x][y-1] = temp[x][y-1], temp[x][y]

        
        #Increase the State_Tracker, to depict all the states that have been enqueued:
        global State_Tracker

        State_Tracker+= len(possible_states)


        #list that will have all the cost metrics per state
        costs = []

        costs = Calc_Huristic1(possible_states)

        
        #move that costs the least
        x = min(costs)
        
        # Get the index corresponding to that move
        x1 = costs.index(x)
        
        # Get that possible next state
        next_s = possible_states[x1]

        
        # Initialize tree with value as the next state
        Next_Node = Tree(next_s,Node.depth+1)
        
        #Connect the states, so you can obtain it when you are retrieving the path
        Node.next_state = Next_Node
        

        #Recursive Algorithm
        FindPath(Next_Node)


        return Node 




#Initialize Tree 
Node = Tree(A_TILE_INIT_BOARD, 0)

Node = FindPath(Node)




#Print the Path , (if it exits), from root to leaf
while(Node.next_state!=None):
    show(Node.val)
    if Node.next_state!="NONE":
        Node = Node.next_state
    else:
        break


#Print out the Statistics of the Particular Instance that Has Just Run

print(" Report on the Depth or Length of the Path (Visited) and the Number of nodes that were expanded or enqueued")
print("----")
print("depth of the Tree or number of moves required: ", Node.depth)
print("----")
print("Total Number of States that are Possible : ", State_Tracker)
print("----")
print("No of States that are enqued : " , Node.depth + 1)


    

     











