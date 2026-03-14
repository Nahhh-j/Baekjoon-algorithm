# 최후의 승자는 누구?

'''
문제
수많은 토너먼트를 거쳐 최종 플레이어 \(N\)명이 남아있다. 각 플레이어는 \(M\)장씩의 숫자가 적힌 카드를 가지고 있으며, 이들은 매 턴 자신이 가진 카드 중 가장 큰 카드를 두고 비교를 하는데, 그 카드들 중 가장 큰 수를 가진 플레이어가 1점을 획득한다. 그 턴에 사용된 카드는 버리기로 한다. 가장 큰 수를 가진 플레이어는 여러 명일 수 있다. \(M\)번의 경기 후 가장 많은 점수를 획득한 플레이어는 몇 번 플레이어인가?

입력
입력의 첫 줄에 플레이어의 수 \(N\)과 가진 카드 수 \(M\)이 입력 된다. \(( 2 \le N \le100, 1 \le M \le 100 )\) 그 다음 \(N\)줄에 걸쳐 각 플레이어가 들고 있는 카드에 적힌 숫자들이 입력된다. \(( 1 \le\) 카드에 적힌 숫자 \(\le 100 )\) 

출력
최종 승자의 번호를 출력한다. 플레이어의 번호는 1번부터 \(N\)번까지 입력받은 순서로 주어진다고 가정한다. 가장 많은 점수를 획득한 플레이어가 여러 명일 경우, 빈칸을 사이에 두고 플레이어들의 번호를 오름차순으로 출력한다.
'''

import sys

N, M = map(int, sys.stdin.readline().split())

player_history = dict()
maximun_card_list = [0] * M

for i in range(1, N + 1):
    card_list = sorted(map(int, sys.stdin.readline().split()), key=lambda x: -x)

    player_history[i] = {
        'score': 0,
        'card_list': card_list
    }

    for j in range(M):
        
        if maximun_card_list[j] < card_list[j]:
            maximun_card_list[j] = card_list[j]

maximun_score = 0

for player, v in player_history.items():
    
    for k in range(M):
        
        if maximun_card_list[k] != v['card_list'][k]:
            continue
        
        player_history[player]['score'] += 1

        if maximun_score < player_history[player]['score']:
            maximun_score = player_history[player]['score']

best_player_list = []

for player, v in player_history.items():
    
    if maximun_score == v['score']:
        best_player_list.append(str(player))

print(' '.join(best_player_list))