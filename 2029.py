# 성냥

'''
문제
24개의 성냥이 아래 그림과 같이 3x3 크기의 격자에 배치되어 있다. 두 개의 연속된 '-'는 가로로 놓은 성냥을 나타내고, 두 개의 연속된 '|'는 세로로 놓은 성냥을 나타낸다.

+--+--+--+
|..|..|..|
|..|..|..|
+--+--+--+
|..|..|..|
|..|..|..|
+--+--+--+
|..|..|..|
|..|..|..|
+--+--+--+
위 그림에서 검정색으로 표시된 부분이 바로 24개의 성냥을 나타낸다. '+'는 두 개 이상의 성냥이 만날 수 있는 부분들을 나타낸 것으로, 위의 그림과 같이 총 16개가 위치하고 있다. 그 외의 칸은 배경으로, 모두 '.'으로 나타낸다.

위의 그림과 같이 24개의 성냥을 모두 배치하면, 찾을 수 있는 정사각형이 총 14개라는 것을 알 수 있다. (9개+4개+1개) 하지만 몇 개의 성냥을 제거하면, 찾을 수 있는 정사각형의 개수가 줄어들기도 한다. 예를 들어 아래와 같은 경우는 24개 중 5개의 성냥을 제거하여 14개 중 4개의 정사각형만을 남겨 둔 경우이다.

+--+--+--+
|..|..|..|
|..|..|..|
+--+--+..+
|.....|..|
|.....|..|
+--+--+..+
|........|
|........|
+--+--+--+
이처럼 성냥의 배치를 알면, 이 배치가 24개 중 A개의 성냥을 제거하여 14개 중 B개의 정사각형만을 남겨 둔 배치라는 것을 구할 수 있다. (1≤A≤24, 1≤B≤14인 정수) 성냥의 배치가 주어졌을 때, A와 B를 구하는 프로그램을 작성하시오.

입력
첫째 줄부터 열 개의 줄에 걸쳐 성냥의 배치가 위의 예제와 같은 형식으로 들어온다. 각 줄에는 10개의 문자가 있다. 입력은 '-', '|', '+', '.'만으로 이루어져 있으며, 항상 위에 주어진 형식에 맞는 배치만이 입력으로 주어진다.

출력
첫째 줄에 A와 B를 빈 칸을 사이에 두고 출력한다.
'''

grid = [input() for _ in range(10)]

total_matches = 0

for i in range(0, 10, 3):
    for j in range(1, 9, 3):
        if grid[i][j] == '-' and grid[i][j+1] == '-':
            total_matches += 1

for i in range(1, 9, 3):
    for j in range(0, 10, 3):
        if grid[i][j] == '|' and grid[i+1][j] == '|':
            total_matches += 1

square_count = 0

for size in range(1, 4):
    for row in range(0, 3 - size + 1):
        for col in range(0, 3 - size + 1):
            ok = True

            for k in range(size):
                i = row * 3
                j = col * 3 + 1 + 3 * k
                if not (grid[i][j] == '-' and grid[i][j+1] == '-'):
                    ok = False

            for k in range(size):
                i = (row + size) * 3
                j = col * 3 + 1 + 3 * k
                if not (grid[i][j] == '-' and grid[i][j+1] == '-'):
                    ok = False

            for k in range(size):
                i = row * 3 + 1 + 3 * k
                j = col * 3
                if not (grid[i][j] == '|' and grid[i+1][j] == '|'):
                    ok = False

            for k in range(size):
                i = row * 3 + 1 + 3 * k
                j = (col + size) * 3
                if not (grid[i][j] == '|' and grid[i+1][j] == '|'):
                    ok = False

            if ok:
                square_count += 1

print(24 - total_matches, square_count)