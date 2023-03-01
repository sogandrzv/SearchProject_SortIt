from State import State
from Solution import Solution
from Problem import Problem


class Search:
    @staticmethod
    def bfs(prb: Problem) -> Solution:  # this method get a first state of Problem and do bfs for find solution if no
        # solution is find return None else return the solution
        queue = []
        state = prb.initState
        queue.append(state)
        explored = []
        while len(queue) > 0:
            state = queue.pop(0)
            explored.append(state.__hash__())
            neighbors = prb.successor(state)
            for c in neighbors:
                if not explored.__contains__(c.__hash__()):
                    if prb.is_goal(state):
                        return Solution(state,prb)
                    queue.append(c)
        return None
