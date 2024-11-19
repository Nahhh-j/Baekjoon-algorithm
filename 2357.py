# 최솟값과 최댓값

'''
문제
N(1 ≤ N ≤ 100,000)개의 정수들이 있을 때, a번째 정수부터 b번째 정수까지 중에서 제일 작은 정수, 또는 제일 큰 정수를 찾는 것은 어려운 일이 아니다. 하지만 이와 같은 a, b의 쌍이 M(1 ≤ M ≤ 100,000)개 주어졌을 때는 어려운 문제가 된다. 이 문제를 해결해 보자.
여기서 a번째라는 것은 입력되는 순서로 a번째라는 이야기이다. 예를 들어 a=1, b=3이라면 입력된 순서대로 1번, 2번, 3번 정수 중에서 최소, 최댓값을 찾아야 한다. 각각의 정수들은 1이상 1,000,000,000이하의 값을 갖는다.

입력
첫째 줄에 N, M이 주어진다. 다음 N개의 줄에는 N개의 정수가 주어진다. 다음 M개의 줄에는 a, b의 쌍이 주어진다.

출력
M개의 줄에 입력받은 순서대로 각 a, b에 대한 답을 최솟값, 최댓값 순서로 출력한다.
'''

import sys
input = sys.stdin.readline

def make_tree(lst, tree, node, st, ed):
    if st == ed:
        tree[node] = (lst[st], lst[st])
    else:
        mid = (st + ed) // 2
        make_tree(lst, tree, 2*node, st, mid)
        make_tree(lst, tree, 2*node + 1, mid + 1, ed)
        tree[node] = (min(tree[2*node][0], tree[2*node + 1][0]), max(tree[2*node][1], tree[2*node + 1][1]))

def calculate(tree, node, st, ed, left, right):
    if right < st or left > ed:
        return float('inf'), -float('inf')
    if left <= st and right >= ed:
        return tree[node]
    mid = (st + ed) // 2
    min_left, max_left = calculate(tree, 2*node, st, mid, left, right)
    min_right, max_right = calculate(tree, 2*node + 1, mid + 1, ed, left, right)
    return min(min_left, min_right), max(max_left, max_right)

N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]

tree_size = 1
while tree_size < N:
    tree_size *= 2
tree = [(float('inf'), -float('inf'))] * (2 * tree_size)
make_tree(lst, tree, 1, 0, N - 1)

for _ in range(M):
    a, b = map(int, input().split())
    mn, mx = calculate(tree, 1, 0, N - 1, a - 1, b - 1)
    print(mn, mx)