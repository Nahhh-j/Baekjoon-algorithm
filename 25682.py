# 체스판 다시 칠하기 2

'''
문제
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 K×K 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 K×K 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 K×K 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N, M, K가 주어진다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 잘라낸 K×K 보드를 체스판으로 만들기 위해 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
'''

import sys
input = sys.stdin.readline
sys.maxsize

def minimal_board(color):
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            if (i + j) % 2 == 0: 
                value = board[i][j] != color
            else:
                value = board[i][j] == color
            prefix_sum[i + 1][j + 1] = prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j] + value
    
    count = sys.maxsize
    for i in range(1, N - K + 2):
        for j in range(1, M - K + 2):
            count = min(count, prefix_sum[i + K - 1][j + K - 1] - prefix_sum[i + K - 1][j - 1] - prefix_sum[i - 1][j + K - 1] + prefix_sum[i - 1][j - 1])
    return count

N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]
print(min(minimal_board('B'), minimal_board('W')))