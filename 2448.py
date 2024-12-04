# 별 찍기 - 11

'''
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N이 주어진다. N은 항상 3×2k 수이다. (3, 6, 12, 24, 48, ...) (0 ≤ k ≤ 10, k는 정수)

출력
첫째 줄부터 N번째 줄까지 별을 출력한다.
'''

import sys
input = sys.stdin.readline

n = int(input())

stars = [[' ']*2*n for _ in range(n)]

def recursion(i, j, size):
    if size == 3:
        stars[i][j] = '*'
        stars[i + 1][j - 1] = stars[i + 1][j + 1] = "*"
        for k in range(-2, 3):
            stars[i + 2][j - k] = "*"
    
    else:
        newSize = size//2
        recursion(i, j, newSize)
        recursion(i + newSize, j - newSize, newSize)
        recursion(i + newSize, j + newSize, newSize)

recursion(0, n - 1, n)
for star in stars:
    print("".join(star))