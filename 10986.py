# 나머지 합

'''
문제
수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.
즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.

입력
첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)
둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)

출력
첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

r = [0] * m
prefixSum = 0
for i in range(n):
    prefixSum += a[i]
    r[prefixSum % m] += 1

ans = r[0]
for i in range(m):
    ans += r[i] * (r[i]-1) // 2
print(ans)