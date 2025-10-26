# 열혈강호 6

'''
문제
강호네 회사에는 직원이 N명이 있고, 해야 할 일이 M개가 있다. 직원은 1번부터 N번까지 번호가 매겨져 있고, 일은 1번부터 M번까지 번호가 매겨져 있다.
각 직원은 자신이 할 수 있는 일들 중 한 개의 일만 담당할 수 있고, 각각의 일을 담당하는 사람은 1명이어야 한다.
각각의 직원이 할 수 있는 일의 목록과 그 일을 할 때 강호가 지급해야 하는 월급이 주어졌을 때, M개의 일 중에서 최대 몇 개를 할 수 있는지, 그리고 그 때 강호가 지불해야 하는 월급의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 직원의 수 N과 일의 개수 M이 주어진다. (1 ≤ N, M ≤ 400)
둘째 줄부터 N개의 줄의 i번째 줄에는 i번 직원이 할 수 있는 일의 개수와 할 수 있는 일의 번호와 그 일을 할 때 지급해야 하는 월급이 주어진다. 월급은 10,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 강호네 회사에서 할 수 있는 일의 개수를 출력한다.
둘째 줄에는 강호가 지급해야 하는 월급의 최댓값을 출력한다.
'''

import sys
from collections import *
def input(): return [*map(int,sys.stdin.readline().split())]

def SPFA():
  DP = [1e9]*K; DP[0] = 0
  parent = [0]*K
  dq = deque([0]); inq = [0]*K
  while dq:
    now = dq.popleft()
    inq[now] = 0
    for next,w,c in graph[now]:
      if c-flow[now][next] and (w1:=DP[now]+w)<DP[next]:
        DP[next] = w1; parent[next] = now
        if not inq[next]:
          dq.append(next); inq[next] = 1
  if DP[N+1]<1e9:
    return DP[N+1],parent

def solve():
  cnt = cost = 0
  while spfa:=SPFA():
    c,parent = spfa
    now = N+1
    while now:
      last = parent[now]
      flow[last][now] += 1; flow[now][last] -= 1
      now = last
    cnt += 1; cost += c
  print(cnt); print(-cost)

N,M = input(); K = N+M+2
graph = [[(i,0,1) for i in range(1,N+1)]]+[[(0,0,0)] for i in range(N)]+[[(-i,0,0) for i in range(1,M+1)]]+[[(N+1,0,1)] for i in range(M)]
for i in range(1,N+1):
  n,*data = input()
  for j in range(n):
    j,w = -data[j*2],-data[j*2+1]
    graph[i].append((j,w,1)); graph[j].append((i,-w,0))
flow = [[0]*K for i in range(K)]
solve()