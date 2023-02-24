from State import State


class Solution:
    def __init__(self, state: State):
        self.state = state

    def print_path(self):
        for i in self.state.path:
            i.print_state()
            print('###')
        self.state.print_state()
