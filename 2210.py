# 숫자판 점프

'''
문제
5×5 크기의 숫자판이 있다. 각각의 칸에는 숫자(digit, 0부터 9까지)가 적혀 있다. 이 숫자판의 임의의 위치에서 시작해서, 인접해 있는 네 방향으로 다섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례로 붙이면 6자리의 수가 된다. 이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며, 0으로 시작하는 000123과 같은 수로 만들 수 있다.
숫자판이 주어졌을 때, 만들 수 있는 서로 다른 여섯 자리의 수들의 개수를 구하는 프로그램을 작성하시오.

입력
다섯 개의 줄에 다섯 개의 정수로 숫자판이 주어진다.

출력
첫째 줄에 만들 수 있는 수들의 개수를 출력한다.
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

grid = [list(map(int, input().split())) for _ in range(5)]
num_set = set()

def dfs(i, j, num):
  num += str(grid[i][j])
  if len(num) == 6:
    num_set.add(num)
    return
  for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
    x, y = i + dx, j + dy
    if 0 <= x < 5 and 0 <= y < 5:
      dfs(x, y, num)

for i in range(5):
  for j in range(5):
    dfs(i, j, '')

print(len(num_set))