# 숌작업

'''
문제
루트가 있는 트리에서, 어떤 정점 V의 레벨이 L이라는 것은, 루트와 정점 V사이의 거리가 L이라는 것을 의미한다. 정점 U가 정점 V의 부모라는 것은 정점 U와 정점 V가 서로 연결되어 있고, U의 레벨이 L-1, V의 레벨이 L인 것을 의미한다.
다솜이는 루트가 있는 트리를 다음과 같은 작업을 몇 번을 수행하려고 한다.
다솜이는 다음과 같은 작업을 숌작업이라고 이름붙였다.
숌작업은 다음과 같다.

루트가 아닌 정점 V를 선택한다.
V의 조상중 하나인 정점 U를 선택한다.
V와 V의 부모를 이은 간선을 제거한다.
U에서 V로 간선을 이은다. U는 V의 부모가 된다.
숌작업은 독특해서 한번의 작업에 가격이 있다.
가격은 두 정점의 레벨 차이 - 1이다.
예를 들어, V의 레벨이 L1이고, U의 레벨이 L2이면, 숌작업의 가격은 L1-L2-1이다.
어떤 트리의 높이가 K라는 것은, K가 레벨인 정점이 몇 개 있고, K+1인 정점이 없다는 것을 의미한다. 어떤 트리와 숌작업을 이용해서 줄이려고 하는 높이 H가 주어졌을 때, 그 트리를 H보다 작거나 같은 높이로 숌작업을 통해서 줄이는 최소 가격을 출력하는 프로그램을 작성하시오. 숌작업은 여러 번 수행해도 된다.
예를 들어, 다음과 같은 트리가 주어졌다. 이 트리의 높이를 1보다 작거나 같게 만들려고 한다.

이 트리의 정점 2를 0의 자식으로 연결 하면, 총 비용은 2-0-1 = 1이 되고, 트리의 높이는 1이된다.

입력
첫째 줄에 정점의 수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄부터 총 N-1개의 줄에 트리의 간선이 주어진다. 트리의 간선에 대한 정보는 a b 와 같이 주어지며, a는 b의 부모라는 뜻이다. 트리에 주어지는 정점은 0부터 N-1이고, 트리의 루트는 항상 0이다. 그리고, 마지막줄에 줄이려고 하는 높이 H가 주어진다. H는 1부터 N-1사이의 정수이다.

출력
첫째 줄에 트리의 높이를 H보다 작거나 같은 값으로 숌작업을 통하여 줄일 때 드는 비용의 최솟값을 출력한다.
'''
 
def redefine_levels(node:int,h:int)->None:
    global levels
    levels[node] = h
    for child in children[node]:
        redefine_levels(child,h+1)

def works(P_node:int,C_node:int)->int:
    global parents,children
    children[P_node].add(C_node)
    children[parents[C_node]].remove(C_node)
    parents[C_node] = P_node
    gap = levels[C_node] - levels[P_node] - 1
    redefine_levels(P_node,levels[P_node])
    return gap

def find_max_idx(ls:list[int])->int:
    value,idx = 0,0
    for i in range(len(ls)):
        if value < ls[i]:
            value = ls[i]
            idx = i
    return idx

def solution(H:int)->int:
    cnt = 0
    while True:
        global levels
        target = find_max_idx(levels)
        if levels[target] > H:
            gap = levels[target]-H
            C_node = target
            h = min(2,H+1)
            while (levels[C_node] > h):
                C_node = parents[C_node]

            if levels[C_node] > H:
                P_node = C_node
                for _ in range(gap+1):
                    P_node = parents[P_node]
            else:
                P_node = 0
            cnt += works(P_node,C_node)
        else:
            return cnt

N = int(input())
parents = [0]*(N)
children = [set() for _ in range(N)]
levels = [0]*(N)
for _ in range(N-1):
    a,b = map(int,input().split())
    parents[b] = a
    children[a].add(b)
redefine_levels(0,0)
H = int(input())
ans = solution(H)
print(ans)