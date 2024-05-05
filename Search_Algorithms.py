from State import State
from queue import PriorityQueue
from queue import Queue
from queue import LifoQueue

#This is calculate for Space

l1 = []
def SpaceOfBFS():
    return max(l1) #get max value of l1 list which is worst case

l2=[]    
def SpaceOfDFS():
    return max(l2) #get max value of l2 list which is worst case

l3=[]
def SpaceOfGr():
    return max(l3) #get max value of l3 list which is worst case

l4=[]
def SpaceOfA():
    return max(l4) #get max value of l4 list which is worst case

#Breadth-first Search
def BFS(given_state , n):
    root = State(given_state, None, None, 0, 0)
    if root.test():
        return root.solution()
    frontier = Queue()
    frontier.put(root) # root palces in frontier 
    explored = []
    
    while not(frontier.empty()):
        l = frontier.qsize()  # Here I take queue size
        l1.append(l)
        current_node = frontier.get()
        explored.append(current_node.state) # store in explored 
        
        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    return

#Depth-first Search with limited depth


def DFS(given_state , n): 
    root = State(given_state, None, None, 0, 0)
    if root.test():
        return root.solution()
    frontier = LifoQueue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        l = frontier.qsize()  # Here I take queue size
        l2.append(l)

        current_node = frontier.get()
        max_depth = current_node.depth #current depth
        explored.append(current_node.state)
        
        if max_depth == 30:
            continue #go to the next branch

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    return (("Couldn't find solution in the limited depth."), len(explored))
        
    

def Greedy(given_state , n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    #root.evaluation()
    evaluation = root.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.
    frontier.put((evaluation[0], counter, root)) #based on greedy evaluation

    while not frontier.empty():
        l = frontier.qsize()  # Here I take queue size
        l3.append(l)
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        
        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                evaluation = child.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.
                frontier.put((evaluation[0], counter, child)) #based on greedy evaluation
    return

def AStar_search(given_state , n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    evaluation = root.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.
    frontier.put((evaluation[1], counter, root)) #based on A* evaluation

    while not frontier.empty():
        l = frontier.qsize()
        l4.append(l)
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        
        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                evaluation = child.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.
                frontier.put((evaluation[1], counter, child)) #based on A* evaluation
    return
