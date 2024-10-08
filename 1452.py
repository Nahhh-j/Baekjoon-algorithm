# 숌 크로스워드

'''
문제
숌 크로스워드 퍼즐은 검정칸으로 칠해져 있고 그렇고 그런 크로스워드 퍼즐을 약간 변형한 것이다. 숌 크로스워드 퍼즐은 영어 단어 4개가 주어졌을 때, 아래 규칙을 모두 만족하는 크로스워드 퍼즐을 총 몇 개 만들 수 있는지 구하는 퍼즐이다.

숌 크로스워드 퍼즐의 규칙은 다음과 같다.

모든 네 개의 단어는 정확하게 한 번 크로스워드 퍼즐에 등장해야 한다.
네 개의 단어중 두 개는 반드시 가로로 쓰여야 한다. (왼쪽에서 오른쪽으로)
네 개의 단어중 두 개는 반드시 세로로 쓰여야 한다. (위쪽에서 아래쪽으로)
가로로 쓰여진 모든 단어는 세로로 쓰여진 모든 단어와 교차해야 한다. (정확하게 하나의 단어를 공유)
세로로 쓰여진 모든 단어는 가로로 쓰여진 모든 단어와 교차해야 한다. (정확하게 하나의 단어를 공유)
가로로 쓰여진 모든 단어는 적어도 하나의 빈 행으로 구분되어야 한다.
세로로 쓰여진 모든 단어는 적어도 하나의 빈 열으로 구분되어야 한다.
이러한 규칙으로 여러 개의 크로스워드 퍼즐을 만들 수 있는데, 이때 두 크로스워드 퍼즐이 서로 다를 조건은 가장 왼쪽에 쓰여진 글자를 0번으로 하고, 가장 위쪽에 쓰여진 글자를 0번으로 해서 모든 단어의 상대적인 위치가 같으면 같은 글자로 친다.

예를 들어, 단어가 zaxb, axc, cxd, bxdy라고 하면, 두 가지 크로스워드 퍼즐을 만들 수 있다.

           z
zaxb       axc
 x x       x x
 cxd       bxdy
   y

입력
네 개의 단어가 한 줄에 하나씩 입력으로 주어진다. 각 단어의 길이는 3보다 크거나 같고 15보다 작거나 같다. 단어는 중복되지 않는다.

출력
첫째 줄에 경우의 수를 출력한다.
'''
