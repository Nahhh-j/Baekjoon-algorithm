# 소수 구하기

'''
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
'''

def primeNumber(N,M):
    for now in range(N,M+1):
        if now > 1:
            sieve = True
            for i in range(2, int(now ** 0.5) + 1):
                if now%i == 0:
                    sieve = False
                    break
            if sieve:
                print(now)

N,M = map(int,input().split())
primeNumber(N,M)