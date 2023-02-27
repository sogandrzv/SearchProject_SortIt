from State import State


class Solution:
    def __init__(self, state: State):
        self.state = state

    def print_path(self):
        print('Init State')
        self.state.print_state()
        q = []
        s = self.state.parent
        while s is not None:
            q.append(s)
            s = s.parent
        for index, s in enumerate(q):
            print('---------\n')
            print(f'next step => {index + 1}')
            s.print_state()
