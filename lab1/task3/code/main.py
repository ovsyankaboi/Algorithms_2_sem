def solve():
    with open('input.txt', 'r', encoding='utf-8') as fin:
        line = fin.readline()
        while line and line.strip() == '':
            line = fin.readline()
        n = int(line.strip())
        intervals = []
        for _ in range(n):
            line = fin.readline()
            while line and line.strip() == '':
                line = fin.readline()
            s, f = map(int, line.split())
            intervals.append((f, s))
    intervals.sort()
    count = 0
    last_end = -1
    for f, s in intervals:
        if s >= last_end:
            count += 1
            last_end = f
    with open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write(str(count))

if __name__ == "__main__":
    solve()
