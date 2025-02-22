# 색종이 - 3

'''
문제
가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 도화지에서 검은색 직사각형을 잘라내려고 한다. 직사각형 또한 그 변이 도화지의 변과 평행하도록 잘라내어야 한다.
예를 들어 흰색 도화지 위에 세 장의 검은색 색종이를 <그림 1>과 같은 모양으로 붙였다. <그림 1>에 표시된 대로 검은색 직사각형을 잘라내면 그 넓이는 22×5=110이 된다.

<그림 1>

<그림 2>

반면 <그림 2>에 표시된 대로 검은색 직사각형을 잘라내면 그 넓이는 8×15=120이 된다.
검은색 색종이의 수와 각 색종이를 붙인 위치가 주어질 때 잘라낼 수 있는 검은색 직사각형의 최대 넓이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 색종이의 수가 주어진다. 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 색종이의 수는 100이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다.

출력
첫째 줄에 잘라낼 수 있는 검은색 직사각형의 최대 넓이를 출력한다.
'''

import sys
input = sys.stdin.readline

def find_rectangle(x,y):

    max_size = 100
    for i in range(100):
        if x+i >100:
            break
        for j in range(100):
            if y + j > 100:
                break
            max_size = max(max_size,calculate_area(x,y,x+i,y+j))
    return max_size

def calculate_area(x,y,h,w):
    cnt = 0
    for i in range(x,h+1):
        for j in  range(y,w+1):
            if not paper[i][j]:
                return 0
            else:
                cnt += 1
    return cnt
        


n = int(input())
paper = [[0]*101 for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            paper[i][j] = 1

max_size = 100
for i in range(100):
    for j in range(100):
        if paper[i][j]==1:
            max_size = max(max_size,find_rectangle(i,j))
print(max_size)