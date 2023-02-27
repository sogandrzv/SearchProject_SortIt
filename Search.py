from Problem import Problem
from Solution import Solution
from State import State


class Search:
    @staticmethod
    def bfs(prb: Problem) -> Solution:  # this method get a first state of Problem and do bfs for find solution if no
        # solution is find return None else return the solution
        queue = []
        state = State(prb, None)
        queue.append(state)
        explored = []
        while len(queue) > 0:
            state = queue.pop(0)
            explored.append(state.__hash__())
            neighbors = state.successor()
            for c in neighbors:
                if not explored.__contains__(c.__hash__()):
                    if c.is_goal():
                        return Solution(c)
                    queue.append(c)
        return None
