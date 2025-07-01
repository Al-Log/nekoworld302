# 함수 solution 정의하기
def solution(n): 
    total = 0 # 약수들의 총합을 total이라는 변수에 저장   
    for i in range(1, n + 1): # 1부터 n까지 반복
        if n % i == 0: # 나머지가 0이라면
            total += i # total에 추가
    return total # 반복문이 끝나면 약수의 총합을 리턴

# 함수 solution 실행하기
print(solution) 