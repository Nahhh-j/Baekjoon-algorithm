# 인간-컴퓨터 상호작용

'''
문제
승재는 인간-컴퓨터 상호작용에서 생체공학 설계를 공부하다가 키보드 자판이 실용적인지 궁금해졌다. 이를 알아보기 위해 승재는 다음과 같은 생각을 했다. 
'문자열에서 특정 알파벳이 몇 번 나타나는지 알아봐서 자주 나타나는 알파벳이 중지나 검지 위치에 오는 알파벳인지 확인하면 실용적인지 확인할 수 있을 것이다.'
승재를 도와 특정 문자열 S, 특정 알파벳 alpha와 문자열의 구간 [l,r]이 주어지면 S의 l번째 문자부터 r번째 문자 사이에 \alpha가 몇 번 나타나는지 구하는 프로그램을 작성하여라. 승재는 문자열의 문자는 0번째부터 세며, l번째와 r번째 문자를 포함해서 생각한다. 주의할 점은 승재는 호기심이 많기에 (통계적으로 크게 무의미하지만) 같은 문자열을 두고 질문을 q번 할 것이다.

입력
첫 줄에 문자열 S가 주어진다. 문자열 길이는 200,000자 이하이며 알파벳 소문자로만 구성되었다. 두 번째 줄에는 질문의 수 q가 주어지며, 문제의 수는 1\leq q\leq 200,000을 만족한다. 세 번째 줄부터 (q+2)번째 줄에는 질문이 주어진다. 각 질문은 알파벳 소문자 alpha_i와 leq l_i\leq r_i<|S|를 만족하는 정수 l_i,r_i가 공백으로 구분되어 주어진다.

출력
각 질문마다 줄을 구분해 순서대로 답변한다. i번째 줄에 S의 l_i번째 문자부터 r_i번째 문자 사이에 \alpha_i가 나타나는 횟수를 출력한다.
'''

import sys

s = sys.stdin.readline().rstrip()
count = {0 : [0] * 26}

q = int(sys.stdin.readline().rstrip())
for i, ch in enumerate(s):
    count[i + 1] = count[len(count) - 1][:]
    count[i + 1][ord(ch) - 97] += 1

for _ in range(q):
    alpha, l, r = sys.stdin.readline().rstrip().split()
    answer = count[int(r) + 1][ord(alpha) - 97] - count[int(l)][ord(alpha) - 97]
    print(answer)