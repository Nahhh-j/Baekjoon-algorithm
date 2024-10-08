# 히스토그램

'''
문제
히스토그램에 대해서 알고 있는가? 히스토그램은 아래와 같은 막대그래프를 말한다.

각 칸의 간격은 일정하고, 높이는 어떤 정수로 주어진다. 위 그림의 경우 높이가 각각 2 1 4 5 1 3 3이다.
이러한 히스토그램의 내부에 가장 넓이가 큰 직사각형을 그리려고 한다. 아래 그림의 빗금 친 부분이 그 예이다. 이 직사각형의 밑변은 항상 히스토그램의 아랫변에 평행하게 그려져야 한다.

주어진 히스토그램에 대해, 가장 큰 직사각형의 넓이를 구하는 프로그램을 작성하시오.

입력
첫 행에는 N (1 ≤ N ≤ 100,000) 이 주어진다. N은 히스토그램의 가로 칸의 수이다. 다음 N 행에 걸쳐 각 칸의 높이가 왼쪽에서부터 차례대로 주어진다. 각 칸의 높이는 1,000,000,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 가장 큰 직사각형의 넓이를 출력한다. 이 값은 20억을 넘지 않는다.
'''

n = int(input())
result = 0
s = []
data = []

for _ in range(n):
    data.append(int(input()))

for i in range(n):
    while s and data[s[-1]] > data[i]:
        height = data[s[-1]]
        s.pop()
        width = i
        if s:
            width = (i - s[-1] - 1)
        result = max(result, width * height)
    s.append(i)

while s:
    height = data[s[-1]]
    s.pop()
    width = n
    if s:
        width = (n - s[-1] - 1)
    result = max(result, width * height)

print(result)