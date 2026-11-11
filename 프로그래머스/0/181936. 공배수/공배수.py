def solution(number, n, m):
    if number % n == 0 and number % m == 0 : # & 는 내가 생각하는 둘다 참이면 참인 기호가 아님 and 쓸것!
        answer = 1
    else :
        answer = 0
    return answer