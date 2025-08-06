def solution(n, m):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    lcm = n * m // gcd(n, m)
    return [gcd(n, m), lcm]
print(solution)