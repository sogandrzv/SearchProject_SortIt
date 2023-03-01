# this class only for the first time setup init state for problem and is given to every search
class State:
    def __init__(self, pipes: list, parent, g_n: int):
        self.pipes = pipes
        self.parent = parent
        self.g_n = g_n

    def change_between_two_pipe(self, pipe_src_ind: int, pipe_dest_ind: int):
        self.pipes[pipe_dest_ind].add_ball(self.pipes[pipe_src_ind].remove_ball())

    def __hash__(self):
        hash_string = ''
        for i in self.pipes:
            for j in i.stack:
                hash_string += str(j)
            hash_string += '###'
        return hash_string
