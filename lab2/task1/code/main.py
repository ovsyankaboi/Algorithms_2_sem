def inorder(keys, left, right, root=0):
    res = []
    stack = []
    v = root
    while v != -1 or stack:
        while v != -1:
            stack.append(v)
            v = left[v]
        v = stack.pop()
        res.append(str(keys[v]))
        v = right[v]
    return res

def preorder(keys, left, right, root=0):
    res = []
    stack = [root]
    while stack:
        v = stack.pop()
        if v == -1:
            continue
        res.append(str(keys[v]))
        stack.append(right[v])
        stack.append(left[v])
    return res

def postorder(keys, left, right, root=0):
    res = []
    stack = [(root, False)]  
    while stack:
        v, seen = stack.pop()
        if v == -1:
            continue
        if seen:
            res.append(str(keys[v]))
        else:
            stack.append((v, True))
            stack.append((right[v], False))
            stack.append((left[v], False))
    return res

def solve():
    with open('input.txt', 'r', encoding='utf-8') as fin:
        n_line = fin.readline().strip()
        n = int(n_line)
        keys = [0] * n
        left = [0] * n
        right = [0] * n
        for i in range(n):
            k, l, r = map(int, fin.readline().split())
            keys[i], left[i], right[i] = k, l, r

    in_ord  = inorder(keys, left, right, 0)
    pre_ord = preorder(keys, left, right, 0)
    post_ord= postorder(keys, left, right, 0)

    with open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write(" ".join(in_ord) + "\n")
        fout.write(" ".join(pre_ord) + "\n")
        fout.write(" ".join(post_ord) + "\n")

if __name__ == "__main__":
    solve()
