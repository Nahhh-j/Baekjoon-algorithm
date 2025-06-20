# 도미노 찾기

'''
문제
도미노의 크기는 1×2이고, 크기가 1×1인 칸으로 나누어져 있다. 칸은 수를 나타내며, 위와 같이 총 28가지가 있다.
크기가 8×7인 격자가 있고, 격자의 각 칸에는 정수가 하나씩 들어있다. 위의 도미노를 이용해 문제의 격자와 같은 상태를 만드는 방법의 수를 구해보자.
격자의 칸에 적힌 수는 도미노의 칸이 의미하는 수와 같아야 한다. 도미노는 회전할 수 있으며, 같은 도미노를 여러 번 사용하면 안된다.

입력
총 8개의 줄에 격자의 상태가 주어진다. 격자에는 0부터 6까지의 수만 존재한다.

출력
첫째 줄에 경우의 수를 출력한다.
'''

from sys import stdin

input = stdin.readline

board = [list(map(int, list(input().strip()))) for _ in range(8)]
used = [[False]*7 for _ in range(7)]
visited = [[False]*7 for _ in range(8)]

def solv():
    print(go(0,0))

def go(x,y):
    global used,visited
    if x == 8:
        return 1
    count = 0
    nnx = x
    nny = y + 1
    if nny == 7:
        nnx = x + 1
        nny = 0
    if visited[x][y]:
        return go(nnx,nny)
    else:
        now = board[x][y]
        visited[x][y] = True
        for dx,dy in ((0,1),(1,0)):
            nx = x + dx
            ny = y + dy

            if boundray_validator(nx,ny):
                nxt = board[nx][ny]

                if not used[now][nxt] and not visited[nx][ny]:
                    used[now][nxt] = used[nxt][now] = True
                    visited[nx][ny] = True
                    count += go(nnx,nny)
                    visited[nx][ny] = False
                    used[now][nxt] = used[nxt][now] = False
        visited[x][y] = False
        return count

def boundray_validator(x,y):
    if x >= 8 or y >= 7:
        return False
    return True
solv()