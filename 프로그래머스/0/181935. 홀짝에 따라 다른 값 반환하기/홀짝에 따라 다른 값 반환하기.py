def solution(n):
    answer = 0
    if n % 2 == 1 :
        for i in range(n+1) :
            if i % 2 == 0 :
                continue
            else :
                answer += i
            print(answer)
    else :
        for i in range(n+1) :
            if i % 2 == 1 :
                continue
            else :
                answer += i*i
            print(i)
    return answer