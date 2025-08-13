# 이동

'''
문제
N개의 수가 있는 X와 Y가 있다. 이때 X나 Y를 순환 이동시킬 수 있다. 순환 이동이란 마지막 원소를 제거하고 그 수를 맨 앞으로 다시 삽입하는 것을 말한다. 예를 들어, {1, 2, 3}을 순환 이동시키면 {3, 1, 2}가 될 것이고, {3, 1, 2}는 {2, 3, 1}이 된다. 순환 이동은 0번 또는 그 이상 할 수 있다. 이 모든 순환 이동을 한 후에 점수를 구하면 된다. 점수 S는 다음과 같이 구한다.
S = X[0]×Y[0] + X[1]×Y[1] + ... + X[N-1]×Y[N-1]
이때 S를 최대로 하면 된다. 

입력
첫째 줄에 N이 주어진다. 둘째 줄에는 X에 들어있는 N개의 수가 주어진다. 셋째 줄에는 Y에 있는 수가 모두 주어진다. N은 60,000보다 작거나 같은 자연수이고, X와 Y에 들어있는 모든 수는 100보다 작은 자연수 또는 0이다.

출력
첫째 줄에 S의 최댓값을 출력한다.
'''

import sys
from cmath import exp,pi
def fft(a):
    N=len(a)
    if N==1:
        return a
    a_even=fft(a[0::2])
    a_odd=fft(a[1::2])
    w_N=[exp(2j*pi*n/N) for n in range(N//2)]
    return [a_even[n] +w_N[n]*a_odd[n] for n in range(N//2)] + [a_even[n]-w_N[n]*a_odd[n] for n in range(N//2)]

def ifft(a):
    N=len(a)
    if N==1:
        return a
    a_even=ifft(a[0::2])
    a_odd=ifft(a[1::2])
    w_N=[exp(-2j*pi*n/N) for n in range(N//2)]
    return [a_even[n] +w_N[n]*a_odd[n] for n in range(N//2)] + [a_even[n]-w_N[n]*a_odd[n] for n in range(N//2)]

M=int(sys.stdin.readline())
N=2*M
even=0
for i in range(18):
    if M==2**i:
        even=-100
        break
    elif N<2**i:
        even=i
        break
A=list(map(int,sys.stdin.readline().split()))
B=list(map(int,sys.stdin.readline().split()))
if even==-100:
    A=A[:]+A[:]
    B=B[-1::-1]+[0]*M
    C=[0]*N
    A_fft=fft(A)
    B_fft=fft(B)
    for i in range(N):
        C[i]=A_fft[i]*B_fft[i]

    C_ifft=ifft(C)
    for k in range(N):
        C_ifft[k]=round(C_ifft[k].real/N)
    max_number=max(C_ifft)
else:
    N_prime=2**i
    N,N_prime=N_prime,N
    A=A[:]+[0]*(N-N_prime//2)
    B=B[-1::-1]+[0]*(N-N_prime)+B[-1::-1]

    C=[0]*N
    A_fft=fft(A)
    B_fft=fft(B)
    for i in range(N):
        C[i]=A_fft[i]*B_fft[i]
    C_ifft=ifft(C)
    for k in range(N):
        C_ifft[k]=round(C_ifft[k].real/N)
    max_number=max(C_ifft)
print(max_number)