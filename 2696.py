# 중앙값 구하기

'''
문제
어떤 수열을 읽고, 홀수번째 수를 읽을 때 마다, 지금까지 입력받은 값의 중앙값을 출력하는 프로그램을 작성하시오.
예를 들어, 수열이 1, 5, 4, 3, 2 이면, 홀수번째 수는 1번째 수, 3번째 수, 5번째 수이고, 1번째 수를 읽었을 때 중앙값은 1, 3번째 수를 읽었을 때는 4, 5번째 수를 읽었을 때는 3이다.

입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스의 첫째 줄에는 수열의 크기 M(1 ≤ M ≤ 9999, M은 홀수)이 주어지고, 그 다음 줄부터 이 수열의 원소가 차례대로 주어진다. 원소는 한 줄에 10개씩 나누어져있고, 32비트 부호있는 정수이다.

출력
각 테스트 케이스에 대해 첫째 줄에 출력하는 중앙값의 개수를 출력하고, 둘째 줄에는 홀수 번째 수를 읽을 때 마다 구한 중앙값을 차례대로 공백으로 구분하여 출력한다. 이때, 한 줄에 10개씩 출력해야 한다.
'''

from sys import stdin
from heapq import heappush, heappop
input = lambda: stdin.readline().rstrip()


def get_median() -> None:
    left, right, ans = [], [], [nums[0]]
    mid = nums[0]

    for i, num in enumerate(nums[1:], 1):
        if num < mid:
            heappush(left, -num)
        else:
            heappush(right, num)

        if i % 2 == 0:
            if len(left) > len(right):
                heappush(right, mid)
                mid = -heappop(left)
            elif len(left) < len(right):
                heappush(left, -mid)
                mid = heappop(right)
            ans.append(mid)

    print(M // 2 + 1)
    for i, num in enumerate(ans):
        if i != 0 and i % 10 == 0:
            print()
        print(num, end=' ')
    print()


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        M = int(input())
        nums = []
        for _ in range(M // 10 + 1):
            nums += list(map(int, input().split()))

        get_median()