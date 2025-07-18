# 프로그래밍 언어 L

'''
문제
다음과 같은 가상의 프로그래밍 언어 L이 있다.

L 프로그램의 각 줄은 순서대로 1부터 N(1 ≤ N ≤ 100,000)의 번호가 붙어 있다.
각 줄에는 정확히 한 개의 명령어만 들어간다.
프로그램은 첫 번째 줄부터 수행된다.

가능한 명령은 ifgo, jump, pass, loop, die의 다섯 가지만 있다.
각 줄을 수행할 때마다 그 줄의 번호가 출력된다. 그 명령이 입력을 받는 명령일 경우에도 줄 번호가 먼저 출력된다.
ifgo 명령은 다른 명령의 줄 번호를 의미하는 한 개의 인자를 갖는다. 이 명령을 수행하면 한 비트의 입력을 받는다. 만약 입력이 1이면 명령에 지시된 줄 번호로 이동한다. 만약 입력이 0이면 다음 줄로 이동한다.

jump 명령은 다른 명령의 줄 번호를 의미하는 한 개의 인자를 갖는다. 이 명령을 수행하면 명령에 지시된 줄 번호로 이동한다.
pass 명령은 인자가 없는 명령이다. 이 명령을 수행하면 아무 것도 하지 않고, 줄 번호만 출력한 다음에 다음 줄로 이동한다.
die 명령은 인자가 없는 명령이다. 이 명령을 수행하면 줄 번호를 출력한 다음에 프로그램이 끝난다. 이 명령은 반복문 안에서는 사용되지 않는다.

loop 명령은 반복문을 수행할 때 사용되는데, 두 개의 인자 l, c를 갖는다. l은 반복문이 시작되는 줄 번호이고, c는 반복 회수이다. l은 항상 loop 명령이 있는 줄 번호보다 작은 값을 갖는다. 이 명령을 수행하면 l번째 줄부터 loop 명령이 있는 줄까지를 c-1번 수행한다. 반복문이 끝난 다음에는 그 다음 줄로 이동한다.
ifgo, jump 명령은 그 명령이 있는 반복문의 범위에서만 이동할 수 있다. 즉, 두 명령이 반복문 안에 있는 경우, 그 반복문의 범위 밖으로 이동할 수 없다. 또한, 반복문 안에 두 명령어가 있고, 그 다음 줄에 또다른 반복문이 있는 경우, 안쪽 반복문 안으로 이동할 수는 없다. 예를 들면 다음과 같은 경우는 잘못된 프로그램이다.
반복문 안에 반복문이 들어갈 경우, 안쪽 반복문이 바깥쪽 반복문에 완전히 포함되어야 한다. 즉, 안쪽 반복문의 시작 줄 번호가 바깥쪽 반복문의 시작 줄 번호보다 커야 한다(같은 경우도 안 됨). 그 외의 형태로 두 반복문이 겹치는 경우는 없다.
프로그램의 제일 마지막 줄이 수행되었을 때, 그 명령이 die가 아닌 경우 프로그램은 첫 번째 줄부터 다시 수행된다.

프로그램을 알아보기 쉽게 하기 위해 각 줄에 스페이스나 탭이 여러 개 들어갈 수도 있다.
각 줄의 최대 길이는 스페이스나 탭을 포함하여 80자를 넘지 않는다.
L로 짠 프로그램이 주어졌을 때, 그 프로그램이 최대 몇 번이나 줄 번호를 출력하는지 계산하는 프로그램을 작성하시오. Ifgo 명령의 경우, 입력값에 따라서 출력 회수가 변할 수 있는데, 출력 회수가 최대가 되는 입력이 주어진다고 가정한다.

입력
첫째 줄에 N이 주어진다. 다음 N개의 줄에 L 프로그램이 첫째 줄부터 차례대로 주어진다.

출력
첫째 줄에 최대 출력 회수를 출력한다. 답은 항상 1,000,000,000이하이며, 이를 넘어가는 경우는 무한 번 수행되는 경우로 infinity를 출력하도록 한다.
'''

import sys
import threading

sys.setrecursionlimit(1 << 25)

def main():
    N = int(sys.stdin.readline())
    code = [None] * (N + 1)
    loops = {}
    parent_loop = [None] * (N + 1)
    loop_stack = []

    for i in range(1, N + 1):
        parts = sys.stdin.readline().strip().split()
        if not parts:
            continue
        cmd = parts[0]
        if cmd == 'loop':
            l, c = int(parts[1]), int(parts[2])
            code[i] = ('loop', l, c)
        elif cmd == 'ifgo':
            code[i] = ('ifgo', int(parts[1]))
        elif cmd == 'jump':
            code[i] = ('jump', int(parts[1]))
        elif cmd == 'pass':
            code[i] = ('pass', )
        elif cmd == 'die':
            code[i] = ('die', )
        else:
            raise ValueError("Unknown command")

    for i in range(1, N + 1):
        instr = code[i]
        if instr[0] == 'loop':
            l, _ = instr[1], instr[2]
            loops[i] = (l, i)
            for j in range(l, i + 1):
                parent_loop[j] = (l, i)

    visited = [0] * (N + 1)
    dp = [None] * (N + 1)
    on_stack = [False] * (N + 1)
    infinity = False

    def dfs(u):
        nonlocal infinity
        if visited[u] == 1:
            infinity = True
            return -1
        if visited[u] == 2:
            return dp[u]

        visited[u] = 1
        on_stack[u] = True
        instr = code[u]
        result = 1

        def in_same_loop(x, y):
            return parent_loop[x] == parent_loop[y]

        if instr[0] == 'ifgo':
            tgt = instr[1]
            res1, res2 = 0, 0
            if in_same_loop(u, tgt):
                res1 = dfs(tgt)
            else:
                res1 = -1
            if u + 1 <= N and in_same_loop(u, u + 1):
                res2 = dfs(u + 1)
            else:
                res2 = -1
            if res1 == -1 or res2 == -1:
                infinity = True
            result += max(res1, res2)

        elif instr[0] == 'jump':
            tgt = instr[1]
            if in_same_loop(u, tgt):
                result += dfs(tgt)
            else:
                infinity = True

        elif instr[0] == 'pass':
            if u + 1 <= N:
                result += dfs(u + 1)

        elif instr[0] == 'die':
            pass

        elif instr[0] == 'loop':
            l, c = instr[1], instr[2]
            loop_range = range(l, u + 1)
            total = 0
            for line in loop_range:
                total += dfs(line)
                if infinity:
                    return -1
            result = total * (c - 1)
            if u + 1 <= N:
                result += dfs(u + 1)

        visited[u] = 2
        dp[u] = result
        on_stack[u] = False
        return result

    ans = dfs(1)
    if infinity or ans > 1_000_000_000:
        print("infinity")
    else:
        print(ans)

threading.Thread(target=main).start()