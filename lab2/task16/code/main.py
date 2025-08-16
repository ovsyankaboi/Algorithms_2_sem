import sys, random
sys.setrecursionlimit(1 << 25)
random.seed(0xC0FFEE)

class Node:
    __slots__ = ("key", "prio", "l", "r", "sz")
    def __init__(self, key: int):
        self.key = key
        self.prio = random.randint(1, 1 << 30)
        self.l = None
        self.r = None
        self.sz = 1

def size(t): return 0 if t is None else t.sz
def upd(t):
    if t: t.sz = 1 + size(t.l) + size(t.r)

def split(t, key):

    if t is None: return (None, None)
    if key <= t.key:
        a, t.l = split(t.l, key)
        upd(t); return a, t
    else:
        t.r, b = split(t.r, key)
        upd(t); return t, b

def merge(a, b):
    if not a or not b: return a or b
    if a.prio > b.prio:
        a.r = merge(a.r, b); upd(a); return a
    else:
        b.l = merge(a, b.l); upd(b); return b

def insert(t, key):
  
    a, b = split(t, key)
    t = merge(merge(a, Node(key)), b)
    return t

def erase(t, key):
    a, b = split(t, key)
    mid, c = split(b, key + 1)   
    return merge(a, c)

def kth_smallest(t, k):
   
    cur = t
    while cur:
        ls = size(cur.l)
        if k < ls:
            cur = cur.l
        elif k == ls:
            return cur.key
        else:
            k -= ls + 1
            cur = cur.r
    raise IndexError("k out of range")

def solve():
    with open('input.txt', 'r', encoding='utf-8') as fin:
        n = int(fin.readline())
        lines = [fin.readline().strip() for _ in range(n)]

    root = None
    out = []

    for line in lines:
        if not line:
            continue
        tkn, val = line.split()
        x = int(val)
        if tkn == '+1':
            root = insert(root, x)
        elif tkn == '-1':
            root = erase(root, x)
        else:  
            k = x
            idx = size(root) - k          
            ans = kth_smallest(root, idx)
            out.append(str(ans))

    with open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write("\n".join(out))

if __name__ == "__main__":
    solve()
