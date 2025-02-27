# Fibonacci Game

'''
문제
당신은 N(2 ≤ N ≤ 1,000,000)개의 구슬을 가지고 다음과 같은 게임을 하려고 한다. 게임은 두 사람이 번갈아 가면서 진행하며, 1번 사람이 몇 개의 구슬을 가져가는 것으로 게임이 시작된다. 1번 사람이 처음에 구슬을 가져갈 때는 몇 개라도 가져갈 수 있지만 N개의 구슬을 다 가져가서는 안 된다. 그 후에 구슬을 가져갈 때는, 상대편이 바로 전에 가져간 개수의 2배 이하를 가져갈 수 있다. 즉, 상대편이 1개를 가져갔다면, 당신은 1개, 또는 2개를 가져갈 수 있는 것이다. 이런 식으로 게임을 진행하여, 마지막으로 구슬을 가져간 사람이 이기게 된다.
예를 들어, N = 3인 경우를 보자. 1번 사람이 몇 개를 가져가도 2번 사람이 남아있는 구슬을 다 가져갈 수 있다. 반면에 N=4인 경우에는, 1번 사람이 1개를 가져가면 이기게 된다.
1번 사람의 입장이 되어, 처음에 몇 개의 구슬을 가져갈 것인지를 결정하는 프로그램을 작성하시오. 만약 가능한 경우가 여러 가지 존재한다면, 더 적은 수의 구슬을 가져가는 것으로 한다. 만약 몇 개를 가져가도 지게 된다면, -1을 출력한다.

입력
첫째 줄에 정수 N이 주어진다.

출력
가져갈 구슬의 개수, 또는 -1을 출력한다.
'''

class Solution:

    def find_max(self, grid, x, y):
        max_element = 0
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                max_element = max(max_element, grid[i][j])
        
        return max_element

    def largestLocal(self, grid):
        N = len(grid)
        
        max_local = [[0] * (N - 2) for _ in range(N - 2)]
        for i in range(N - 2):
            for j in range(N - 2):
                max_local[i][j] = self.find_max(grid, i, j)
        
        return max_local