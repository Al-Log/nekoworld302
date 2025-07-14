import math

def solution(n):
    root = math.isqrt(n)  # 정수 제곱근 (ex. 121 → 11)
    if root * root == n:
        return (root + 1) ** 2
    else:
        return -1
    
print(solution(121))