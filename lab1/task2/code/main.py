def read_n_ints(fin, n):
    vals = []
    while len(vals) < n:
        line = fin.readline()
        if not line:
            break
        vals.extend(map(int, line.split()))
    if len(vals) != n:
        raise ValueError("Ожидалось %d чисел, получено %d" % (n, len(vals)))
    return vals

def solve():
    with open('input.txt', 'r', encoding='utf-8') as fin:
        first = fin.readline()
        while first is not None and first.strip() == '':
            first = fin.readline()
        n = int(first.strip())

        a = read_n_ints(fin, n)
        b = read_n_ints(fin, n)

    a.sort()
    b.sort()
    ans = sum(x * y for x, y in zip(a, b))

    with open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write(str(ans))

if __name__ == "__main__":
    solve()
