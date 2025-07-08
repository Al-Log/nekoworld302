def solution(n):
    for x in range(2, n):  # 1은 항상 n으로 나누면 나머지가 n이므로 제외
        if n % x == 1:
            return x
        
print(solution(10))