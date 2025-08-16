import sys
import random

sys.setrecursionlimit(1 << 25)
M = 10 ** 9 + 1

class Node:
    __slots__ = ("key", "prio", "left", "right", "subsum")
    def __init__(self, key):
        self.key = key
        self.prio = random.randint(1, 1 << 30)
        self.left = None
        self.right = None
        self.subsum = key

def getsum(t):
    return 0 if t is None else t.subsum

def update(t):
    if t:
        t.subsum = t.key + getsum(t.left) + getsum(t.right)

def split(t, x):
    """return (<= x, > x)"""
    if t is None:
        return (None, None)
    if t.key <= x:
        a, b = split(t.right, x)
        t.right = a
        update(t)
        return (t, b)
    else:
        a, b = split(t.left, x)
        t.left = b
        update(t)
        return (a, t)

def merge(a, b):
    if not a or not b:
        return a or b
    if a.prio > b.prio:
        a.right = merge(a.right, b)
        update(a)
        return a
    else:
        b.left = merge(a, b.left)
        update(b)
        return b

def find(t, key):
    while t:
        if key == t.key:
            return True
        t = t.left if key < t.key else t.right
    return False

def insert(t, key):
    if find(t, key):
        return t
    node = Node(key)
    a, b = split(t, key)
    a, mid = split(a, key - 1)
    t = merge(merge(a, node), b)
    return t

def erase(t, key):
    if not find(t, key):
        return t
    a, b = split(t, key)
    a, mid = split(a, key - 1)  # mid — единственный key
    # просто выбрасываем mid
    t = merge(a, b)
    return t

def sum_leq(t, x):
    res = 0
    cur = t
    while cur:
        if cur.key <= x:
            res += getsum(cur.left) + cur.key
            cur = cur.right
        else:
            cur = cur.left
    return res

def solve():
    with open('input.txt', 'r', encoding='utf-8') as fin:
        n = int(fin.readline())
        lines = [fin.readline().strip() for _ in range(n)]

    root = None
    x = 0
    out_lines = []

    for line in lines:
        if not line:
            continue
        op, *rest = line.split()
        if op == '+':
            v = (int(rest[0]) + x) % M
            root = insert(root, v)
        elif op == '-':
            v = (int(rest[0]) + x) % M
            root = erase(root, v)
        elif op == '?':
            v = (int(rest[0]) + x) % M
            out_lines.append("Found" if find(root, v) else "Not found")
        else:  # 's'
            l, r = map(int, rest)
            L = (l + x) % M
            R = (r + x) % M
            if L > R:
                L, R = R, L
            ans = sum_leq(root, R) - sum_leq(root, L - 1)
            out_lines.append(str(ans))
            x = ans % M

    with open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
