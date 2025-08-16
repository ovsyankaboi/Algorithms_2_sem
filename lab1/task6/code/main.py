def count_k_almost_palindromes(s: str, k: int) -> int:
    n = len(s)
    total = 0

    # нечётные длины
    for c in range(n):
        l = r = c
        mism = 0
        while l >= 0 and r < n:
            if s[l] != s[r]:
                mism += 1
            if mism > k:
                break
            total += 1
            l -= 1
            r += 1

    # чётные длины
    for c in range(n - 1):
        l, r = c, c + 1
        mism = 0
        while l >= 0 and r < n:
            if s[l] != s[r]:
                mism += 1
            if mism > k:
                break
            total += 1
            l -= 1
            r += 1

    return total

def solve():
    with open('input.txt', 'r', encoding='utf-8') as fin:
        n_k = fin.readline().split()
        n, k = int(n_k[0]), int(n_k[1])
        s = fin.readline().strip()

    ans = count_k_almost_palindromes(s, k)

    with open('output.txt', 'w', encoding='utf-8') as fout:
        fout.write(str(ans))


if __name__ == "__main__":
    solve()
