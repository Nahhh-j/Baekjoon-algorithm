# 영식이와 친구들

'''
문제
영식이와 친구들이 원형으로 모여서 시계방향으로 1부터 N까지 적혀있는 자리에 앉는다. 영식이와 친구들은 공 던지는 게임을 하기로 했다. 게임의 규칙은 다음과 같다.
일단 1번 자리에 앉은 사람이 공을 받는다. 그리고 나서 공을 다른 사람에게 던진다. 다시 공을 받은 사람은 다시 공을 던지고, 이를 계속 반복한다. 한 사람이 공을 M번 받았으면 게임은 끝난다. (지금 받은 공도 포함하여 센다.) 공을 M번보다 적게 받은 사람이 공을 던질 때, 현재 공을 받은 횟수가 홀수번이면 자기의 현재 위치에서 시계 방향으로 L번째 있는 사람에게, 짝수번이면 자기의 현재 위치에서 반시계 방향으로 L번째 있는 사람에게 공을 던진다.
공을 총 몇 번 던지는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N, M, L이 입력으로 들어온다. N은 3보다 크거나 같고, 50보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다. L은 N-1보다 작거나 같은 자연수이다.

출력
첫째 줄에 공을 몇 번 던지는지 횟수를 출력한다.
'''

N, M, L = map(int, input().split())
li = [0]*N
cnt = i = 0
while li[i] < M-1:
    li[i] += 1
    cnt += 1
    i = (i+L)%N if li[i]%2 == 1 else (i-L)%N
print(cnt)