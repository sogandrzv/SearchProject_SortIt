from Pipe import Pipe
from Problem import Problem
from Search import Search

if __name__ == '__main__':
    p1 = Pipe([1, 1, 2], 4)
    p2 = Pipe([2, 2, 2], 4)
    p3 = Pipe([1], 4)
    s = Search.bfs(Problem([p1, p2, p3]))
    s.print_path()
