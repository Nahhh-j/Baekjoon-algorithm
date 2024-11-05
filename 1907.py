# 탄소 화합물

'''
문제
세 가지 종류의 원자 - C, H, O로만 이루어진 화합물을 탄소 화합물이라고 한다. 우리는 아래와 같은 단순한 화학식의 계수를 맞추어 균형을 주려고 한다.

<분자> + <분자> = <분자>

여기서 <분자>란 아래와 같은 형식으로 되어 있는 문자열을 말한다.

<원자>[숫자]<원자>[숫자] … <원자>[숫자]

각각의 분자는 적어도 하나 이상의 원자로 구성되어 있고, 각각의 원자 뒤에 따라붙게 되는 숫자는 그 원자가 몇 번 나타나는가 하는 것이다. 숫자는 2 이상 9 이하이며, 숫자가 표시되지 않은 경우는 그 원자가 한 번만 나타났다는 뜻이다.
예를 들어 HC3OH2와 같은 문자열은 분자이고, 이는 H 3개, C 3개, O 1개로 되어 있는 분자가 된다. C2HOH + CH = C5O2H4와 같은 식이 우리가 관심이 있는 화학식이 된다.

어떤 화학식이 균형이 있다는 것은, 등호(=)를 기준으로 왼쪽에 있는 각각의 원자의 개수와 오른쪽에 있는 각각의 원자의 개수가 같을 때를 말한다. 예를 들어 C+CH=C2H와 같은 식이 균형 있는 화학식이 된다.
만일 어떤 화학식이 균형이 있지 않다면, 적절한 계수를 주어 화학식의 균형을 맞출 수 있다. 즉 각 <분자>가 여러 개 있는 것으로 생각한다는 것이다. 예를 들어 C+CC=CCCCC와 같은 화학식은 C + 2 ( CC ) = CCCCC 와 같이 1, 2, 1의 계수를 주어 균형을 맞출 수 있다는 것이다.
탄소 화합물 분자로만 이루어진 <분자> + <분자> = <분자> 형태의 화학식이 주어지면, 적절히 계수를 맞추어서 균형 있는 화학식으로 만드는 프로그램을 작성하시오. 단, 계수는 1 이상 10 이하로만 한정하도록 하자.

입력
첫째 줄에 M1+M2=M3 형태의 화학식이 입력으로 주어진다. 주어지는 화학식의 길이는 50을 넘지 않으며, 'C', 'H', 'O', '+', '='와 '2'∼'9'만으로 이루어져 있다.

출력
첫째 줄에 세 정수 X1, X2, X3 (1 이상 10 이하)를 빈 칸을 사이에 두고 순서대로 출력한다. 이는 각각 M1, M2, M3의 계수가 된다. 만일 해가 둘 이상이라면 답을 세 자연수로 이루어진 수열으로 생각해서, 사전순으로 가장 앞선 것을 출력한다. (즉 X1이 가장 작은 것을 먼저 출력하고, 그것도 둘 이상이면 X2가 가장 작은 것, ... 이런 순서로 출력한다.)
'''

checknum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
select = [0 for i in range(3)]
isStop = False

def dfs(cnt) :
    global isStop
    global select
    
    if isStop:
        return 
    
    if cnt == 3:
        checklist = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        for i in range(3):
            for j in range(3):
                checklist[i][j] = count[i][j] * select[i]
        
        isAns = True
        for i in range(3):
            if checklist[0][i] + checklist[1][i] != checklist[2][i]:
                isAns = False
                break
        
        if isAns:
            isStop = True
            for i in range(3):
                print(select[i], end=" ")
        return 
    
    for i in range(10):
        select[cnt] = checknum[i]
        dfs(cnt + 1)
        


str = input()
list = str.replace('+', ' ').replace('=', ' ').split(' ')
list[0] = list[0] + ' '
list[1] = list[1] + ' '
list[2] = list[2] + ' '

count = []
for s in list:
    tmp = [0, 0, 0]
    
    for i in range(len(s)):
        if s[i].isdigit():
            continue
        
        num = 1
        if s[i] == 'C':
            if s[i+1].isdigit():
                num = int(s[i+1]) 
            tmp[0] += num
            
        elif s[i] == 'H':
            if s[i+1].isdigit():
                num = int(s[i+1]) 
            tmp[1] += num
            
        elif s[i] == 'O':
            if s[i+1].isdigit():
                num = int(s[i+1]) 
            tmp[2] += num
    
    count.append(tmp)
    
dfs(0)