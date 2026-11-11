def solution(a, b):
    answer = max(int((str(a)+str(b))), int(str(b)+str(a))) # max는 같아도 둘 중에 하나를 반환
    return answer