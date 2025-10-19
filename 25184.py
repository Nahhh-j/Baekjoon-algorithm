# 동가수열 구하기

'''
문제
길이가 $N$인 동가수열은 다음 두 조건을 만족하는 수열이다.

동가수열은 $1$ 이상 $N$ 이하인 정수로 이루어져 있고, 모든 원소는 서로 다르다.
동가수열의 서로 이웃한 원소의 차는 
 
$\lfloor \frac{N}{2} \rfloor$이상이다.
길이가 $N$인 동가수열을 아무거나 하나 구해보자. 주어지는 모든 입력에 대해 동가수열은 항상 존재한다.

입력
첫째 줄에 구하고자 하는 동가수열의 길이 $N$($1 \le N \le 5\,000$)이 주어진다.

출력
첫째 줄에 길이가 $N$인 동가수열을 아무거나 하나 출력한다. 동가수열은 공백으로 구분해서 출력해야 한다.
'''

import java.io.*;

public class C0032
{
    public static void main (String[] args) throws IOException
    {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder s = new StringBuilder("");
        int N = Integer.parseInt(input.readLine());
        int mid = N/2; 

        if ( N == 1 )
        {
            output.write("1");
            output.close();
            return;
        }

        for (int i=1; i<=mid; i++)
        {
            s.append(mid + i + " ");
            s.append(i + " ");
        }

        if ( N % 2 == 1 )
            s.append(N + "");

        output.write(s.toString());
        output.close();
    }
}