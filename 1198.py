# 삼각형으로 자르기

'''
문제
볼록 다각형이 있고, 여기서 3개의 연속된 점을 선택해서 삼각형을 만든다. 그 다음, 만든 삼각형을 다각형에서 제외한다. 원래 다각형이 N개의 점이 있었다면, 이제 N-1개의 점으로 구성된 볼록 다각형이 된다. 위의 과정은 남은 다각형이 삼각형이 될 때까지 반복한다.
볼록 다각형의 점이 시계 방향순으로 주어진다. 마지막에 남은 삼각형은 여러 가지가 있을 수 있다. 이때, 가능한 넓이의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 볼록 다각형 점의 수 N (3 ≤ N ≤ 35)이 주어진다. 둘째 줄부터 N개의 줄에는 볼록 다각형을 이루고 있는 점이 시계 방향 순서로 주어진다. 좌표는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다. 절대/상대 오차는 10-9까지 허용한다.
'''

from itertools import combinations
import math
def area(a,b,c):
    x1,y1 = a[0],a[1]
    x2,y2 = b[0],b[1]
    x3,y3 = c[0],c[1]
    return int(math.fabs(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3)) * 1/2
ans = -1
N = int(input())
pts = []
for _ in range (0,N):
    pt = list(map(int,input().split()))
    pts.append(pt)

for t in combinations(pts,3):
    t = list(t)
    a,b,c = t[0],t[1],t[2]
    ans = max(ans, area(a,b,c))
print(ans)