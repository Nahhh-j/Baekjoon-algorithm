# 트리의 독립집합

'''
문제
그래프 G(V, E)에서 정점의 부분 집합 S에 속한 모든 정점쌍이 서로 인접하지 않으면 (정점쌍을 잇는 간선이 없으면) S를 독립 집합(independent set)이라고 한다. 독립 집합의 크기는 정점에 가중치가 주어져 있지 않을 경우는 독립 집합에 속한 정점의 수를 말하고, 정점에 가중치가 주어져 있으면 독립 집합에 속한 정점의 가중치의 합으로 정의한다. 독립 집합이 공집합일 때 그 크기는 0이라고 하자. 크기가 최대인 독립 집합을 최대 독립 집합이라고 한다.
문제는 일반적인 그래프가 아니라 트리(연결되어 있고 사이클이 없는 그래프)와 각 정점의 가중치가 양의 정수로 주어져 있을 때, 최대 독립 집합을 구하는 것이다.

입력
첫째 줄에 트리의 정점의 수 n이 주어진다. n은 10,000이하인 양의 정수이다. 1부터 n사이의 정수가 트리의 정점이라고 가정한다. 둘째 줄에는 n개의 정수 w1, w2, ..., wn이 주어지는데, wi는 정점 i의 가중치이다(1 ≤ i ≤ n). 셋째 줄부터 마지막 줄까지는 간선의 리스트가 주어지는데, 한 줄에 하나의 간선을 나타낸다. 간선은 정점의 쌍으로 주어진다. 입력되는 정수들 사이에는 빈 칸이 하나 있다. 가중치들의 값은 10,000을 넘지 않는 자연수이다.

출력
첫째 줄에 최대 독립집합의 크기를 출력한다. 둘째 줄에는 최대 독립집합에 속하는 정점을 오름차순으로 출력한다. 최대 독립 집합이 하나 이상일 경우에는 하나만 출력하면 된다.
'''

import sys
N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
dp = [[0, 0] for _ in range(N+1)]
path = [[[] for _ in range(2)] for _ in range(N+1)]
W = [0] + list(map(int, sys.stdin.readline().split()))
visit = [False] * (N+1)

for _ in range(N-1):
    A, B = map(int, sys.stdin.readline().split())
    tree[A].append(B)
    tree[B].append(A)


def dfs(node):
    visit[node] = True
    dp[node][1] += W[node]
    path[node][1].append(node)

    for x in tree[node]:
        if not visit[x]:
            result = dfs(x)
            dp[node][0] += max(dp[x][0], dp[x][1])
            dp[node][1] += dp[x][0]

            path[node][1] += result[0]
            if dp[x][0] > dp[x][1]:
                path[node][0] += result[0]
            else:
                path[node][0] += result[1]

    return path[node]


p = dfs(1)
if dp[1][0] > dp[1][1]:
    print(dp[1][0])
    p[0].sort()
    for i in p[0]:
        print(i, end=' ')
else:
    print(dp[1][1])
    p[1].sort()
    for i in p[1]:
        print(i, end=' ')