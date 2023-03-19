from Solution import Solution
from Problem import Problem
from datetime import datetime


class Search:
    @staticmethod
    def bfs(prb: Problem) -> Solution:  # this method get a first state of Problem and do bfs for find solution if no
        # solution is find return None else return the solution
        start_time = datetime.now()
        queue = []
        state = prb.initState
        queue.append(state)
        while len(queue) > 0:
            state = queue.pop(0)
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                queue.append(c)
        return None

    @staticmethod
    def dfs(prb: Problem) -> Solution:
        start_time = datetime.now()
        stack = []
        state = prb.initState
        stack.append(state)
        while len(stack) > 0:
            state = stack.pop()
            children = prb.successor(state)
            for c in children:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                stack.append(c)
        return None

    @staticmethod
    def optimized_dfs(prb: Problem) -> Solution:
        start_time = datetime.now()
        hashmap = {}
        stack = []
        state = prb.initState
        stack.append(state)
        hashmap[state.__hash__()] = True

        while len(stack) > 0:
            state = stack.pop()
            # hashmap[state.__hash__()] = False
            children = prb.successor(state)
            for c in children:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                if c.__hash__() not in hashmap:
                    stack.append(c)
                    hashmap[c.__hash__()] = True
        return None

    @staticmethod
    def limited_dfs(prb: Problem, cutoff) -> Solution:
        start_time = datetime.now()
        hashmap = {}
        stack = []
        state = prb.initState
        stack.append(state)
        hashmap[state.__hash__()] = True

        while len(stack) > 0:
            state = stack.pop()
            hashmap[state.__hash__()] = False
            children = prb.successor(state)

            for c in children:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                if c.__hash__() not in hashmap and c.g_n <= cutoff:
                    stack.append(c)
                    hashmap[c.__hash__()] = True
        return None


