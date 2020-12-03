# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    from game import Directions, Actions

    pacmanStack = util.Stack()
    positionList = []
    positionListFinal = {}
    # Start
    
    currentState = problem.getStartState()
    FoundGoal = problem.isGoalState(currentState)
    pacmanStack.push(currentState)
    while(FoundGoal != True):
        currentState = pacmanStack.pop()
        if(problem.isGoalState(currentState)):
            FoundGoal = True
            break
        positionList.append(currentState)
        succ = problem.getSuccessors(currentState)

        for i in range(0,len(succ)):
            if(not (succ[i][0] in positionList)): 
                pacmanStack.push(succ[i][0]) 
                positionListFinal[succ[i][0]] = (currentState,succ[i][1])


    #getpath
    endList = []
 
    currentState = positionListFinal[currentState]
    while(currentState[0] != problem.getStartState()):
        endList.insert(0,currentState[1])
        currentState = positionListFinal[currentState[0]]

    endList.insert(0,currentState[1])
    return endList

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions, Actions

    pacmanQueue = util.Queue()
    positionList = []
    positionListFinal = {}
    
    # Start
    
    currentState = problem.getStartState()
    FoundGoal = problem.isGoalState(currentState)
    pacmanQueue.push(currentState)
    while(FoundGoal != True):
        currentState = pacmanQueue.pop()
        if(problem.isGoalState(currentState)):
            FoundGoal = True
            break
        positionList.append(currentState)
        succ = problem.getSuccessors(currentState)
        for i in range(0,len(succ)):
            successor = succ[i][0]
            if(not (successor in positionList)): 
                pacmanQueue.push(successor) 
                positionList.append(successor)
                positionListFinal[successor] = (currentState,succ[i][1])

    #getpath
    endList = []

    currentState = positionListFinal[currentState]
    while(currentState[0] != problem.getStartState()):
        endList.insert(0,currentState[1])
        currentState = positionListFinal[currentState[0]]

    endList.insert(0,currentState[1])
    return endList


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    from game import Directions, Actions
    pacmanPriorityQueue = util.PriorityQueue()
    positionList = {}
    positionListFinal = {}

    currentState = (problem.getStartState(),[])
    FoundGoal = problem.isGoalState(currentState[0])

    pacmanPriorityQueue.push(currentState,0)
    positionList[currentState[0]] = 0

    while(FoundGoal != True):
        currentState = pacmanPriorityQueue.pop()
        if(problem.isGoalState(currentState[0])):
            FoundGoal = True
            break
        succ = problem.getSuccessors(currentState[0])
        for i in range(0,len(succ)):
            successor = succ[i][0]
            action = succ[i][1]
            totalPath = currentState[1] + [action]
            totalPathCost = problem.getCostOfActions(totalPath)
            if(not (successor in positionList)): 
                pacmanPriorityQueue.push((successor,totalPath), totalPathCost) 
                positionList[successor] =  totalPathCost
                positionListFinal[successor] = (currentState[0],action)
            elif(totalPathCost < positionList[successor]):
                pacmanPriorityQueue.push((successor,totalPath), totalPathCost) 
                positionList[successor] = totalPathCost
                positionListFinal[successor] = (currentState[0], action)

    endList = []
    currentState = positionListFinal[currentState[0]]
    while(currentState[0] != problem.getStartState()):
        endList.insert(0,currentState[1])
        currentState = positionListFinal[currentState[0]]

    endList.insert(0,currentState[1])

    return endList
    



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"


    from game import Directions, Actions
    pacmanPriorityQueueWithFunction = util.PriorityQueueWithFunction(lambda x: x[2] + heuristic(x[0],problem))
    positionList = {}
    positionListFinal = {}

    currentState = (problem.getStartState(),[],0)
    FoundGoal = problem.isGoalState(currentState[0])

    pacmanPriorityQueueWithFunction.push(currentState)
    positionList[currentState[0]] = 0

    while(FoundGoal != True):
        currentState = pacmanPriorityQueueWithFunction.pop()
        if(problem.isGoalState(currentState[0])):
            FoundGoal = True
            break
        succ = problem.getSuccessors(currentState[0])
        for i in range(0,len(succ)):
            successor = succ[i][0]
            action = succ[i][1]
            totalPath = currentState[1] + [action]
            totalPathCost = heuristic(successor,problem) + problem.getCostOfActions(totalPath)
            if(not (successor in positionList)): 
                pacmanPriorityQueueWithFunction.push((succ[i][0],totalPath,totalPathCost)) 
                positionListFinal[successor] = (currentState[0],action)
                positionList[successor] = totalPathCost
            elif(totalPathCost < positionList[successor]):
                pacmanPriorityQueueWithFunction.push((successor,totalPath,totalPathCost)) 
                positionList[successor] = totalPathCost
                positionListFinal[successor] = (currentState[0], action)
    
    endList = []
    currentState = positionListFinal[currentState[0]]
    while(currentState[0] != problem.getStartState()):
        endList.insert(0,currentState[1])
        currentState = positionListFinal[currentState[0]]

    endList.insert(0,currentState[1])

    return endList
    

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
