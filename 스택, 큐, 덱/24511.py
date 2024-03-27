# queuestack

'''
24511.jpeg
'''

import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
sequence_A = list(map(int, input().split())) 
sequence_B = list(map(int, input().split()))

M = int(input())                            
sequence_C = list(map(int, input().split()))

queue = deque([])
for i in range(N):
  if sequence_A[i] == 0:
    queue.appendleft(sequence_B[i])
else:
  if queue == []:
    print(*sequence_C)
    sys.exit()

for i in range(M):
  queue.append(sequence_C[i])
  print(queue.popleft(), end = " ")