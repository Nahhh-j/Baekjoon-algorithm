# 다음수 구하기

'''
문제
어떤 수 A가 주어졌을 때, A의 다음수를 구하는 프로그램을 작성하시오.
A의 다음수는 A와 구성이 같으면서, A보다 큰 수 중에서 가장 작은 수 이다.
A와 B의 구성이 같다는 말은 A를 이루고 있는 각 자리수의 등장 횟수가, B를 이루는 각 자리수의 등장 횟수와 같을 때 이다.
예를 들어 123과 321은 구성이 같다. 왜냐하면 두 수 모두 1이 1번, 2가 1번, 3이 1번 나오기 때문이다. 마찬가지로 14232와 12243도 구성이 같다.
하지만, 14232와 14432는 구성이 같지 않다. 

입력
첫째 줄에 테스트 케이스의 개수 T(1<=T<=1,000)가 주어진다. 둘째 줄부터 T개 줄에는 각 테스트 케이스가 주어진다. 테스트 케이스는 한 줄로 이루어져 있으며, 수 A이다. A는 최대 80자리 자연수이다.

출력
각 테스트 케이스에 대해서, 한 줄에 하나씩 A의 다음수를 출력한다. 만약, A의 다음수가 없을 때는 BIGGEST를 출력한다.
'''

from sys import stdin
from itertools import permutations
T = int(stdin.readline())

for _ in range(T):
    a = stdin.readline().rstrip()
    num = int(a)
    tmp = []
    for n in a:
        tmp.append(n)

    comb = list(permutations(tmp, len(a)))
    total = []
    for arr in comb:
        w = ''
        for n in arr:
            w += n
        total.append(int(w))
    
    total.sort(reverse=True)

    for i in range(len(total) - 1):
        if total[i] == num:
            print("BIGGEST")
            break
        if total[i + 1] == num:
            print(total[i])