# 이분 매칭

'''
문제
그래프의 최대 매칭 (Maximum Matching)은 두 간선이 같은 정점을 공유하지 않는 간선의 최대 집합을 말한다.
이분 그래프 (Bipartited Graph)는 그래프의 모든 정점을 두 집합 A와 B로 나눌 수 있는 그래프이다. 모든 간선의 끝 점은 A에 하나, B에 하나 있어야 한다. 이분 그래프에서 최대 매칭을 구하는 문제는 Maximum Flow 알고리즘을 이용해서 풀 수 있다.
거의 이분 그래프는 모든 정점이 집합 A = {A1, A2, …, AnA}와 B = {B1, B2, …, BnB}로 나누어져 있고, 모든 간선의 끝 점은 A에 하나, B에 하나있는 그래프이다. 여기까지는 이분 그래프와 동일한 모양을 갖는다. 거의 이분 그래프는 이분 그래프와 다르게 nA-1 + nB-1개의 간선을 추가로 가진다. 추가가 되는 간선은 Ai에서 Ai+1로 가는 간선 (1 ≤ i ≤ nA-1)과 Bi에서 Bi+1로 가는 간선 (1 ≤ i ≤ nB-1)이다. 따라서, 끝 점이 A에 하나, B에 하나 있는 간선의 개수를 M이라고 했을 때, 정점의 수가 nA + nB인 거의 이분 그래프의 간선의 개수는 M + nA-1 + nB-1이 된다.
거의 이분 그래프의 정점의 개수를 나타내는 nA, nB와 A와 B에 끝점을 두고 있는 간선 M개가 입력으로 주어졌을 때, 최대 매칭을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 nA와 nB가 주어진다. 둘째 줄에는 A와 B에 끝점을 두고 있는 간선의 개수 M이 주어진다. 다음 M개의 줄에는 간선의 정보가 i j와 같은 형식으로 주어지며, i는 집합 A의 정점 Ai, j는 B의 정점 (Bj)를 의미한다.

출력
첫째 줄에 입력으로 주어진 거의 이분 그래프의 최대 매칭의 수를 출력한다.
'''

import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

nA, nB = map(int, input().split())
M = int(input())
result = 0

if nA % 2 == 1 and nB % 2 == 1:
    for _ in range(M):
        x, y = map(int, sys.stdin.readline().rstrip().split(" "))
        if (x - 1) % 2 == 0 and (y - 1) % 2 == 0 :
            result += 1
            break
result += nA // 2 + nB // 2
print(result)