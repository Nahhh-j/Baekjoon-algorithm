# 이항 계수 3

'''
문제
자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 4,000,000, 0 ≤ \(K\) ≤ \(N\))

출력
\(\binom{N}{K}\)를 1,000,000,007로 나눈 나머지를 출력한다.
'''

n, k = map(int, input().split())
p = 10 ** 9 + 7
x = 4 * 10 ** 6
a = [1] * (x + 1)

mod = 1
for i in range(1, x + 1):
    mod = (mod * i) % p
    a[i] = mod

m1, m2 = a[n], (a[k] * a[n - k]) % p
ans = m1
log = 0
while ((1 << log) <= p - 2):
    if ((1 << log) & (p - 2)):
        ans = (ans * m2) % p
    m2 = (m2 * m2) % p
    log += 1
print(ans)