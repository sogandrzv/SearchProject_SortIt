class Pipe:
    def __init__(self, stack: list, limit: int):
        self.stack = stack
        self.limit = limit

    def is_one_color(self) -> bool:  # this function checks that all balls are the same color
        for i in range(1, len(self.stack)):
            if self.stack[i] != self.stack[i - 1]:
                return False
        return True

    def add_ball(self, color):
        self.stack.append(color)

    def remove_ball(self):
        return self.stack.pop()

    def is_full(self):
        if len(self.stack) == self.limit:
            return True
        return False

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def print_pipe(self):
        print('{', end=' ')
        for i in self.stack:
            print(i, end=' ')
        print('}')

    def __hash__(self):
        hash_string = ''
        for i in self.stack:
            hash_string += str(i)
        return hash_string
