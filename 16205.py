# 변수명

'''
문제
변수명을 정하는 표기법은 여러 가지가 있다.

카멜 표기법 (Camel Case): 각 단어의 첫 글자를 대문자로 적는다. 단, 가장 첫 글자는 소문자를 사용한다.
예시: camelCase, variableN, thisIsCamelCase, howToSolveThisProblem
스네이크 표기법 (Snake Case): 소문자만 사용하고, 각 단어의 사이에 언더바(_)를 넣어서 적는다.
예시: snake_case, variable_n, this_is_snake_case, how_to_solve_this_problem
파스칼 표기법 (Pascal Case): 카멜 표기법과 같지만, 가장 첫 글자도 대문자를 사용한다.
예시: PascalCase, VariableN, ThisIsPascalCase, HowToSolveThisProblem
한 표기법을 사용한 변수명이 주어졌을 때, 이를 다른 표기법으로 변환하는 프로그램을 작성하시오.

입력
첫째 줄에 사용한 표기법의 번호와 변수명이 주어진다. 번호가 1인 경우는 카멜 표기법, 2인 경우는 스네이크 표기법, 3인 경우는 파스칼 표기법이다.
입력으로 주어지는 변수명의 길이는 100을 넘지 않는다.
카멜 표기법, 파스칼 표기법을 사용한 변수명은 알파벳 소문자와 대문자로만 이루어져 있고, 스네이크 표기법을 사용한 변수명은 알파벳 소문자와 언더바(_)로만 이루어져 있다. 또, 스네이크 표기법을 사용한 변수명의 첫 글자와 마지막 글자는 언더바가 아니고, 언더바가 연속해서 두 개 이상 사용하는 경우는 없다.

출력
첫째 줄에 카멜 표기법을 사용한 경우, 둘째 줄에 스네이크 표기법을 사용한 경우, 셋째 줄에 파스칼 표기법을 사용한 경우를 출력한다.
'''

def camel_to_pascal(camel):
    return camel[0].upper() + camel[1:]

def camel_to_snake(camel):
    snake = ''

    for char in camel:
        if char.isupper():
            snake += '_' + char.lower()
            continue
        
        snake += char

    return snake

def snake_to_camel(snake):
    camel = ''

    is_upper = False

    for char in snake:
        if is_upper:
            camel += char.upper()
            is_upper = False
            continue

        if char == '_':
            is_upper = True
            continue
        
        camel += char
    
    return camel

def pascal_to_camel(pascal):
    return pascal[0].lower() + pascal[1:]

number, variable = input().split()

camel_case = ''
snake_case = ''
pascal_case = ''

if number == '1':
    camel_case = variable
    snake_case = camel_to_snake(camel_case)
    pascal_case = camel_to_pascal(camel_case)

elif number == '2':
    snake_case = variable
    camel_case = snake_to_camel(snake_case)
    pascal_case = camel_to_pascal(camel_case)

elif number == '3':
    pascal_case = variable
    camel_case = pascal_to_camel(pascal_case)
    snake_case = camel_to_snake(camel_case)

print(camel_case)
print(snake_case)
print(pascal_case)