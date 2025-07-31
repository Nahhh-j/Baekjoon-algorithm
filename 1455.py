# 뒤집기 II

'''
문제
세준이는 동전 뒤집기를 하려고 한다. 세준이는 동전을 N×M개 가지고 있다. 동전은 세로로 N개, 가로로 M개 크기의 직사각형에 차곡차곡 놓여져 있다.
동전의 앞면을 0이라고 하고 뒷면을 1이라고 했을 때, 세준이는 모든 동전을 뒤집어서 앞면으로 만들려고 한다.
세준이가 (a,b)칸을 뒤집으려고 한다면, (i,j) (1 ≤ i ≤ a, 1 ≤ j ≤ b)의 조건을 만족하는 a×b개의 동전이 한번에 모두 뒤집힌다. (i는 위에서부터 위치의 위치이고, j는 왼쪽에서 부터의 위치이다.)
세준이가 뒤집어야하는 동전의 개수를 출력하시오. (a,b)칸을 선택해서 a×b개가 뒤집혔다면, 동전을 뒤집은 횟수는 a×b가 아니라 1이다.

입력
첫째 줄에 세로크기 N과 가로크기 M이 주어진다. N과 M은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 M개의 동전 상태가 주어진다.

출력
첫째 줄에 세준이가 동전을 뒤집는 횟수를 출력한다.
'''

N, M = map(int, input().split())
src = []
for _ in range(N):
    tmp = []
    for i in input():
        tmp.append(i)
    tmp = list(map(int, tmp))
    src.append(tmp)
cnt = 0
for i in range(N - 1, -1, -1):
    for j in range(M - 1, -1, -1):
        if src[i][j]:
            cnt += 1
            for p in range(i + 1):
                for q in range(j + 1):
                    if src[p][q] == 1:
                        src[p][q] = 0
                    else:
                        src[p][q] = 1
print(cnt)