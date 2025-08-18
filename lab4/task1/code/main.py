def prefix_function(s: str):
    pi = [0] * len(s)
    for i in range(1, len(s)):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        p = f.readline().strip()
        t = f.readline().strip()

    m = len(p)
    s = p + '#' + t
    pi = prefix_function(s)

    pos = []

    for i in range(m + 1, len(s)):
        if pi[i] == m:
            pos.append(i - 2 * m + 1)

    with open('output.txt', 'w', encoding='utf-8') as out:
        out.write(str(len(pos)) + '\n')
        out.write(' '.join(map(str, pos)))

if __name__ == "__main__":
    main()
