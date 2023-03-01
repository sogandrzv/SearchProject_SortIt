from Pipe import Pipe
from Problem import Problem
from State import State
from Search import Search

if __name__ == '__main__':
    p1 = Pipe(['red', 'red', 'blue'], 4)
    p2 = Pipe(['blue', 'blue', 'blue'], 4)
    p3 = Pipe(['red', 'red'], 4)
    s = Search.bfs(Problem(State([p1, p2, p3], None, 0)))
    s.print_path()
