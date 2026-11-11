def solution(n):
    a = 0
    if n % 2 == 1 :
        a = n // 2 + 1
        answer = a**2
    else :
        a = n // 2
        answer = 4*a*(a+1)*(2*a+1)/6
    return answer