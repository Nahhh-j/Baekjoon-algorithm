# 부분합

'''
문제
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

출력
첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.
'''

N, S = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
sum_ = arr[0]
ans = 100001

while True:
    if sum_ < S:
        end += 1
        if end == N: break
        sum_ += arr[end]
    else:
        sum_ -= arr[start]
        ans = min(ans, end - start + 1)
        start += 1
        
print(ans if ans != 100001 else 0)