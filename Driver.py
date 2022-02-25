import sys
import os

#Import files so you can access them from the driver program
import A_TILE_DFS
import A_TILE_ASTAR
import A_TILE_IDS


#get the inputs from command line
algo = sys.argv[1]
file_name = sys.argv[2]

#Perform the control functions
if(algo == "DFS"):
    os.system(f"python3 A_TILE_DFS.py {file_name}")
if(algo == "IDS"):
    os.system(f"python3 A_TILE_IDS.py {file_name}")
if(algo == "ASTAR1"):
    os.system(f"python3 A_TILE_ASTAR.py {file_name}  H1")
if(algo == "ASTAR2"):
    os.system(f"python3 A_TILE_ASTAR.py {file_name} H2")



