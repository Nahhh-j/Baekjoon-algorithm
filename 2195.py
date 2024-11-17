# 문자열 복사

'''
문제
어떤 원본 문자열 S가 주어졌을 때, 이 문자열의 부분을 복사하여 P라는 새로운 문자열을 만들려고 한다. 복사를 할 때에는 copy(s, p) 이라는 함수를 이용하는데, 이는 S의 s번 문자부터 p개의 문자를 P에 복사해서 붙인다는 의미이다.
예를 들어 S="abaabba", P="aaabbbabbbaaa"인 경우를 생각해 보자. 이때는 copy(3, 2), copy(4, 3), copy(2, 2), copy(5, 2), copy(2, 3), copy(1, 1) 를 수행하여 P를 만들 수 있다. 각 단계별로 P는 "aa", "aaabb", "aaabbba", …와 같이 변하게 된다.
이와 같은 copy 연산을 이용하여 S에서 P를 만들려고 하는데, 이때 가능하면 copy 함수를 조금 사용하려고 한다.
S와 P가 주어졌을 때, 필요한 copy 함수의 최소 사용횟수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 S, 둘째 줄에 P가 주어진다. S와 P는 영어 대소문자와 숫자로만 되어 있다. S의 길이는 1,000을 넘지 않으며, P의 길이는 1,000을 넘지 않는다. copy함수만을 이용하여 S에서 P를 만들어낼 수 없는 경우는 입력으로 주어지지 않는다고 가정하자. 각 문자열은 최소한 한 개의 문자로 이루어져 있다.

출력
첫째 줄에 copy 함수의 최소 사용횟수를 출력한다.
'''

import sys
input = sys.stdin.readline

S = input().strip()
P = input().strip()
index_p = 0
ans = 0

while index_p < len(P):
    max_value, temp, index_s = 0, 0, 0
    while index_s < len(S) and index_p + temp < len(P):
        if P[index_p + temp] == S[index_s]:
            temp += 1
            max_value = max(max_value, temp)
        else:
            temp = 0
        index_s += 1
    index_p += max_value
    ans += 1
print(ans)