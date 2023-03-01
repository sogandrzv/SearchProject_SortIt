from Problem import Problem
from State import State


class Solution:
    def __init__(self, state: State, problem: Problem):
        self.state = state
        self.problem = problem

    def print_path(self):  # this for show path of every search how it's done
        q = []
        s = self.state.parent
        while s is not None:
            q.insert(0, s)
            s = s.parent
        print('Init State')
        self.problem.print_state(q[0])
        for index, s in enumerate(q[1:]):
            print('---------\n')
            print(f'next step => {index + 1}')
            self.problem.print_state(s)
        print('---------\n')
        print('Solution State')
        self.problem.print_state(self.state)
