# 마법의 문자열

'''
문제
L개의 문자로 이루어진 문자열 T가 있다. T(i)는 T를 i (0 ≤ i < L)번째 문자부터 시작하게 부터 시작하게 원형 이동한 것이고, 길이는 T의 길이와 같다. 즉, 0 ≤ j < L을 만족하는 모든 j에 대해서, T(i)의 j번째 문자는 T의 (i+j)%L 번째 문자와 같다. T(i)와 T가 같은 문자열이 되는 i가 정확히 K개 있다면, T를 마법의 문자열이라고 한다.
N개의 문자열 S1, S2, ..., SN이 주어진다. 크기가 N인 모든 순열 p = (p0, p1, ..., pN-1) 마다 새로운 문자열을 Sp0 + Sp1 + ... + SpN-1을 하나 정의할 수 있다. 새로운 문자열이 마법의 단어가 되는 순열의 개수를 구해보자.

입력
첫째 줄에 단어의 개수 N이 주어진다. N은 8보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 각 단어가 주어진다. 단어의 길이는 최대 20이다. 단어는 알파벳 대문자로만 이루어져 있다. 마지막 줄에 K가 주어진다. K는 200보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.
'''

import itertools
n = int(input())
words = []
for _ in range(n):
    words.append(input())
k = int(input())

def kmp(pattern, all_string):
    table = [0 for _ in range(len(pattern))]
    i = 0
    for j in range(1, len(pattern)):
        while i>0 and pattern[i]!=pattern[j]:
            i = table[i-1]

        if pattern[i]==pattern[j]:
            i += 1
            table[j] = i

    count = -1
    i = 0
    for j in range(len(all_string)):
        while i > 0 and pattern[i] != all_string[j]:
            i = table[i-1]

        if pattern[i] == all_string[j]:
            i += 1
            if i == len(pattern):
                count += 1
                i = table[i-1]
    return count == k

answer = 0
permutations = list(itertools.permutations(words, n))
for perm in permutations:
    a = ''.join(list(perm))a
    answer += kmp(a, a+a)
print(answer)