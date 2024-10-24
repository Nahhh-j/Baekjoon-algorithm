# 삼각형 개수 세기

'''
문제
텍스트 블록에 채워진 삼각형 형태의 패턴이 나타날 수 있다. 일반적인 삼각형은 (a)와 같은 직각 이등변 삼각형이거나, (각 변은 2차원 어디에든, 어느 방향으로든 놓일 수 있다.)

A          BBB
AA         BB 
AAA        B  
(a)

(b)와 같은 이등변 삼각형이다. (마찬가지로 각 변은 어디에든 놓일 수 있다.)

                B
  A            BB
 AAA          BBB
AAAAA          BB
                B
(b)

삼각형의 한 변의 길이는 2 이상이어야 한다. 하나의 글자로만 이루어진 삼각형은 삼각형으로 취급하지 않아 세지 않는다.
문제는 주어진 텍스트 블록에서 위의 조건을 만족하는 삼각형의 개수를 세는 것이다.

입력
첫째 줄에 정사각형 행렬의 행의 수와 열을 수를 나타내는 정수 N(1 ≤ N ≤ 500)이 주어진다. 두 번째 줄부터 N+1번째 줄까지 텍스트 블록에 대한 정보를 나타내는 영문 대문자 N개로 구성된 문자열이 한 줄에 하나씩 주어진다.

출력
첫째 줄에 삼각형의 총 개수를 출력한다.
'''

n,m=map(int, input().split())
if n>100 or n%2 == 0 or m<1 or m>4:
    print("INPUT ERROR!")
else:
    if m==1:
        c=0
        for i in range(n):
            r=[]
            for j in range(i+1):
                c+=1
                r.append(str(c))
            print(' '.join(list(reversed(r)) if i%2==1 else r))
    elif m==2:
        for i in range(n):
            print('  '*i + (str(i)+" ")*((n-i-1)*2+1))
    elif m==3:
        r=[]
        for i in range(n):
            r.append(str(i+1)) if i <= n//2 else r.pop()
            print(' '.join(r))