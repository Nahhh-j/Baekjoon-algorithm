# 컨닝

'''
문제
최백준은 서강대학교에서 “컨닝의 기술”이라는 과목을 가르치고 있다. 이 과목은 상당히 까다롭기로 정평이 나있기 때문에, 몇몇 학생들은 시험을 보는 도중에 다른 사람의 답지를 베끼려 한다.
시험은 N행, M열 크기의 직사각형 교실에서 이루어진다. 교실은 1×1 크기의 단위 정사각형으로 이루어져 있는데, 각 단위 정사각형은 자리 하나를 의미한다.
최백준은 컨닝을 방지하기 위해서 다음과 같은 전략을 세웠다. 모든 학생은 자신의 왼쪽, 오른쪽, 왼쪽 대각선 위, 오른쪽 대각선 위, 이렇게 총 네 자리에 앉아있는 친구의 답지를 항상 베낀다고 가정한다. 따라서, 자리 배치는 모든 학생이 컨닝을 할 수 없도록 배치되어야 한다.

위의 그림을 보자. A, C, D 혹은 E에 다른 학생을 앉히는 것은 좋은 생각이 아니다. 그 이유는 이미 앉아있는 학생이 그들의 답안지를 베낄 우려가 있기 때문이다. 하지만, B에 다른 학생을 앉힌다면, 두 학생은 서로의 답지를 베낄 수 없어 컨닝의 우려가 없다.
위와 같이 컨닝이 불가능하도록 자리를 배치 하려는 최백준의 행동에 분노한 일부 학생들이 교실의 책상을 부숴버렸기 때문에, 일부 자리에는 학생이 앉을 수 없다.
최백준은 교실의 모양이 주어졌을 때, 이 곳에서 아무도 컨닝을 할 수 없도록 학생을 배치하였을 경우에 교실에 배치할 수 있는 최대 학생 수가 몇 명인지 궁금해졌다. 최백준을 위해 이를 구하는 프로그램을 작성하라.

입력
입력의 첫 줄에는 테스트케이스의 개수 C가 주어진다. 각각의 테스트 케이스는 아래와 같이 두 부분으로 이루어진다.
첫 번째 부분에서는 교실의 세로길이 N과 가로길이 M이 한 줄에 주어진다. (1 ≤ M ≤ 10, 1 ≤ N ≤ 10)
두 번째 부분에서는 정확하게 N줄이 주어진다. 그리고 각 줄은 M개의 문자로 이루어져있다. 모든 문자는 ‘.’(앉을 수 있는 자리) 또는 ‘x’(앉을 수 없는 자리, 소문자)로 구성된다.

출력
각각의 테스트 케이스에 대해 그 교실에서 시험을 볼 수 있는 최대 학생의 수를 출력한다.
'''

import sys; input = sys.stdin.readline

def bip_match(n, m):
    for nn, mm in [(n, m - 1), (n, m + 1), (n - 1, m - 1), (n - 1, m + 1), (n + 1, m - 1), (n + 1, m + 1)]:
        if 0 <= nn < N and 0 <= mm < M and not visited[nn][mm] and seat[nn][mm]:
            visited[nn][mm] = True
            if connect[nn][mm] == [-1, -1] or bip_match(connect[nn][mm][0], connect[nn][mm][1]):
                connect[nn][mm] = [n, m]       
                return True
    return False

for _ in range(int(input())):
    N, M = map(int, input().split())
    matrix = [input().strip() for _ in range(N)]
    
    seat = [[False] * M for _ in range(N)]
    answer = 0
    for n in range(N):
        for m in range(M):
            if matrix[n][m] == '.':
                seat[n][m] = True
                answer += 1
                
    connect = [[[-1] * 2 for _ in range(M)] for __ in range(N)]
    for n in range(N):
        for m in range(0, M, 2):
            if seat[n][m]:
                visited = [[False] * M for _ in range(N)]
                if bip_match(n, m):
                    answer -= 1
                    
    print(answer)