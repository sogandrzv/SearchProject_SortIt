# this class only for the first time setup init state for problem and is given to every search
class State:

    def __init__(self, pipes: list, parent, g_n: int, prev_action: tuple):
        self.pipes = pipes
        self.parent = parent
        self.g_n = g_n
        self.f_n = int(0)
        self.prev_action = prev_action

    def h_n(self):
        variety = 0
        full_pipe = 0
        for pipe in self.pipes:
            if not pipe.is_empty:
                variety += pipe.color_variety()
                full_pipe += 1

        return variety + full_pipe

    def set_f_n(self):
        self.f_n = self.h_n() + self.g_n

    # def sort_f_n(self):
    #     self.set_f_n()
    #     return self.f_n

    def __lt__(self, other):
        return self.g_n < other.g_n


    def __gt__(self, other):
        return self.g_n >= other.g_n

    # def __lt__(self, other):
    #     return self.f_n < other.f_n
    #
    #
    # def __gt__(self, other):
    #     return self.f_n > other.f_n




    def change_between_two_pipe(self, pipe_src_ind: int, pipe_dest_ind: int):
        self.pipes[pipe_dest_ind].add_ball(self.pipes[pipe_src_ind].remove_ball())

    def __hash__(self):
        hash_strings = []
        for i in self.pipes:
            hash_strings.append(i.__hash__())
        hash_strings = sorted(hash_strings)
        hash_string = ''
        for i in hash_strings:
            hash_string += i + '###'
        return hash_string
