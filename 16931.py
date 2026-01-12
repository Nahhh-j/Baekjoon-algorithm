# 겉넓이 구하기

'''
문제
크기가 N×M인 종이가 있고, 종이는 1×1크기의 칸으로 나누어져 있다. 이 종이의 각 칸 위에 1×1×1 크기의 정육면체를 놓아 3차원 도형을 만들었다.
종이의 각 칸에 놓인 정육면체의 개수가 주어졌을 때, 이 도형의 겉넓이를 구하는 프로그램을 작성하시오.
위의 그림은 3×3 크기의 종이 위에 정육면체를 놓은 것이고, 겉넓이는 60이다.

입력
첫째 줄에 종이의 크기 N, M이 주어진다. 둘째 줄부터 N개의 줄에는 종이의 각 칸에 놓인 정육면체의 수가 주어진다.

출력
첫째 줄에 도형의 겉넓이를 출력한다.

제한
1 ≤ N, M ≤ 100
1 ≤ 종이의 한 칸에 놓인 정육면체의 수 ≤ 100
'''

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

up = N * M

left = 0
for i in range(N):
    for j in range(M):
        if j == 0:
            left += arr[i][j]
        else:
            if arr[i][j-1] < arr[i][j]:
                left += arr[i][j] - arr[i][j-1]

front = 0
for j in range(M):
    for i in range(N):
        if i == 0:
            front += arr[i][j]
        else:
            if arr[i-1][j] < arr[i][j]:
                front += arr[i][j] - arr[i-1][j]
        
answer = 2 * (up + left + front)
print(answer)