# 이전 수열은 어떤 수열일까

'''
문제
길이 n의 수열 S가 주어진다. S는 1부터 n까지의 n개 정수를 임의 순서로 늘어놓은 것이다. 다음 조건을 만족하는 수열들 중 오름차순으로 가장 앞에 오는 수열이 무엇인지 궁금하다. 이를 알아내는 프로그램을 작성하라.

1부터 n까지의 정수를 임의 순서로 늘어놓은 수열이다.
이 수열의 i번째 수 와 원래 수열 S의 i번째 수 의 차는 1을 넘을 수 없다.

입력
첫 줄에 수열의 길이 n이 주어진다. (3 ≤ n ≤ 50,000) 이후 n개의 줄에 수열을 이루는 수가 한 개씩 차례대로 주어진다.

출력
n개의 줄에 걸쳐, 조건을 만족하는 수열 중 오름차순으로 가장 앞에 오는 수열을 출력한다.
'''

n = int(input())
S = [int(input()) for _ in range(n)]

used = [False] * (n + 1)  
result = []

for i in range(n):
    candidates = []
    for d in [-1, 0, 1]:
        val = S[i] + d
        if 1 <= val <= n and not used[val]:
            candidates.append(val)

    candidates.sort()
    selected = candidates[0]
    result.append(selected)
    used[selected] = True

for num in result:
    print(num)