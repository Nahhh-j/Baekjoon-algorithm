# 요컨대 형택이의 사탕봉지

'''
문제
요컨대 형택이는 사탕을 좋아한다. 이제 이 사탕을 보관하기 위해, 형택이는 요컨대 N개의 사탕 봉지를 만들었다. 그런데 형택이는 서로 다른 사탕 봉지에 같은 개수의 사탕이 들어있는 것을 요컨대 끔찍이도 싫어한다.

요컨대 첫 번째 사탕 봉지에는 사탕이 한 개, 요컨대 두 번째 사탕 봉지에는 사탕이 두 개, ..., 요컨대 N번째 사탕 봉지에는 사탕이 요컨대 N개 들어있다. 이제 요컨대 형택이는 이 N개의 요컨대 사탕 봉지 중에 몇 개만을 골라서 남겨 두고 나머지는 요컨대 조교님들께 드리려고 한다. 그런데 문제가 있다.
문제는 바로, 기훈이가 호시탐탐 형택이를, 아니 형택이의 사탕봉지를 노리고 있다는 것이다. 기훈이는 절대로 사탕을 노리는 것이 아니다. 형택이가 손수 만든 사탕 봉지를 노리는 것이다. 그런데 너무 티가 나면 안 되니까, 두 개의 사탕 봉지에 들은 사탕을 합쳐서 한 봉지에 넣고, 한 봉지를 자신이 가져가려고 한다.
그런데 문제가 있다. 바로 N = 10일 때, 네 개의 사탕이 들어있는 사탕봉지와 다섯 개의 사탕이 들어있는 사탕봉지를 합치게 되면 아홉 개의 사탕이 들어있는 사탕봉지와 개수가 똑같아진다. 이것은 형택이가 너무너무 싫어하는 것!

따라서 기훈이는 N개의 사탕 봉지 중에 K개를 고를 때, K개중 어떤 두 개의 사탕 봉지를 합쳤을 때 그것과 같은 개수의 사탕이 들어 있는 봉지가 포함되지 않도록 K개를 고르고 싶다. 위의 예처럼 각각 4개, 5개의 사탕이 들은 사탕 봉지를 고르기로 하였으면 9개의 사탕이 들은 사탕 봉지는 고르지 않아야 하는 것이다.
이러한 조건을 만족하면서 최대 몇 개의 사탕 봉지를 고를 수 있는지를 결정하는 프로그램을 작성하시오. 또한, 그러한 경우가 몇 가지나 있는지, 또 실제로 어떻게 고르면 되는지도 함께 구해야 한다. 예를 들어 N=3일 때, 최대로 두 개의 사탕 봉지만을 고를 수 있고, (세 개를 고르면 1+2=3이 되어 안 된다.) 이러한 경우는 1과 2, 1과 3, 2와 3의 세 가지 경우가 있다.

입력
첫째 줄에 데이터 케이스의 개수 D가 주어진다. (1≤D≤100) 둘째 줄부터 D개의 줄에 걸쳐 각각의 케이스의 경우 N이 주어진다. (1≤N≤1,000,000)

출력
각 테스트 케이스에 대해, 첫째 줄에 최대 몇 봉지를 뽑을 수 있는지를 나타내는 정수 K와, 그러한 경우가 몇 가지인지를 나타내는 정수 A를 빈 칸을 사이에 두고 출력한다. 둘째 줄부터 A개의 줄에 걸쳐 최대로 사탕봉지를 뽑을 수 있는 경우를 각각 한 줄에 한 가지씩 출력한다. 각 줄에는 K개의 정수를 오름차순으로 빈 칸을 사이에 두고 하나씩 나타내면 된다. 각각의 A개의 줄을 출력할 때는, K개의 정수를 나열한 것을 하나의 순열으로 볼 때 사전 순으로 앞서는 순서대로 출력해야 한다. 예를 들어 N=3인 경우 1, 2를 먼저, 1, 3을 그 다음, 마지막으로 2, 3을 출력하면 된다.
'''

