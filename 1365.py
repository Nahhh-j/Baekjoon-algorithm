# 꼬인 전깃줄

'''
문제
공화국에 있는 유스타운 시에서는 길을 사이에 두고 전봇대가 아래와 같이 두 줄로 늘어서 있다. 그리고 길 왼편과 길 오른편의 전봇대는 하나의 전선으로 연결되어 있다. 어떤 전봇대도 두 개 이상의 다른 전봇대와 연결되어 있지는 않다.

문제는 이 두 전봇대 사이에 있는 전깃줄이 매우 꼬여 있다는 점이다. 꼬여있는 전깃줄은 화재를 유발할 가능성이 있기 때문에 유스타운 시의 시장 임한수는 전격적으로 이 문제를 해결하기로 했다.
임한수는 꼬여 있는 전깃줄 중 몇 개를 적절히 잘라 내어 이 문제를 해결하기로 했다. 하지만 이미 설치해 놓은 전선이 아깝기 때문에 잘라내는 전선을 최소로 하여 꼬여 있는 전선이 하나도 없게 만들려고 한다.
유스타운 시의 시장 임한수를 도와 잘라내야 할 전선의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫 줄에 전봇대의 개수 N(1 ≤ N ≤ 100,000)이 주어지고, 이어서 N보다 작거나 같은 자연수가 N개 주어진다. i번째 줄에 입력되는 자연수는 길 왼쪽에 i번째 전봇대와 연결된 길 오른편의 전봇대가 몇 번 전봇대인지를 나타낸다.

출력
전선이 꼬이지 않으려면 최소 몇 개의 전선을 잘라내야 하는 지를 첫째 줄에 출력한다.
'''

N = int(input())
nums = list(map(int, input().split()))
n_list = list()

def lower_bound(val) :
  start, end = 0, len(n_list)-1
  while start < end :
    mid = (start + end) // 2
    if n_list[mid] < val :
      start = mid+1
    else :
      end = mid
  return end

for num in nums :
  if not n_list or n_list[-1] < num :
    n_list.append(num)
  else :
    idx = lower_bound(num)
    n_list[idx] = num

print(N-len(n_list))