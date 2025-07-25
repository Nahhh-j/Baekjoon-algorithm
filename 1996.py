# 지뢰 찾기

'''
문제
다들 windows에서 지원하는 지뢰 찾기 게임을 한번쯤은 해 보았을 것이다. 특히 동호는 지뢰찾기의 매니아로 알려져 있다. 지뢰 찾기 map은 N*N의 정사각형 모양으로 각 칸에는 숫자가 들어가 있거나 지뢰가 들어가 있다. 빈 칸에는 숫자 0이 들어있다고 생각하자.
map의 어떤 칸에 적혀 있는 숫자는, 그 칸과 인접해 있는 여덟 개의 칸 중에서 지뢰가 들어 있는 칸이 몇 개인지를 나타내 준다. 물론 인접한 칸이 map 내부에 있는 경우에 대해서만 생각하면 된다. 예제를 보면 더 잘 이해할 수 있을 것이다.
이번 문제는 조금 업그레이드 된 지뢰 찾기로, 한 칸에 한 개의 지뢰가 있는 것이 아니고, 한 칸에 여러 개(1 이상 9 이하)의 지뢰가 묻혀 있는 게임이다. 따라서 map의 어떤 칸에 적혀 있는 숫자는, 그 칸과 인접해 있는 여덟 개의 칸들에 들어 있는 지뢰의 총 개수가 된다.
이미 windows 지뢰찾기 같은 것을 마스터한 영식이는, map에서 지뢰에 대한 정보만이 주어졌을 때, 영식이는 map을 완성하고 싶다고 한다. N과 지뢰의 위치가 주어졌을 때, 영식이를 도와서 지뢰 찾기 map을 완성하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000)이 주어진다. 다음 N개의 줄에는 지뢰 찾기 map에 대한 정보가 주어지는데 '.' 또는 숫자로 이루어진 문자열이 들어온다. '.'는 지뢰가 없는 것이고 숫자는 지뢰가 있는 경우로 그 칸의 지뢰의 개수이다. 한 줄은 N개의 문자로 이루어져 있다.

출력
N개의 줄에 걸쳐서 완성된 지뢰 찾기 map을 출력한다. 지뢰는 '*'로 출력하며. 10 이상인 경우는 'M'(Many)으로 출력하면 된다. map은 숫자 또는 'M' 또는 '*'로만 이루어져 있어야 한다.
'''

import sys

N = int(sys.stdin.readline())

mine_map = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    row = sys.stdin.readline().rstrip()

    for j in range(N):
        col = row[j]

        if col == '.':
            continue
        
        mine_count = int(col)
        mine_map[i][j] = '*'
        
        k = 0 if i - 1 < 0 else i - 1
        l = N - 1 if N <= i + 1 else i + 1
        m = 0 if j - 1 < 0 else j - 1
        n = N - 1 if N <= j + 1 else j + 1

        for o in range(k, l + 1):
            
            for p in range(m, n + 1):
                area = mine_map[o][p]
                
                if area == '*' or area == 'M':
                    continue
                
                if 10 <= area + mine_count:
                    mine_map[o][p] = 'M'
                else:
                    mine_map[o][p] += mine_count

for map_row in mine_map:
    print(''.join(map(str, map_row)))