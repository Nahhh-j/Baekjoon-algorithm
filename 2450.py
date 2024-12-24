# 모양 정돈

'''
문제
여러 개의 세모, 네모, 동그라미 모양들이 일렬로 나열되어 있다. 임의의 위치에 있는 두 개의 모양을 서로 맞바꾸는 작업을 반복하여 같은 모양끼리 연속하도록 정돈하려고 한다. 단, 정돈된 모양의 순서는 상관없다.
예를 들어, 모양들이 다음과 같이 나열되어 있다고 하자. 

△ ○ ○ □ △ △ ○ □

첫 번째 위치에 있는 세모와 일곱 번째 위치에 있는 동그라미를 맞바꾸면 다음과 같이 된다.

○ ○ ○ □ △ △ △ □

이어서, 다섯 번째 위치에 있는 세모와 마지막에 있는 네모를 맞바꾸면 다음과 같이 된다.

○ ○ ○ □ □ △ △ △

위와 같이 맞바꾸기를 두 번하면 같은 모양들끼리 연속하도록 정돈할 수 있지만, 한 번의 맞바꾸기만으로 같은 모양들끼리 연속하도록 하는 방법은 없으므로 이 경우 모양을 정돈하기위해 필요한 맞바꾸기의 최소 횟수는 2이다. 
일렬로 나열된 모양들의 순서가 입력으로 주어질 때, 같은 모양들끼리 연속하도록 정돈하기 위해 필요한 맞바꾸기 의 최소 횟수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 모양의 전체 개수 N이 주어진다. N은 3이상 100,000이하이다. 둘째 줄에는 나열된 모양들을 나타내는 N개의 정수가 빈 칸을 사이에 두고 주어지는데, 정수 1은 세모를, 정수 2는 네모를, 정수 3은 동그라미를 나타낸다. 각 모양은 최소 한번 이상 나타난다.

출력
첫째 줄에 같은 모양들끼리 연속하도록 정돈하기 위해 필요한 맞바꾸기의 최소 횟수를 출력한다.
'''