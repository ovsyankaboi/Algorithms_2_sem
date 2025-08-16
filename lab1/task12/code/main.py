def solve():
    with open('input.txt', 'r', encoding='utf-8') as fin:
        line = fin.readline()
        if not line:
            n = 0
        else:
            n = int(line.strip())

        if n == 0:
            with open('output.txt', 'w', encoding='utf-8') as fout:
                fout.write("")
            return

        K = [0] * (n + 1)
        L = [0] * (n + 1)
        R = [0] * (n + 1)
        parent = [0] * (n + 1)

        for i in range(1, n + 1):
            k, l, r = map(int, fin.readline().split())
            K[i], L[i], R[i] = k, l, r
            if l != 0:
                parent[l] = i
            if r != 0:
                parent[r] = i

    root = 1
    while root <= n and parent[root] != 0:
        root += 1
    if root > n:
        root = 1

    height = [0] * (n + 1)
    balance = [0] * (n + 1)

    stack = [(root, 0)]
    while stack:
        v, phase = stack.pop()
        if v == 0:
            continue
        if phase == 0:
            stack.append((v, 1))
            stack.append((R[v], 0))
            stack.append((L[v], 0))
        else:
            hl = height[L[v]] if L[v] != 0 else 0
            hr = height[R[v]] if R[v] != 0 else 0
            height[v] = (hl if hl > hr else hr) + 1
            balance[v] = hr - hl

    with open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write("\n".join(str(balance[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()
