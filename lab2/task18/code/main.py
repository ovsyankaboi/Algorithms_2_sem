import sys, random
sys.setrecursionlimit(1 << 25)

BLOCK = 1000

class Node:
    __slots__ = ("s", "prio", "l", "r", "sz")
    def __init__(self, s: str):
        self.s = s
        self.prio = random.randint(1, 1 << 30)
        self.l = None
        self.r = None
        self.sz = len(s)

def size(t): return 0 if t is None else t.sz
def upd(t):
    if t: t.sz = len(t.s) + size(t.l) + size(t.r)

def merge(a, b):
    if not a or not b: return a or b
    if a.prio > b.prio:
        a.r = merge(a.r, b); upd(a); return a
    else:
        b.l = merge(a, b.l); upd(b); return b

def split(t, k):
    if t is None: return None, None
    left_sz = size(t.l)
    if k < left_sz:
        L, t.l = split(t.l, k); upd(t); return L, t
    elif k > left_sz + len(t.s):
        t.r, R = split(t.r, k - left_sz - len(t.s)); upd(t); return t, R
    else:
        # разрез попадает внутрь текущего узла
        pos = k - left_sz
        s = t.s
        Ltree = t.l
        Rtree = t.r
        left_node = Node(s[:pos]) if pos > 0 else None
        right_node = Node(s[pos:]) if pos < len(s) else None
        L = Ltree if left_node is None else merge(Ltree, left_node)
        R = Rtree if right_node is None else merge(right_node, Rtree)
        return L, R

def build_from_string(s: str):
    root = None
    for i in range(0, len(s), BLOCK):
        root = merge(root, Node(s[i:i+BLOCK]))
    return root

def inorder_to_string(t):
    out, st, cur = [], [], t
    while cur or st:
        while cur: st.append(cur); cur = cur.l
        cur = st.pop()
        out.append(cur.s)
        cur = cur.r
    return "".join(out)

def solve():
    with open('input.txt', 'r', encoding='utf-8') as fin:
        S = fin.readline().rstrip('\n')
        q = int(fin.readline())
        ops = [tuple(map(int, fin.readline().split())) for _ in range(q)]

    root = build_from_string(S)

    for i, j, k in ops:
        left, rest = split(root, i)
        mid, right = split(rest, j - i + 1)
        root = merge(left, right)
        L, R = split(root, k)
        root = merge(merge(L, mid), R)

    ans = inorder_to_string(root)
    with open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write(ans)

if __name__ == "__main__":
    solve()
