#A STAR ALGO FOR SOLVING A-TILE

import sys

#Define Variables to store Number of nodes Possible
global State_Tracker
State_Tracker = 0


#Store the Value of the Huristic Choosen over here
global huristic_choosen


#Store Visited list, To make sure same states are not visited Again
global Frontier

# Initialize visited Node
Frontier = []

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
        self.depth = d
        self.parent = "NONE"
        


#Show function that lets us print a matrix in a presentable manner
def show(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end= " ")
        print()
        
    print("=========")



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


#Definition of Function that Finds the path based on Huristics to given optimal possible path
def FindPath(Node,final = A_TILE_GOAL_STATE):
    global Frontier
    global State_Tracker


    while len(Frontier) > 0:

        #To store the values of the list elements in each class
        List_VAl = []
        for N in Frontier:
            List_VAl.append(N.val)


        #list that will have all the cost metrics per state
        costs = []
        
        global huristic_choosen
        #check what Huristic was choosen
        if (huristic_choosen == "H1"):
            costs = Calc_Huristic1(List_VAl)
        else:
            costs = Calc_Huristic2(List_VAl)

        
        #Add Depth to each of the cost functions that is compute f(n) + g(n): 

        for i in range(len(costs)):
            costs[i] = costs[i] + Frontier[i].depth

        #find Min cost
        x = min(costs)

        # Get the index corresponding to that move
        x1 = costs.index(x)
            


        
        # Get that possible next state
        Current_Node = Frontier.pop(x1)

        #Initialize Temp array so that given a state, you can find all possible next states that are admissible through manipulation
        temp =[[0 for j in range(len(A_TILE_GOAL_STATE[0]))] for i in range(len(A_TILE_GOAL_STATE))]

        #Current State 
        state = Current_Node.val

        #All possible next states stored here
        possible_states = []

        row_len = len(A_TILE_GOAL_STATE)
        col_len = len(A_TILE_GOAL_STATE[0])
        

        #Get the Value of "*" in the given state
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] == "*":
                    x,y = i,j  

        #Set the Value of Temp to the state that you are currently in
        for i in range(len(state)):
            for j in range(len(state[0])):
                temp[i][j] = state[i][j] 

        #Move left        
        if (y > 0):               
            temp[x][y], temp[x][y-1] = temp[x][y-1], temp[x][y]
                
                
            d = [[0 for i in range(len(temp[i]))] for j in range(len(temp))]
            for i in range(len(temp)):
                for j in range(len(temp[0])):
                    d[i][j] = temp[i][j]
                    
            Node1 = Tree(d, Current_Node.depth + 1)
            Node1.parent = Current_Node
            possible_states.append(Node1)
                
                
            temp[x][y], temp[x][y-1] = temp[x][y-1], temp[x][y]

        #Move right
        if(y != col_len - 1):

            temp[x][y], temp[x][y+1] = temp[x][y+1], temp[x][y]
            
            
            b = [[0 for i in range(len(temp[i]))] for j in range(len(temp))]
            for i in range(len(temp)):
                for j in range(len(temp[0])):
                    b[i][j] = temp[i][j] 
            Node2 = Tree(b, Current_Node.depth + 1)
            Node2.parent = Current_Node
            possible_states.append(Node2)
            
            
            temp[x][y], temp[x][y+1] = temp[x][y+1], temp[x][y]

            
        #Move up
        if (x > 0):             
            temp[x][y],temp[x-1][y] = temp[x-1][y], temp[x][y]
            
            
            c = [[0 for i in range(len(temp[i]))] for j in range(len(temp))]
            for i in range(len(temp)):
                for j in range(len(temp[0])):
                    c[i][j] = temp[i][j] 
            Node3 = Tree(c, Current_Node.depth + 1)
            Node3.parent = Current_Node
            possible_states.append(Node3)
            
            
            temp[x][y],temp[x-1][y] = temp[x-1][y], temp[x][y]

        #Move down
        if(x != row_len -1):
            temp[x][y], temp[x+1][y] = temp[x+1][y], temp[x][y]
            
            

            a = [[0 for i in range(len(temp[i]))] for j in range(len(temp))]
            for i in range(len(temp)):
                for j in range(len(temp[0])):
                    a[i][j] = temp[i][j] 
            Node4 = Tree(a, Current_Node.depth + 1)
            Node4.parent = Current_Node
            possible_states.append(Node4)

            temp[x][y], temp[x+1][y] = temp[x+1][y], temp[x][y]


            
        #Increase the State_Tracker, to depict all the states that have been enqueued:
        #check for the number of possible states that can be enqued
        if(x != row_len -1):
            State_Tracker+= 1

        if(y != col_len -1):
            State_Tracker+= 1

        if(x > 0):
            State_Tracker+= 1

        if(y > 0):
            State_Tracker+= 1


        
        
        #Stopping Conditions for Reccursion
        if(Current_Node.depth >= 15):
            pass
        #Check if you reached the goal Node
        elif(Current_Node.val == final):
            print(" Goal State Reached !!")
            return Current_Node
        else:

            #Append New frontier Nodes
            for i in possible_states:
                if(Frontier.count(i) == 0 ):
                    #Add new states to Frontier
                    Frontier.append(i)
            


#Define Main Funtion That controls the Process Flow
def main():
    #Set the Scope for all the global variables that were defined
    global huristic_choosen
    global Initial
    global Final
    global Frontier

    



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

    #Code to Enbale the User to Choose the Huristic that Has to be Performed for the Particular Problem:
    huristic_choosen = sys.argv[2]

    #Initialize Tree 
    Node = Tree(A_TILE_INIT_BOARD, 0)

    #Add the Node to visited :
    Frontier.append(Node)
    

    #Get result from the A-Star Algo
    Node = FindPath(Node)

    #Variable that Stores the depth at which solution is found
    depth_node = 0



    
    #Print Results
    if(Node == None):
        print("No solution Found at a Maximum depth of 15")
        print()
        print("Total number of nodes encountered : ", State_Tracker)
    else:
        depth_node = Node.depth
        print()
        print()
        print("Solution Found")
        print()
        print("==========================")
        res = []
        while(Node!= "NONE"):
            res.append(Node.val)
            Node = Node.parent
        
        res.reverse()
        for i in res:
            show(i)
            



        #Print out the Statistics of the Particular Instance that Has Just Run

        print()
        print(" Report on the Depth or Length of the Path (Visited) and the Number of nodes that were expanded or enqueued")
        print("----")
        print("depth of the Tree or number of moves required, enqued: ", depth_node)
        print("----")
        print("Total Number of States that are Possible or in other words total length of frontier : ", State_Tracker)
        print("----")

 

if __name__ == "__main__":
    main()


