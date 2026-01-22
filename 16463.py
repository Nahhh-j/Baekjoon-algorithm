# 13일의 금요일

'''
문제
재운이는 이 구역의 소문난 오컬트 매니아다. 늘 도서관에서 오컬트 서적을 읽고 외계문물 스터디에 참여하던 재운이는 어느 날 엄청난 소문을 듣게 되었다. 소문의 정체는 지구의 미래에 관한 예언이었는데, 그 예언에 따르면 2019년부터 다가오는 13일의 금요일의 수를 세지 않으면 지구가 멸망할 수 있다고 한다. 평소 배려심이 넘치는 재운이는 자신 뿐만 아니라 자신의 후세들을 위해 앞으로 기원 후 100,000년 까지 누적되는 13일의 금요일의 수를 매 년도마다 기록하기로 했다. 하지만 계산에 약한 재운이는 온갖 계산을 우리에게 떠맡겼다. 재운이를 도와 2019년부터 N년까지 누적되는 13일의 금요일의 수를 계산하여 알려주자. 

입력
첫째 줄에 정수 N이 입력된다. (2019 ≤ N ≤ 100,000)

출력
첫째 줄에 2019년부터 N년까지 누적되는 13일의 금요일의 수를 출력한다.
'''

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def count_friday_13(N):
    day_of_week = 1
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = 0

    for year in range(2019, N + 1):
        for month in range(12):
            if (day_of_week + 12) % 7 == 4:
                count += 1

            days = month_days[month]
            if month == 1 and is_leap(year):
                days += 1
            day_of_week = (day_of_week + days) % 7

    return count

N = int(input())
print(count_friday_13(N))