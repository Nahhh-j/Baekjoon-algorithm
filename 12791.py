# Starman

'''
문제
“ There's a starman waiting in the sky
He'd like to come and meet us
But he thinks he'd blow our minds 
There's a starman waiting in the sky
He's told us not to blow it
Cause he knows it's all worthwhile “

David Bowie - Starman, 1972

2016년은 Coder's High 온사이트가 2년 만에 돌아온 경사스러운 해이기도 하지만, 전설적인 락 스타 David Bowie가 지병인 암으로 사망한 슬픈 년도이기도 하다.
재현이는 데이빗 보위를 기리기 위해서, RDBMS(Rockstar David Bowie Memorial System) 라는 프로그램을 구상하였다. RDBMS는 SQL(Starman Query Language)라는 언어를 통해서 작동한다. SQL은 상당히 간단한 언어로, 다음과 같은 질의에 대해서 응답한다.
S E -> S년 1월 1일 이후, E년 12월 31일 이전 발매된 데이빗 보위의 앨범을 출력한다. 앨범을 출력할 때는, "발매연도 앨범 이름" (따옴표 없이) 의 형식으로 출력하라. 출력은 발매일 순으로 진행해야 하며, 앨범은 새 줄로 구분한다. (1 ≤ S ≤ E ≤ 2016)
재현이를 도와서, SQL의 질의에 응답하는 프로그램을 만들어라. 문제 설명에 주어지지 않은 정보로 생기는 문제를 없애기 위해, 예제 2는 모든 가능한 데이빗 보위의 앨범을 포함한, 올바른 출력을 보여준다. 예제 2의 데이터를 바탕으로 출력하라.

입력
첫 번째 줄에 질의의 수 정수 Q(Q ≤ 100)가 주어진다.
이후 Q개의 줄에 질의 S, E(1 ≤ S ≤ E ≤ 2016)가 정수로 주어진다.

출력
각 질의에 대해서 다음 정보를 출력한다 :
첫 번째 줄에는, 질의를 만족하는 데이빗 보위의 앨범 수 S를 출력한다.
이후 S개의 줄에 데이빗 보위의 앨범 이름을 새 줄로 구분하여 주어진 순서대로 출력한다. 앨범의 이름을 출력할 때, 띄어쓰기, 대소문자 등이 출제자의 코드와 다르게 출력되면 안 된다. 출력은 예제에 나온 이름과 정확히 일치해야 한다.
각각의 질의마다 새 줄로 구분할 필요는 없다. 예제 입출력을 참고하라.
'''