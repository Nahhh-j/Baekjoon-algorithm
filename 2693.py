# N번째 큰 수

'''
문제
배열 A가 주어졌을 때, N번째 큰 값을 출력하는 프로그램을 작성하시오.
배열 A의 크기는 항상 10이고, 자연수만 가지고 있다. N은 항상 3이다.

입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 배열 A의 원소 10개가 공백으로 구분되어 주어진다. 이 원소는 1보다 크거나 같고, 1,000보다 작거나 같은 자연수이다.

출력
각 테스트 케이스에 대해 한 줄에 하나씩 배열 A에서 3번째 큰 값을 출력한다.
'''

T = int(input())

for _ in range(T):
    N = list(map(int, input().split()))
	N.sort()
    print(N[-3])