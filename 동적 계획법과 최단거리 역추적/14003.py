# 가장 긴 증가하는 부분 수열 5

'''
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (-1,000,000,000 ≤ Ai ≤ 1,000,000,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
둘째 줄에는 정답이 될 수 있는 가장 긴 증가하는 부분 수열을 출력한다.
'''

n=int(input())
arr = list(map(int,input().split()))

LIS = [arr[0]]
dp = [(0,arr[0])] 

def binarySearch(e):
    start = 0
    end = len(LIS) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if LIS[mid] == e:
            return mid
        elif LIS[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
            
    return start


for i in range(1,n):
    if arr[i] > LIS[-1]:
        LIS.append(arr[i])
        dp.append((len(LIS)-1, arr[i]))

    else:
        idx = binarySearch(arr[i])
        LIS[idx] = arr[i]
        dp.append((idx, arr[i]))


print(len(LIS))

last_idx = len(LIS) - 1
res = []
for i in range(len(dp)-1, -1, -1):
    if dp[i][0] == last_idx:
        res.append(dp[i][1])
        last_idx-=1

print(*res[::-1])