MAX_DEPTH = 4


class Node(list):
    def __init__(self, children, parent=None):
        list.__init__(self, children)
        self.parent: Node = parent
        for child in self:
            if isinstance(child, Node):
                child.parent = self

    def depth(self):
        return self.parent.depth() + 1 if self.parent else 1

    def leaf(self, side):
        return self[side].leaf(side) if isinstance(self[side], Node) else (self, side)

    def neighbor(self, side):
        if self.parent:
            if self.parent[side] is self:
                return self.parent.neighbor(side)
            else:
                return self.parent[side].leaf(1 - side) if isinstance(self.parent[side], Node) else (self.parent, side)
        else:
            return None, 0

    def explode(self):
        for i, x in enumerate(self):
            node, j = self.neighbor(i)
            if node:
                node[j] += x
        self.parent[self.parent.index(self)] = 0

    def explode_all(self):
        if self.depth() > MAX_DEPTH:
            self.explode()
            return True
        else:
            return any([child.explode_all() for child in self if isinstance(child, Node)])

    def split(self, i):
        q, r = divmod(self[i], 2)
        self[i] = Node([q, q + r], self)

    def split_next(self):
        for i, child in enumerate(self):
            if isinstance(child, Node):
                if child.split_next():
                    return True
            else:
                if child > 9:
                    self.split(i)
                    return True
        return False

    def reduce(self):
        self.explode_all()
        while self.split_next():
            self.explode_all()
        return self

    def __abs__(self):
        return sum(x * abs(c) for x, c in zip((3, 2), self))

    def __add__(self, node):
        return Node([self.copy(), node.copy()]).reduce()

    def copy(self):
        return Node([c.copy() if isinstance(c, Node) else c for c in self])


def solve(data):
    numbers = [parse(iter(seq)) for seq in data.split()]
    # return abs(sum(numbers[1:], numbers[0]))
    return max(abs(n0 + n1) for n0 in numbers for n1 in numbers if n0 is not n1)

    # m = 0
    # for n0 in numbers:
    #     for n1 in numbers:
    #         if n0 is not n1:
    #             x = abs(n0 + n1)
    #             if x > m:
    #                 m = x
    #                 print(f'{x} <= {n0} ++ {n1}')


def parse(seq):
    return Node([parse(seq), next(seq), parse(seq), next(seq)][::2]) if (c := next(seq)) == '[' else int(c)


DATA0 = '''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''

DATA = open(__file__.removesuffix('.py') + '.txt').read()


def main(use_test_data=True):
    from time import time_ns
    t0 = time_ns()
    solution = solve(DATA0 if use_test_data else DATA)
    calc_time = (time_ns() - t0) / 1e6
    print(f'Solution ====> {solution} | Calc time = {calc_time:.0f} ms.')


if __name__ == '__main__':
    # main()
    main(False)
