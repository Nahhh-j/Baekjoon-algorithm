# 책정리

'''
문제
동혁이는 캠프가 끝나고 집에 가서 책꽂이 정리를 하고 있었다. 책들은 한 줄로 길게 꽂히 있었다. 동혁이의 책은 1번부터 N번까지 숫자로 표현되고  현재 뒤죽박죽 되어있는 순서를 왼쪽부터 오른쪽으로 순서대로 1∼N번의 책들로 재배열하길 원한다.
동혁이가 책들을 배열하는 방법은 어떠한 책 하나를 꺼내서 다른 위치에 꽂는 방법이다.

1 5 2 3 4

위와 같이 책이 배열되어 있을 때 5번 책을 꺼내 가장 뒤쪽에 꼽으면

1 2 3 4 5

로 배열되고, 1∼5번까지 순서대로 책이 꽂히면서 정리는 끝나게 된다.
문제는 현재 책들의 배열순서가 주어지면 최소 횟수로 책들을 옮겨 책 정리를 끝내는 것이다.

입력
첫째 줄에 책의 개수 N(1 ≤ N ≤ 200,000)이 주어진다. 두 번째 줄에는 현재 책들이 배열된 순서가 공백으로 구분되어 주어진다.

출력
동혁이가 책들을 옮겨야 하는 최소 횟수를 출력한다.
'''

import sys; input = sys.stdin.readline
from bisect import bisect_left

class LIS:
    def __init__(self):
        self.I = [0] * N
        self.idx = 1
        self.L = [A[0]]

        for i in range(1, N):
            
            if self.L[-1] < A[i]:
                self.I[i] = self.idx
                self.idx += 1
                self.L.append(A[i])
        
            else:
                self.I[i] = bisect_left(self.L, A[i])
                self.L[self.I[i]] = A[i]

    def trace(self): 
        self.result = [0] * self.idx
        for i in range(N - 1, -1, -1):
            if self.I[i] + 1 == self.idx:
                self.idx -= 1
                self.result[self.idx] = A[i]

        print(*self.result)

N = int(input())
A = list(map(int, input().split()))

lis = LIS()
print(N - lis.idx)