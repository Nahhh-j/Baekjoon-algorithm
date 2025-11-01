# 회사 문화 4

'''
문제
영선회사에는 매우 좋은 문화가 있는데, 바로 상사가 직속 부하를 칭찬하면 그 부하가 부하의 직속 부하를 연쇄적으로 칭찬하는 내리 칭찬이 있다. 즉, 상사가 한 직속 부하를 칭찬하면 그 부하의 모든 부하들이 칭찬을 받는다.
이러한 내리 칭찬은 회사에 가장 큰 장점이 되었고, 사장 영선이는 이 장점을 이용하기 위하여 근무 시간 도중 도중 칭찬의 방향을 바꿀 것이다. 가장 처음에는 부하 직원 방향이다.
칭찬에 대한 정보는 실시간으로 주어진다.
입력으로 아래와 같은 쿼리가 주어질 것이다.

1 i w: i번째 직원이 직속 상사로부터 w만큼 칭찬을 받는다. 만약, 칭찬의 방향이 상사 방향이라면, i번째 직원이 직속 부하 중 한 명으로부터 w만큼 칭찬을 받는다. (1 ≤ i ≤ n, 1 ≤ w ≤ 1,000)
2 i: i번째 직원이 칭찬을 받은 정도를 출력한다.
3: 칭찬의 방향이 부하 직원 방향이면 상사 방향으로, 상사 방향이면 부하 직원 방향으로 바꾼다.
직속 상사와 직속 부하관계에 대해 주어지고, 쿼리가 주어졌을 때 2번 쿼리에 따라 출력하시오.

입력
첫째 줄에는 회사의 직원 수 n명, 쿼리의 개수 m이 주어진다. 직원은 1번부터 n번까지 번호가 매겨져 있다. (2 ≤ n, m ≤ 100,000)
둘째 줄에는 직원 n명의 직속 상사의 번호가 주어진다. 직속 상사의 번호는 자신의 번호보다 작으며, 최종적으로 1번이 사장이다. 1번의 경우, 상사가 없으므로 -1이 입력된다.
다음 m줄에는 쿼리가 한 줄에 하나씩 주어진다.

출력
2번 쿼리가 주어질 때마다, 알맞게 출력하시오.
'''

import sys
sys.setrecursionlimit(2 * 10**5)
input = sys.stdin.readline

class Fenwick:
    def __init__(s, n): s.t = [0]*(n+1)
    def u(s, i, w):
        while i < len(s.t): s.t[i] += w; i += i & -i
    def q(s, i):
        r=0
        while i>0: r+=s.t[i]; i-=i&-i
        return r
    def ru(s, l, r, w): s.u(l,w); s.u(r+1,-w)

n,m=map(int,input().split())
p=list(map(int,input().split()))
g=[[] for _ in range(n+1)]
for i in range(2,n+1): g[p[i-1]].append(i)

In,Out=[0]*(n+1),[0]*(n+1)
t=0
def dfs(v):
    global t
    t+=1; In[v]=t
    for x in g[v]: dfs(x)
    Out[v]=t
dfs(1)

D,U=Fenwick(n),Fenwick(n)
d=0
for _ in range(m):
    q=list(map(int,input().split()))
    if q[0]==1:
        _,i,w=q
        (D if d==0 else U).ru(In[i],Out[i] if d==0 else In[i],w)
    elif q[0]==2:
        print(D.q(In[q[1]])+U.q(In[q[1]]))
    else:
        d^=1