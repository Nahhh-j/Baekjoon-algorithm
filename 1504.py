# 특정한 최단 경로

'''
문제
방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1) 임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.

출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.
'''

from heapq import heappop, heappush
maxCost= float('inf')

N, E = map(int,input().split())
G=[ [0 for _ in range(N+1)] for _ in range(N+1) ]
for _ in range(E):
    u,v,c = map(int,input().split())
    G[u][v]=c
    G[v][u]=c
v1, v2 = map(int,input().split())

def dijkstra(start):
    
    heap=[]
    heappush(heap, [0,start])
    
    visited=[-1 for _ in range(N+1)]
    dist = [maxCost for _ in range(N+1)]
    dist[start]=0                           
    while heap:
        cost, node = heappop(heap)
        
        if visited[node]!=1:
            visited[node]=1
            
            for next in range(1,N+1):
                if node!=next and visited[next]==-1 and G[node][next]!=0:
                    
                    if dist[next] >= G[node][next] + cost:
                        dist[next] = G[node][next] + cost
                        heappush(heap, [dist[next], next])
    
    return dist

dist_start, dist_v1, dist_v2 = dijkstra(1), dijkstra(v1), dijkstra(v2)

tmp1= dist_start[v1] + dist_v1[v2] + dist_v2[N]
tmp2= dist_start[v2] + dist_v2[v1] + dist_v1[N]

if tmp1==maxCost and tmp2==maxCost:
    print(-1)
else:
    print(min(tmp1,tmp2))