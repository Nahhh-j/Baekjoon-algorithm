# 서로 다른 소수의 합

'''
문제
양의 정수는 서로 다른 소수의 합으로 나타낼 수 있다. 두 정수 n과 k가 주어졌을 때, n을 서로 다른 k개의 소수의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오. 여기서 덧셈의 순서만 다른 경우(3+5, 5+3)는 모두 1가지로 센다.
예를 들어, n=24, k=3일 때, 2가지로 나타낼 수 있다. {2, 3, 19}, {2, 5, 17} 합이 24가 되는 서로 다른 소수 3개는 이 2가지를 제외하고는 없다. 또, n=24, k=2일 때 답은 {5, 19}, {7, 17}, {11, 13} 3가지이며, n=2, k=1일 때 답은 {2} 1가지이다. n=1, k=1일 경우에는 1은 소수가 아니기 때문에 답은 0이다. 마지막으로 서로 다른 2개 소수의 합이 4가 되는 경우도 없기 때문에, n=4, k=2도 답이 0이다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각각의 테스트 케이스는 한 줄에 n과 k가 공백으로 구분되어 있다. (n ≤ 1120, k ≤ 14)

출력
각 테스트 케이스에 해당하는 경우의 수를 한 줄에 하나씩 출력한다. 정답은 항상 231보다 작다.
'''

import sys

input = sys.stdin.readline

MAX_N = 1120
MAX_K = 14

is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX_N ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False

primes = [i for i in range(2, MAX_N + 1) if is_prime[i]]

dp = [[0] * (MAX_N + 1) for _ in range(MAX_K + 1)]
dp[0][0] = 1

for p in primes:
    for k in range(MAX_K, 0, -1):
        for n in range(MAX_N, p - 1, -1):
            dp[k][n] += dp[k - 1][n - p]

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    print(dp[k][n])