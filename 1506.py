# 경찰서

'''
문제
종욱이가 살고있는 나라에는 도시가 N개 있고, 도시의 일부는 일방 통행 도로로 연결되어 있다. 종욱이가 살고있는 나라의 대통령 욱종이는 범죄와 싸우기 위해서 일부 도시에 경찰서를 세우려고 한다. 도시 i에 경찰서를 세우는 비용은 cost[i] 이다.
도시 i에 세운 경찰서가 도시 j를 통제할 수 있으려면, i에서 j로 갔다가, 다시 돌아오는 경로가 존재해야 한다.
도로가 연결되어 있는 상태와 각 도시에 경찰서를 지을 때 필요한 비용이 주어졌을 때, 모든 도시를 통제하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 도시의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 각 도시에 경찰서를 세우는데 드는 비용이 주어진다. 셋째 줄부터 도로가 연결되어 있는 상태가 한 줄에 한 줄에 하나씩 주어진다. i번째 줄의 j번째 문자가 0인 경우에는 도시 i에서 도시 j로 갈 수 없는 것이고, 1인 경우에는 갈 수 있는 것이다.
경찰서를 세우는 비용은 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 도시를 통제하는데 필요한 최소 비용을 출력한다.
'''

n = int(input())
cost = list(map(int, input().split()))

graph = []
for _ in range(n):
    graph.append([int(x) for x in input()])

node_id = 0
stack = []
on_stack = [False for _ in range(n)]
parent = [-1 for _ in range(n)]

def dfs(node):
    global answer

    global node_id
    cur_id = node_id
    node_id += 1

    parent[node] = cur_id
    stack.append(node)
    on_stack[node] = True

    for i in range(n):
        if graph[node][i] == 1:

            if parent[i] == -1:
                dfs(i)
                parent[node] = min(parent[node], parent[i])

            elif on_stack[i]:
                parent[node] = min(parent[node], parent[i])

    ## find scc
    if parent[node] == cur_id:
        scc = []
        while True:
            elem = stack.pop()
            on_stack[elem] = False
            scc.append(elem)
            if elem == node:
                break

        min_cost = 9876543210
        for node in scc:
            min_cost = min(min_cost, cost[node])
        answer += min_cost


answer = 0
for i in range(n):
    if parent[i] == -1:
        dfs(i)
print(answer)