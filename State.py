import copy

from Problem import Problem


class State:
    def __init__(self, *args):
        if type(args[0]) == Problem:
            self.problem = args[0]
            self.parent = args[1]
        else:
            self.problem = Problem(args[0])
            self.parent = args[1]

    def is_goal(self) -> bool:
        for i in self.problem.pipes:
            if not i.is_one_color():
                return False
        return True

    def change_between_two_pipe(self, pipe_src_ind: int, pipe_dest_ind: int):
        self.problem.pipes[pipe_dest_ind].add_ball(self.problem.pipes[pipe_src_ind].remove_ball())

    def successor(self) -> list:
        l = []
        for i in range(len(self.problem.pipes)):
            for j in range(len(self.problem.pipes)):
                if i == j:
                    continue
                if not self.problem.pipes[j].is_full() and not self.problem.pipes[i].is_empty():
                    s = State(copy.deepcopy(self.problem.pipes), self)
                    s.change_between_two_pipe(i, j)
                    l.append(s)
        return l

    def print_state(self):
        for i in self.problem.pipes:
            i.print_pipe()

    def __hash__(self):
        hash_string = ''
        for i in self.problem.pipes:
            for j in i.stack:
                hash_string += str(j)
            hash_string += '###'
        return hash_string
