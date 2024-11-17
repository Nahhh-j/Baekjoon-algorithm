# LCD Test

'''
문제
지민이는 새로운 컴퓨터를 샀다. 하지만 새로운 컴퓨터에 사은품으로 온 LC-디스플레이 모니터가 잘 안나오는 것이다. 지민이의 친한 친구인 지환이는 지민이의 새로운 모니터를 위해 테스트 할 수 있는 프로그램을 만들기로 하였다.

입력
첫째 줄에 두 개의 정수 s와 n이 들어온다. (1 ≤ s ≤ 10, 0 ≤ n ≤ 9,999,999,999)이다. n은 LCD 모니터에 나타내야 할 수 이며, s는 크기이다.

출력
길이가 s인 '-'와 '|'를 이용해서 출력해야 한다. 각 숫자는 모두 s+2의 가로와 2s+3의 세로로 이루어 진다. 나머지는 공백으로 채워야 한다. 각 숫자의 사이에는 공백이 한 칸 있어야 한다.
'''

import sys
input = sys.stdin.readline
def getInts(): return map(int, input().split())


h, v = '-', '|'
s, n = input().split()
s = int(s)


def construct_segment(n):
    lcd = [[' ']*(s+2) for _ in range(2*s + 3)]
    for i in range(1, s+1):
        if n in '02356789':
            lcd[0][i] = h
        if n in '01234789':
            lcd[i][-1] = v
        if n in '013456789':
            lcd[s+1+i][-1] = v
        if n in '0235689':
            lcd[2*s + 2][i] = h
        if n in '0268':
            lcd[s+1+i][0] = v
        if n in '045689':
            lcd[i][0] = v
        if n in '2345689':
            lcd[s+1][i] = h
    return lcd


display = [construct_segment(i) for i in n]

for line in zip(*display):
    for r in line:
        print(''.join(r), end=' ')
    print()