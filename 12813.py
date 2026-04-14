# 이진수 연산

'''
문제
총 100,000 비트로 이루어진 이진수 A와 B가 주어진다. 이때, A & B, A | B, A ^ B, ~A, ~B를 한 값을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 이진수 A, 둘째 줄에 이진수 B가 주어진다. 두 이진수의 길이는 모두 100,000이다. 예제의 경우에만 길이가 10이며, 예제는 채점하지 않는다.

출력
첫째 줄부터 한 줄에 하나씩 차례대로 A & B, A | B, A ^ B, ~A, ~B를 출력한다.
'''

 = int(input(), 2)
b = int(input(), 2)
n = 100000
mask = 2 ** n - 1
print(bin(a & b)[2:].zfill(n))
print(bin(a | b)[2:].zfill(n))
print(bin(a ^ b)[2:].zfill(n))
print(bin(a ^ mask)[2:].zfill(n))
print(bin(b ^ mask)[2:].zfill(n))