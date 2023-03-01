from Problem import Problem
from State import State


class Solution:
    def __init__(self, state: State, problem: Problem):
        self.state = state
        self.problem = problem

    def print_path(self):  # this for show path of every search how it's done
        queue = []
        state = self.state.parent
        while state is not None:
            queue.insert(0, state)
            state = state.parent
        print('Init State')
        self.problem.print_state(queue[0])
        for index, state in enumerate(queue[1:]):
            print('---------\n')
            print(f'next step => {index + 1}')
            self.problem.print_state(state)
        print('---------\n')
        print('Solution State')
        self.problem.print_state(self.state)
