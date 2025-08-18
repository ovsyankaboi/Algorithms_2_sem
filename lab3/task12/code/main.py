def solve():
    with open('input.txt', 'r', encoding='utf-8') as fin:
        data = list(map(int, fin.read().split()))
    if not data:
        with open('output.txt', 'w', encoding='utf-8') as fout:
            fout.write('INCORRECT')
        return

    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [dict() for _ in range(n + 1)]
    for _ in range(m):
        u = next(it); v = next(it); c = next(it)
        adj[u][c] = v
        adj[v][c] = u

    k = next(it)
    colors = [next(it) for _ in range(k)] if k > 0 else []

    cur = 1
    for col in colors:
        nxt = adj[cur].get(col)
        if nxt is None:
            with open('output.txt', 'w', encoding='utf-8') as fout:
                fout.write('INCORRECT')
            return
        cur = nxt

    with open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write(str(cur))

if __name__ == "__main__":
    solve()
