# RGB거리 2

'''
문제
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.
집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
'''

import sys

N = int(sys.stdin.readline().rstrip())
houses = [[-1, -1, -1]]
for _ in range(N):
    houses.append(list(map(int, sys.stdin.readline().rstrip().split())))

R, G, B = 0, 1, 2

dp = [[-1] * 3 for _ in range(N+1)]
dp[1] = houses[1]

for i in range(2, N+1):
    dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + houses[i][R]
    dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + houses[i][G]
    dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + houses[i][B]

print(min(dp[N]))