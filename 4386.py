# 별자리 만들기

'''
문제
도현이는 우주의 신이다. 이제 도현이는 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것이다. 별자리의 조건은 다음과 같다.

별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.
별들이 2차원 평면 위에 놓여 있다. 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.

입력
첫째 줄에 별의 개수 n이 주어진다. (1 ≤ n ≤ 100)
둘째 줄부터 n개의 줄에 걸쳐 각 별의 x, y좌표가 실수 형태로 주어지며, 최대 소수점 둘째자리까지 주어진다. 좌표는 1000을 넘지 않는 양의 실수이다.

출력
첫째 줄에 정답을 출력한다. 절대/상대 오차는 10-2까지 허용한다.
'''

import sys
import math
import heapq

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
ps = []
for i in range(n):
    x, y = map(float, input().split())
    ps.append((x, y))

memo = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        memo[i][j] = math.sqrt((ps[i][0] - ps[j][0]) ** 2 + (ps[i][1] - ps[j][1]) ** 2)

sum = 0
visit = set()
mh = []
heapq.heappush(mh, (0, 0))

while len(visit) <= n - 1:
    cost, cur = heapq.heappop(mh)
    if cur in visit:
        continue
    visit.add(cur)
    sum += cost
    for to in range(n):
        if cur != to and to not in visit:
            heapq.heappush(mh, (memo[cur][to], to))

print(f"{sum:.2f}")