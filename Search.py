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

    @staticmethod
    def ids(prb: Problem):
        k = 0
        while True:
            solution = Search.limited_dfs(prb,k)
            k += 1
            if solution is not None:
                return solution

    @staticmethod
    def ucs(prb: Problem) -> Solution:
        start_time = datetime.now()
        hashmap = {}
        pqueue = queue.PriorityQueue()
        state = prb.initState
        pqueue.put((state.g_n, state))
        hashmap[state.__hash__()] = True

        while not pqueue.empty():
            state = pqueue.get()[1]
            if prb.is_goal(state):
                return Solution(state, prb, start_time)

            children = prb.ucs_successor(state)
            for c in children:
                if c.__hash__() not in hashmap:

                    pqueue.put((c.g_n, c))
                    hashmap[c.__hash__()] = True
        return None

    @staticmethod
    def A_star(prb: Problem) -> Solution:
        start_time = datetime.now()
        hashmap = {}
        pqueue = queue.PriorityQueue()
        state = prb.initState
        state.set_f_n()
        pqueue.put((state.f_n, state))
        hashmap[state.__hash__()] = True

        while not pqueue.empty():
            state = pqueue.get()[1]
            if prb.is_goal(state):
                return Solution(state, prb, start_time)

            children = prb.successor(state)
            for c in children:
                if c.__hash__() not in hashmap:
                    c.set_f_n()
                    pqueue.put((c.f_n, c))
                    hashmap[c.__hash__()] = True
        return None

    @staticmethod
    def ida_star(prb: Problem) -> Solution:
        prb.initState.set_f_n()
        cutoff = prb.initState.f_n

        while True:
            min_f_n = 999999
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

                    c.set_f_n()
                    if cutoff < c.f_n < min_f_n:
                        min_f_n = c.f_n

                    if c.__hash__() not in hashmap and c.f_n <= cutoff:
                        stack.append(c)
                        hashmap[c.__hash__()] = True

            cutoff = min_f_n
            if cutoff > 1000:  # TODO increase limit
                break

        return None

    @staticmethod
    def rbfs(prb: Problem, node, f_limit: int):  # -1 -> goal
        start_time = datetime.now()
        if prb.is_goal(node):
            return Solution(node, prb, start_time), -1
        children = prb.successor(node)
        if not bool(children):  # children list is empty
            return None, 999999

        for c in children:
            c.f_n = max((c.g_n + c.h_n()), node.f_n)

        while True:
            for i in range(2):
                for j in range(0, len(children) - i - 1):
                    if children[j].f_n < children[j + 1].f_n:
                        children[j], children[j + 1] = children[j + 1], children[j]

            best_node = children[len(children) - 1]

            if best_node.f_n > f_limit:
                return None, best_node.f_n
            second_best_node = children[len(children) - 2]
            result, best_node.f_n = Search.rbfs(prb, best_node, min(f_limit, second_best_node.f_n))
            if result is not None:
                return result, -1


    @staticmethod
    def recursive_best_first_search(prb: Problem) -> Solution:
        solution, f_limit = Search.rbfs(prb, prb.initState, 999999)
        if f_limit == -1:
            return solution
        else:
            return None