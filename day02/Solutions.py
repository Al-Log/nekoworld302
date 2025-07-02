#함수 생성하기
def solution(n):
    answer = 0
    for digit in str(n): #문자열을 숫자로 변환해서 answer에 추가
        answer += int(digit)
    return answer # answer값을 반환한다

print(solution) #solution 함수 실행하기