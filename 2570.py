# 비숍2

'''
문제
서양장기인 체스에는 대각선 방향으로 움직일 수 있는 비숍(bishop)이 있다. < 그림 1 >과 같이 크기가 5인 정사각형 체스판 위에 B라고 표시된 곳에 비숍이 있을 때 비숍은 대각선 방향으로 움직여 O로 표시된 칸에 있는 다른 말을 잡을 수 있다.

< 그림 1 >

그런데 체스판 위에는 비숍이 지나갈 수 없는 장애물이 놓일 수 있다. 예를 들어 < 그림 2 >와 같이 체스판 중앙에 비숍이 지나갈 수 없는 장애물이 놓이면 비숍은 장애물 오른쪽 아래 대각선 방향으로는 움직일 수 없다.

< 그림 2 >

정사각형 체스판의 한 변에 놓인 칸의 개수를 체스판의 크기라고 한다. 체스판의 크기와 체스판에 놓인 장애물들의 위치가 주어질 때, 체스판 위에 서로가 서로를 잡을 수 없도록 하면서 최대 몇 개의 비숍을 놓을 수 있는지를 구하는 프로그램을 작성하시오.
예를 들어 < 그림 2 >와 같이 체스판이 주어지면 < 그림 3 >과 같이 서로가 서로를 잡지 못하도록 하면서 최대 10개의 비숍을 놓을 수 있다.

< 그림 3 >

입력
첫째 줄에 정사각형 체스판의 크기 N이 주어진다. 둘째 줄에는 체스판 위에 놓인 장애물의 개수 M이 주어진다. N은 100이하의 자연수이고 M은 음이 아닌 정수이다. 이어 셋째 줄부터 한 줄에 하나씩 장애물의 위치가 주어진다. 장애물이 놓인 칸의 위치는 위에서부터 몇 번째 행인지와 왼쪽부터 몇 번째 열인지를 나타내는 두 개의 자연수가 차례로 주어진다.

출력
첫째 줄에 주어진 체스판 위에 놓을 수 있는 비숍의 최대 개수를 출력한다.
'''

def DFS(i):
  if visited[i]:
    return 0
  visited[i] = 1
  for j in graph[i]:
    if not match[j]:
      match[j] = i
      return 1
  for j in graph[i]:
    if DFS(match[j]):
      match[j] = i
      return 1
  return 0

N = int(input())
board = [[0]*N for i in range(N)]
for y,x in [map(int,input().split()) for i in range(int(input()))]:
  board[y-1][x-1] = -1
R = 0
for k in range(N*2):
  R += 1
  for y in range(N):
    if N>y>=0 and N>k-y>=0:
      if board[y][k-y]<0:
        R += 1
        continue
      board[y][k-y] = R
graph = [[] for i in range(R+1)]
C = 0
for k in range(-N+1,N):
  C += 1
  for y in range(N):
    if N>y>=0 and N>y-k>=0:
      if board[y][y-k]<0:
        C += 1
        continue
      graph[board[y][y-k]].append(C)
M = 0; match = [0]*(C+1)
for r in range(1,R+1):
  visited = [0]*(R+1)
  M += DFS(r)
print(M)