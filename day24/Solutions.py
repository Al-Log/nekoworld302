def solution(left, right):
    total = 0
    for num in range(left, right + 1):
        if (num ** 0.5).is_integer():  
            total -= num
        else:
            total += num
    return total
print(solution)