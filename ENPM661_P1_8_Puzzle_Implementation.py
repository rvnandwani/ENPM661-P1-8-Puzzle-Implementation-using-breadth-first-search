import numpy as np
import itertools

def NodeValid(node):            #Function to check whether the solution of the node exists or not
    x=node.ravel()
    x=x.tolist()
    x=[a for a in x if a != 0]
    count=0
    for i in range(0,len(x)):
        y=x[i]
        c=0
        for j in range(i,len(x)):
            if (x[j]<y):
                c=c+1
        count=count+c
    if(count%2==0):
        return ("true")
    else:
        return ("false")
    
def nodecode(J):            #Function to convert 3X3 node to an integer code specific to a particular node
	chain = list(itertools.chain(*J))
	G = ''.join(map(str, chain))
	return G


def BlankTileLocation(Current_Node):            #Function to check the location of '0' in 3X3 matrix
	cp=np.array([1,2])
	for k in range(0,3):
		for l in range(0,3):
			if(Current_Node[k][l]==0):
				cp[0]=k
				cp[1]=l
				break
	return cp

def nodeDisplay(J):            #Function to convert 3X3 node to an 1X3 string
	J=np.transpose(J)
	chain = list(itertools.chain(*J))
	G = ' '.join(map(str, chain))
	return G

def shift(Current_Node,cp):            #Function to swap 0 with another location
	v=BlankTileLocation(Current_Node)
	p=cp+v
	Current_Node[v[0]][v[1]]=Current_Node[p[0]][p[1]]
	Current_Node[p[0]][p[1]]=0
	return Current_Node

def MoveRight(Current_Node):            #Function to move the blank tile right
	c=np.array([0,1])
	cl=BlankTileLocation(Current_Node)
	if(cl[1]==2):
		flag=1
		return flag
	else:
		Ct_Node=shift(Current_Node,c)
		return Ct_Node


def MoveLeft(Current_Node):            #Function to move the blank tile left
	c=np.array([0,-1])
	cl=BlankTileLocation(Current_Node)
	if(cl[1]==0):
		flag=1
		return flag
	else:		
		Ct_Node=shift(Current_Node,c)
		return Ct_Node

def MoveUp(Current_Node):            #Function to move the blank tile up
	c=np.array([-1,0])
	cl=BlankTileLocation(Current_Node)
	if(cl[0]==0):
		flag=1
		return flag
	else:		
		Ct_Node=shift(Current_Node,c)
		return Ct_Node
	

def MoveDown(Current_Node):            #Function to move the blank tile down
	c=np.array([1,0])
	cl=BlankTileLocation(Current_Node)
	if(cl[0]==2):
		flag=1
		return flag
	else:		
		Ct_Node=shift(Current_Node,c)
		return Ct_Node
    
def InputNode():            #Function to take input and generate an nd array - used to generate user entered Initial Node

    print("Enter Row 1 - " , )
    a = [int(x) for x in input().split()]
    print("Enter Row 2 - " , )
    b = [int(x) for x in input().split()]
    print("Enter Row 3 - " , )
    c = [int(x) for x in input().split()]
    return (np.vstack((a,b,c)))


flag=0
print("Enter start array \n")
Node_init=InputNode()
print("Node_init = \n",Node_init)
Node_init_code=nodecode(Node_init)

Node_goal=np.array([[1,2,3],[4,5,6],[7,8,0]])
print("Node_goal = \n",Node_goal)
Node_goal_code=nodecode(Node_goal)

if(NodeValid(Node_init)=="false"):            #Condition in which solution not possible and generating blank txt file
    print("Input matrix has no solution. ")
    
elif(Node_init_code==Node_goal_code):            #Condition to check weather the entered node and goal node is same
    print("Initial node and Goal node is same ")

else:
    i=0
    j=1
    x=np.empty((3,3))
    n=np.empty((3,3))
    z=0
    addr=[]
    nodeset=[]
    nodeset.append(Node_init)            #Initialized set of all possible nodes and appended the initial node
    nodecodeset=[]
    nodecodeset.append(Node_init_code)            #Initialized Set of nodecodes and appending the code of initial array
    goal=0
    

    while 1:

        if(goal==1):
            break
        else:
            x=np.array(nodeset[i])
            n=np.array(MoveUp(x[:]))
            if(np.shape(n)!=(3,3)):
                z=1
            else:
                nc=nodecode(n)
                check=0
                for cku in range(0,len(nodecodeset)):            #Checking whether the newly generated node already present in the nodeset
                    if  (nc==nodecodeset[cku]) :
                        check=1

                if(check!=1):            #If the node is not present, then appending the node in nodeset 
                    nodeset.append(n)
                    nodecodeset.append(nc)
                    a4=[i,j]
                    addr.append(a4)
                    j=j+1
                if  (nc==Node_goal_code):            #Comparing the newly generated node with the goal node
                    goal=1


#------------------ Same is done for the rest of the operations i.e. Down , Left and Right ------------------

        if(goal==1):
            break
        else:
            s=np.array(nodeset[i])
            n=np.array(MoveDown(s[:]))
            
            if(np.shape(n)!=(3,3)):
                z=1
            else:
                check=0
                nc=nodecode(n)
                for ckd in range(0,len(nodecodeset)):
                    if(nc==nodecodeset[ckd]):
                        check=1
                if(check!=1):
                    nodeset.append(n)
                    nodecodeset.append(nc)
                    a1=[i,j]
                    addr.append(a1)
                    j=j+1
                if  (nc==Node_goal_code):
                    goal=1
                    print("Node goal found")
						
			

	
        if(goal==1):
            break
        else:
            t=np.array(nodeset[i])
            n=np.array(MoveLeft(t))
            if(np.shape(n)!=(3,3)):
                z=1
            else:
                check=0
                nc=nodecode(n)
                for ckl in range(0,len(nodecodeset)):
                    if  (nc==nodecodeset[ckl]):
                        check=1
                if(check!=1):
                    nodeset.append(n)
                    nodecodeset.append(nc)
                    a2=[i,j]
                    addr.append(a2)
                    j=j+1
                if  (nc==Node_goal_code):
                    goal=1
					
					

	
        if(goal==1):
            break
        else:
            u=np.array(nodeset[i])	
            n=np.array(MoveRight(u))
            if(np.shape(n)!=(3,3)):
                z=1
            else:
                check=0
                nc=nodecode(n)
                for ckr in range(0,len(nodecodeset)):
                    if  (nc==nodecodeset[ckr]):
                        check=1
					
                if(check!=1):
                    nodeset.append(n)
                    nodecodeset.append(nc)
                    a3=[i,j]
                    addr.append(a3)
                    j=j+1
	
                if  (nc==Node_goal_code):
                    goal=1


        i=i+1
    

    l=len(addr)-1
    seq=[]
    seq.append(addr[l][1])
    seq.append(addr[l][0])

    z=addr[l][0]

    for lm in range(0,len(addr)):            
    	for ln in range(0,len(addr)):
    		if addr[ln][1] == z:
    			seq.append(addr[ln][0])
    			z = addr[ln][0]
    seq=seq[::-1]
    solution=[]            #List of the nodes in order to reach the Goal node
    for ans in seq:
        solution.append(nodeset[ans])

    print("Solution found !! ")

    for fw in range(0,len(solution)):
        print(solution[fw])
    
    
    
    
