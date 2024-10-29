# 순열복원

'''
문제
1부터 N번까지로 수로 이루어진 순열이 있다.
그리고 이 순열과 연관된 "Inversion sequence"라고 부르는 수열이 있다. 이 수열의 i번째 원소에는 순열에서 i보다 뒤에 나오면서 i보다 작은 수의 개수가 들어간다.

2  4  5  1  7  6  3  8

위의 순열이 있다면 이것의 Inversion sequence는

0  1  0  2  2  1  2  0 이 된다.

문제는 역으로 어떤 Inversion sequence가 주어지면 이것에 해당하는 순열을 찾는 프로그램을 작성하는 것이다.

입력
순열의 크기 N(1 ≤ N ≤ 100,000)이 주어진다. 두 번째 줄에는 순열 1, 2, …, N에 해당하는 Inversion sequence가 공백으로 구분되어 들어온다.

출력
입력으로 주어진 Inversion sequence에 대응하는 순열을 공백으로 구분하여 한 줄에 출력한다.
'''

def updatefen(i):
  while i<=M:
    fen[i] += 1
    i += i&-i

def sumfen(i):
  SUM = 0
  while i:
    SUM += fen[i]
    i -= i&-i
  return SUM

def find(x,i,c):
  s = i-1-sumfen(i)
  if x==s and not seq[i]:
    return i
  if x>s:
    return find(x,i+(1<<c),c-1)
  return find(x,i-(1<<c),c-1)

N = int(input()); M = 1<<17
data = [*map(int,input().split())]
seq = [0]*(N+1); fen = [0]*(M+1)
for i in range(1,N+1):
  idx = find(data[-i],M,16)
  seq[idx] = N+1-i
  updatefen(idx)
print(*reversed(seq[1:]))