# 거울

'''
문제
세로 N, 가로 M 크기의 상자가 있다. 이 상자 안에는 몇 개의 거울이 들어 있다. 상자를 위에서 봤을 때, 거울은 한 칸 안에 대각선 모양으로 들어있다고 한다. 또, 상자의 테두리를 따라서 칸마다 구멍이 뚫려 있다. 편의상 구멍은 왼쪽 위에 뚫려있는 것부터 시계 반대 방향으로 1, 2, …, 2N+2M 의 번호가 붙어 있다. 예를 들어 다음과 같은 경우를 보자.

이제 이 상자에 뚫려있는 구멍으로 빛을 쏜다고 생각해보자. 1번 구멍으로 쏠 경우에는 (1, 2)의 위치에 있는 거울에 반사되어 9번 구멍으로 빛이 가게 된다. 또, 2번 구멍으로 빛을 쏠 경우에는 (2, 2)의 위치에 있는 거울과 (1, 2)에 있는 거울에 차례로 반사되어 7번 구멍으로 빛이 나가게 된다.
이와 같이 상자의 모양이 주어졌을 때, 각 구멍으로 쏜 빛이 나가게 되는 구멍을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N, M (1 ≤ N, M ≤ 1,000)이 주어진다. 다음 N개의 줄에는 M개의 수로 상자의 모양이 주어진다. 거울이 있는 위치는 1로, 거울이 없는 위치는 0으로 주어진다. 거울은 / 모양으로만 놓일 수 있다고 하자.

출력
첫째 줄부터 차례로 1번 구멍으로 쏜 빛이 나가는 구멍의 번호, 2번 구멍으로 쏜 빛이 나가는 구멍의 번호, …, 2N+2M번 구멍으로 쏜 빛이 나가는 구멍의 번호를 출력한다.
'''

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
mirrors = []
for _ in range(n):
mirrors.append(list(map(int, input().split())))
ans = [0 for _ in range(2*n+2*m)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def move(i, x, y, d):
global n, m
while 0 <= x < n and 0 <= y < m:
if mirrors[x][y] == 0:
x += dx[d]
y += dy[d]
else:
if d == 0 or d == 3:
if d == 0: d = 3
else: d = 0
else:
if d == 1: d = 2
else: d = 1
x += dx[d]
y += dy[d]
if y < 0:
ans[i] = x+1
elif x >= n:
ans[i] = n+y+1
elif y >= m:
ans[i] = n+m+(n-x)
elif x < 0:
ans[i] = 2*n+m+(m-y)
for i in range(2*n+2*m):
if 0 <= i < n:
x, y, d = i, 0, 0
move(i, x, y, d)
elif n <= i < n+m:
x, y, d = n-1, i-n, 3
move(i, x, y, d)
elif n+m <= i < 2*n+m:
x, y, d = (n-1)-(i-(n+m)), m-1, 2
move(i, x, y, d)
else:
x, y, d = 0, (2*m+2*n-1)-i, 1
move(i, x, y, d)
print(*ans)