# 님 게임 2

'''
문제
koosaga와 cubelover가 님 게임을 하고 있다. 님 게임은 돌을 차곡 차곡 위로 쌓아올린 돌 더미 k개를 이용한다. 각각의 돌 더미에는 한 개 이상의 돌이 있다. 두 사람은 서로 턴을 번갈아가면서 님 게임을 진행한다. 각 사람의 턴이 되면, 돌이 있는 돌 더미를 하나 선택하고, 그 돌 더미에서 돌을 하나 이상 제거한다. 전체 돌 더미에서 마지막 돌을 제거하는 사람이 게임을 이기게 된다. 
게임은 koosaga가 먼저 시작한다. 두 사람이 최적의 방법으로 게임을 진행했을 때, 이기는 사람을 출력한다.

입력
첫째 줄에 돌 더미의 개수 N (1 ≤ N ≤ 100)이 주어진다.
둘째 줄에는 각 돌 더미에 쌓여있는 돌의 개수 Pi (1 ≤ Pi ≤ 109)가 주어진다.

출력
koosaga가 이기는 경우에는 'koosaga'를, cubelover가 이기는 경우에는 'cubelover'를 출력한다.
'''

import sys

n = int(sys.stdin.readline())
piles = list(map(int, sys.stdin.readline().split()))

nim = 0
for p in piles:
    nim ^= p

print("koosaga" if nim != 0 else "cubelover")