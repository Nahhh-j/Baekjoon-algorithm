# 유럽여행

'''
문제
민식이는 여름에 유럽여행을 떠날 계획이다. 방문할 나라는 총 N개의 나라이고 편리하게 1번부터 N번까지 번호를 붙였다. 또한 이 나라들 사이에 이동 가능한 길은 M개가 있는데 민식이는 귀찮기 때문에 N개의 나라가 서로 연결된 것을 유지시키면서 최대한 많은 길을 지도에서 제거하고자 한다. 즉, N-1개의 길만을 남겨야할 것이다.
각 길을 통과하기 위한 비용이 각기 다르고 한 나라를 도착하면 내야할 비용 역시 나라마다 다르게 정해져있다. 민식이는 모든 도시를 최소 한번 이상 방문하면서 최소 비용이 드는 방법을 찾고 있다. 물론 길과 나라는 여러 번 방문할 수 있고, 첫 시작 나라는 민식이가 정할 수 있고, 마지막 나라는 시작 나라이어야 한다. 이러한 민식이의 유럽 계획을 도와주자. 

입력
첫 줄에는 방문할 나라의 수 N(5 ≤ N ≤ 10,000)과 이 나라들 사이를 연결하는 길의 수 P(N-1 ≤ P ≤ 100,000)가 주어진다. 두 번째 줄에는 N+1번째 줄까지 i+1번째 줄에는 i번째 나라를 방문할 때 드는 비용 Ci (1 ≤ Ci ≤ 1,000)가 입력된다. 다음 P개의 줄에는 P개의 길에 대한 정보를 의미하는 세 정수 Sj, Ej, Lj가 입력되는데 이는 Sj번째 나라와 Ej번째 나라 사이를 연결짓는 길을 통과하기 위해서는 Lj 비용이 든다는 의미이다. (Sj ≠ Ej, 0 ≤ Lj ≤ 1,000)

출력
첫 줄에 민식이가 유럽여행을 마치기 위한 최소비용을 출력한다.
'''

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def find_set(u):
    curr = u
    history = []
    while curr != parent[curr]:
        history.append(curr)
        curr = parent[curr]
    for h in history:
        parent[h] = curr
    return curr

def union_set(u, v):
    if u == v:
        return False
    if rank[u] >= rank[v]:
        parent[v] = u
        if rank[u] == rank[v]:
            rank[u] += 1
    else:
        parent[u] = v
    return True


N, M = map(int, input().split())
parent = list(range(N+1))
rank = [0]*(N+1)
edges = []

village_cost = [9999999999]

for _ in range(N):
    village_cost.append(int(input()))

for _ in range(M):
    a, b, c = map(int, input().split())
    c += village_cost[a] + village_cost[b] + c
    heappush(edges, (c, a, b))

connected_cnt = 0
ans = 0
while connected_cnt < N - 1:
    w, x, y = heappop(edges)
    xr, yr = find_set(x), find_set(y)
    if union_set(xr, yr):
        ans += w
        connected_cnt += 1
        
ans += min(village_cost)

print(ans)