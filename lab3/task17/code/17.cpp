#include <cstdio>
#include <vector>
#include <algorithm>

int main() {
    int nV, nE;
    scanf("%d %d", &nV, &nE);
    const int INF = 1000 * 1000 * 1000;
    std::vector<std::vector<int>> d(nV, std::vector<int>(nV, INF));
    for (int i = 0; i < nV; i++) {
        d[i][i] = 0;
    }
    for (int i = 0; i < nE; i++) {
        int v1, v2;
        scanf("%d %d", &v1, &v2);
        v1--;
        v2--;
        d[v1][v2] = 0;
        d[v2][v1] = std::min(d[v2][v1], 1);
    }
    for (int k = 0; k < nV; k++) {
        for (int i = 0; i < nV; i++) {
            for (int j = 0; j < nV; j++) {
                d[i][j] = std::min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }
    int max = 0;
    for (int i = 0; i < nV; i++) {
        for (int j = 0; j < nV; j++) {
            max = std::max(max, d[i][j]);
        }
    }
    printf("%d", max);
    return 0;
}
