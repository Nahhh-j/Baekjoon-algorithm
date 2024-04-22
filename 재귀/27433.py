# 팩토리얼 2

'''
문제
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(0 ≤ N ≤ 20)이 주어진다.

출력
첫째 줄에 N!을 출력한다.
'''

N = int(input())

if N == 0 :
    print(1)
else :
    result = 1
    for i in range(2, N+1) :
        result *= i
    print(result)