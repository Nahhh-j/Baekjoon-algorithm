# 이항 계수 1

'''
문제
자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 10, 0 ≤ \(K\) ≤ \(N\))

출력
 
\(\binom{N}{K}\)를 출력한다.
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)

print(factorial(N) // (factorial(N-K) * factorial(K)))