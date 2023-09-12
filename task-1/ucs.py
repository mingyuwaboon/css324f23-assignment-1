from heapq import heappush, heappop, heapify
from utils import create_node


def uniform_cost_tree_search(problem):
    initial_node = create_node(problem.initial_state(), None,
                               "", 0, 0)
    frontier = [(0, initial_node)]
    n_visits = 0
    while True:
        if not frontier:
            return (None, n_visits)
        else:
            n_visits += 1
            _, node = heappop(frontier)
            state, _, _, path_cost, depth = node
            if problem.is_goal(state):
                return (node, n_visits)
            else:
                for succ, cost in problem.successors(state):
                    child_cost = path_cost + cost
                    child = create_node(succ, node, "", child_cost,
                                        depth + 1)
                    heappush(frontier, (child_cost, child))


def index(f, s):
    return next((i for i, x in enumerate(f) if x[1][0] == s), -1)


def uniform_cost_graph_search(problem):
    initial_node = create_node(problem.initial_state(), None,
                               "", 0, 0)
    frontier = [(0, initial_node)]
    explored = set()
    n_visits = 0
    while True:
        if not frontier:
            return (None, n_visits)
        # search next path (seccesor function)
        else:
            n_visits += 1
            _, node = heappop(frontier)
            state, _, _, path_cost, depth = node
            explored.add(state)
            # check goal state
            if problem.is_goal(state):
                return (node, n_visits)
            # not goal state, find next path
            else:
                for succ, cost in problem.successors(state):
                    child_cost = path_cost + cost 
                    child = create_node(succ, node, "", child_cost,
                                        depth + 1)
                    if succ not in explored:
                        idx = index(frontier, succ)
                        #if not met in explored, push in heap (meaning: find new path)
                        if idx < 0:
                            heappush(frontier, (child_cost, child))
                        #if met in explored, if old path_cost > new path_cost, update new path_cost instead of old path_cost
                        else:
                            _, existing = frontier[idx]
                            if existing[3] > child_cost:
                                frontier[idx] = (child_cost, child)
                                heapify(frontier)
