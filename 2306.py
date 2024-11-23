# 유전자

'''
문제
DNA 서열은 4개의 문자 {a,c,g,t} 로 이루어진 문자열이다. DNA 서열에는 생명의 신비를 풀 수 있는 많은 정보가 들어 있다. 특히 KOI 유전자의 길이는 사람의 키와 깊은 상관 관계가 있다는 것이 알려져 있다. 이러한 KOI 유전자는 다음의 조건을 만족한다.

at 와 gc 는 가장 짧은 길이의 KOI 유전자이다.
어떤 X가 KOI 유전자라면, aXt와 gXc도 KOI 유전자이다. 예를 들어, agct 와 gaattc는 KOI 유전자이나, tgca 와 cgattc는 KOI 유전자가 아니다.
어떤 X와 Y가 KOI 유전자라면, 이 둘을 연결한 XY도 KOI 유전자이다. 예를 들면, aattgc 또는 atat는 KOI 유전자이나 atcg 또는 tata는 KOI 유전자가 아니다.
KOI 유전자는 DNA 서열 중에서 부분 서열로 구성되어 있다. 부분 서열이란 주어진 서열에서 임의의 위치에 있는 0개 이상의 문자들을 삭제해서 얻어지는 서열이다. 예를 들면, DNA 서열 acattgatcg에서 두 번째 문자 c와 마지막 문자 g를 삭제하여 생긴 부분 서열 aattgatc는 길이가 8인 KOI 유전자이다. 그러나 마지막 문자 g를 삭제하여 만들어진 부분 서열 acattgatc는 KOI 유전자가 아니다.

문제는 주어진 DNA 서열의 부분 서열들 중에서 길이가 최대가 되는 KOI 유전자를 찾아 그 길이를 출력하는 것이다.

입력
첫째 줄에는 분석하고자 하는 DNA 서열이 주어진다. DNA 서열의 길이는 최대 500이다.

출력
입력 DNA 서열로부터 계산된 가장 긴 KOI 유전자의 길이를 첫 번째 줄에 출력한다. 단, KOI 유전자가 없는 경우에는 0을 출력한다.
'''

import sys
input = sys.stdin.readline

t = input().strip()
dp = [[float('inf') for _ in range(len(t))] for _ in range(len(t))]

def dfs(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if dp[x][y] != float('inf'):
        return dp[x][y]

    if (t[x] == 'a' and t[y] == 't') or (t[x] == 'g' and t[y] == 'c'):
        dp[x][y] = min(dp[x][y], dfs(x+1, y-1))
    for k in range(x, y):
        dp[x][y] = min(dp[x][y], dfs(x, k) + dfs(k+1, y))

    return dp[x][y]

print(len(t) - dfs(0, len(t)-1))