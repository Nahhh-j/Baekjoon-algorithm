# 기둥만들기

'''
문제
주사위 모양의 정육면체에 각 면이 빨강(R), 초록(G), 파랑(B), 노랑(Y) 가운데 어떤 색으로 칠해져 있다. 이러한 정육면체 4개를 기둥 모양으로 쌓아 올려서 기둥의 각 옆면에 4가지 색이 모두 나타나게 하고 싶다. 이러한 기둥을 모두 몇 개나 만들 수 있는지 구하는 프로그램을 작성하시오.
정육면체 1	정육면체 2	정육면체 3	정육면체 4
그림 1
그림 2	그림 3	그림 4
정육면체를 쌓을 때 1번 정육면체를 맨 아래에 놓고, 그 위에 2번 정육면체, 3번 정육면체, 맨 위에 4번 정육면체를 놓는다. 각 정육면체는 마음대로 위치를 바꾸어서 놓을 수 있다. 예를 들어서, 그림 1과 같은 4개의 정육면체를 쌓아서 그림 2와 그림 3의 두 개의 기둥을 만들 수 있다.
하지만, 기둥을 옆으로 회전시켜서 같은 모양이 되는 것은 같은 기둥으로 본다. 예를 들어서 그림 3에 있는 기둥과 그림 4에 있는 기둥은 같은 기둥이다. 기둥의 윗면의 색이 다른 것은 다른 기둥이며, 기둥의 밑면은 보이지 않으므로 고려하지 않는다.

입력
첫줄에는 1번 정육면체, 두 번째 줄에 2번 정육면체, 세 번째 줄에 3번 정육면체, 네 번째 줄에 4번 정육면체가 입력된다. 각 줄은 6개의 영문자로 이루어진다. 영문자는 R, G, B, Y 중의 하나이다. 6개의 영문자는 순서대로 그림 5의 가, 나, 다, 라, 마, 바 면의 색을 나타낸다.
그림 5

출력
조건을 만족하는 기둥의 개수를 출력한다. 조건을 만족하는 기둥이 하나도 만들어지지 않으면 0을 출력한다.
'''

from collections import deque

side_dict = {
  2 : deque([1, 5, 3, 4]),
  3 : deque([0, 4, 2, 5]),
  0 : deque([1, 4, 3, 5]),
  1 : deque([0, 5, 2, 4]),
  5 : deque([0, 3, 2, 1]),
  4 : deque([0, 1, 2, 3])
}

colors = set(['R', 'G', 'B', 'Y'])
cube_list = [input().strip() for _ in range(4)]
column_dict = { key : list() for key in colors }

top_list = list()
side_list = list()

def column_search(idx) :
  if idx == 4 :
    make_column(1)
    return

  for i in range(6) :
    top_list.append(i)
    side_list.append(side_dict[i].copy())
    
    column_search(idx+1)
    
    top_list.pop()
    side_list.pop()

def make_column(idx) :
  if idx == 4 :
    is_valid_column()
    return

  for i in range(4) :
    make_column(idx+1)
    side_list[idx].rotate(1)
  
def is_valid_column() :
  top = top_list[-1]
  top_color = cube_list[-1][top]
  side_result = deque()
  for i in range(4) :
    side_idx_list = [side_list[j][i] for j in range(4)]
    side_color_list = [cube_list[j][side_idx_list[j]] for j in range(4)]
    if set(side_color_list) != colors :
      return
    side_result.append(''.join(side_color_list))

  for _ in range(4) :
    if side_result in column_dict[top_color] :
      return
    side_result.rotate(1)

  column_dict[top_color].append(side_result)

def solve() :
  column_search(0)
  result = 0
  for val in column_dict.values() :
    result += len(val)
  print(result)

solve()