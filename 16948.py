# 데스 나이트

'''
문제
게임을 좋아하는 큐브러버는 체스에서 사용할 새로운 말 "데스 나이트"를 만들었다. 데스 나이트가 있는 곳이 (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.
크기가 N×N인 체스판과 두 칸 (r1, c1), (r2, c2)가 주어진다. 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 구해보자. 체스판의 행과 열은 0번부터 시작한다.
데스 나이트는 체스판 밖으로 벗어날 수 없다.

입력
첫째 줄에 체스판의 크기 N(5 ≤ N ≤ 200)이 주어진다. 둘째 줄에 r1, c1, r2, c2가 주어진다.

출력
첫째 줄에 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.
'''

import sys
from collections import deque

input=sys.stdin.readline

dx=[-2,-2,0,0,2,2]
dy=[-1,1,-2,2,-1,1]

N=int(input())
r1,c1,r2,c2=map(int,input().split())

visited=[[-1]*N for _ in range(N)]

def bfs(r,c):
    global visited
    q=deque()
    q.append((r,c))
    visited[r][c]=0
    while q:
        now=q.popleft()
        for i in range(6):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if visited[nx][ny]!=-1:
                continue
            q.append((nx,ny))
            visited[nx][ny]=visited[now[0]][now[1]]+1

bfs(r1,c1)
print(visited[r2][c2])  