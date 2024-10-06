# 달리기 코스

'''
문제
캠프가 시작된 지도 벌써 12일이 지났다. 이제 캠프의 반이 지났을 뿐인데, 학생들은 벌써 운동부족을 호소하고 있다.
선생님은 학생들에게 달리기 시합을 시키기로 결정하고, 달리기 시합에서 1등을 한 사람은 훼밀리마트에 데려가기로 했다. 적절한 운동장을 찾고 있던 중, 숙소 근처에서 널찍한 운동장을 발견했다. 그 곳에는 가느다란 기둥이 N개 꽂혀 있었다.
달리기 코스는 한 기둥에서 시작하여 다른 기둥까지 직선코스이고 코스 내에 다른 기둥이 포함되어도 상관하지 않는다. 학생들을 운동시키는 것이 이 시합의 목적이므로, 최대한 멀리 떨어져 있는 두 기둥으로 지표를 잡으려고 한다.
이 숙소에서 나가 달리기를 하고 싶다면 이 문제를 풀어야 한다. N개의 기둥의 좌표가 주어졌을 때, 가장 멀리 떨어진 두 기둥 사이의 거리의 제곱을 출력하는 프로그램을 작성하라.

입력
첫째 줄에 기둥의 개수 N(1 ≤ N ≤ 100,000)이 주어지고, 이어서 N줄에 걸쳐 각 기둥의 좌표를 나타내는 정수 두 개가 주어진다. 좌표의 절댓값의 범위는 50,000을 넘을 수 없다.

출력
첫째 줄에 가장 먼 기둥 사이의 거리를 제곱하여 출력한다.
'''

#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

typedef struct point {
    int x, y, p, q;
    point() : point(0, 0, 0, 0) {};
    point(int x_, int y_, int p_, int q_) : x(x_), y(y_), p(p_), q(q_) {}

    bool operator < (const struct point& z) const {
        if (1LL * q * z.p != 1LL * p * z.q) return 1LL * q * z.p < 1LL * p * z.q;
        if (y != z.y) return y < z.y;
        return x < z.x;
    }
} point;

long long ccw(const int px, const int py, const int qx, const int qy)
{
    return 1LL * px * qy - 1LL * qx * py;
}

long long ccw(const point& p1, const point& p2, const point& p3)
{
    return ccw(p2.x - p1.x, p2.y - p1.y, p3.x - p1.x, p3.y - p1.y);
}

long long dist(const point& p1, const point& p2)
{
    return 1LL * (p1.x - p2.x) * (p1.x - p2.x) + 1LL * (p1.y - p2.y) * (p1.y - p2.y);
}

int main()
{
    int n;
    int st[100001] = { 0 };
    point p[100001];

    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        int x, y;
        scanf("%d %d", &x, &y);
        p[i] = point(x, y, 0, 0);
    }

    if (n == 1) {
        puts("0");
        return 0;
    }

    sort(p, p + n);
    for (int i = 1; i < n; ++i) {
        p[i].p = p[i].x - p[0].x;
        p[i].q = p[i].y - p[0].y;
    }
    sort(p + 1, p + n);

    // Get ConvexHull using Graham's scan
    st[0] = 0; st[1] = 1;
    int pos = 2;
    for (int i = 2; i < n; ++i) {
        while (pos >= 2 && ccw(p[st[pos - 2]], p[st[pos - 1]], p[i]) <= 0) {
            pos--;
        }
        st[pos] = i;
        pos++;
    }

    // Rotating Calipers
    int j = 1;
    long long ans = 0;
    for (int i = 0; i < pos; ++i) {
        int ni = (i + 1) % pos, nj;
        for (;;) {
            nj = (j + 1) % pos;
            long long ret = ccw(p[st[ni]].x - p[st[i]].x, p[st[ni]].y - p[st[i]].y,
                                p[st[nj]].x - p[st[j]].x, p[st[nj]].y - p[st[j]].y);

            if (ret > 0) j = nj;
            else break;
        }
        if (i != j) {
            long long d = dist(p[st[i]], p[st[j]]);
            if (d > ans) ans = d;
        }
    }

    printf("%lld\n", ans);
    return 0;
}