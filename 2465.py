# 즐 세우기

'''
문제
N명의 사람들이 어떤 공연장에 입장하기 위해서 한 줄로 서 있다. 줄 서 있는 각 사람은 자기 앞에 서 있는 사람들 중에서 자기보다 키가 작거나 같은 사람들의 수를 알고 있다. 그러면, 이 수들을 표시하는 수열을 S라고 한다.
N명의 키 집합과 수열 S가 주어질 때, 원래 줄 서 있는 키 순서를 정확히 찾아내는 프로그램을 작성하시오. 

예를 들어서, 사람들의 키 집합이 다음과 같이 주어진다 (여기서, 같은 키의 사람들이 여러 명 존재할 수 있어서 중복이 포함된다). 
{120, 167, 163, 172, 145, 134, 182, 155, 167, 120, 119, 156}

또한 각 사람이 자기 앞에 있는 사람들 중에서 자기보다 키가 작거나 같은 사람들의 수를 표시하는 수열 S는 다음과 같이 주어진다. 
S : 0 1 0 0 3 2 6 7 4 6 9 4

그러면, 실제 줄 서 있는 사람들의 키 순서는 다음과 같다. 
134 167 120 119 156 120 167 182 155 163  172 145

입력
첫째 줄에는 전체 사람의 수 N (1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에 사람들의 키를 나타내는 양의 정수가 하나씩 주어진다. 여기서 모든 키들은 2×109이하이다. 그리고 마지막 줄에 수열 S가 한 줄로 주어진다. 단 그 수열의 수는 하나의 공백을 두고 나타난다. 

출력
출력은 N개의 줄로 구성된다. N개의 줄 각각에 원래 줄 서 있는 사람들의 키를 순서대로 하나씩 출력한다. 
'''

import sys
input = sys.stdin.readline

N = int(input())
heights = sorted([int(input()) for _ in range(N)])
order = list(map(int, input().split()))
tree = [0]*(4*N)
ans = [0] * N

def init(start, end, idx) :
  if start == end :
    tree[idx] = 1
    return
  mid = (start + end) // 2
  init(start, mid, idx*2)
  init(mid+1, end, idx*2+1)
  tree[idx] = tree[idx*2] + tree[idx*2+1]

def search(target) :
  start, end, idx = 0, N-1, 1
  while start < end :
    tree[idx] -= 1
    mid = (start + end) // 2
    if tree[idx*2] < target :
      target -= tree[idx*2]
      start = mid + 1
      idx = idx*2 + 1
    else :
      end = mid
      idx = idx*2
  tree[idx] -= 1
  return end

init(0, N-1, 1)
for i, o in enumerate(reversed(order)) :
  idx = search(o+1)
  ans[N-i-1] = heights[idx]

print(*ans, sep = '\n')