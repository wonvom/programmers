def solution(str1, str2):
    answer = "" # 문자를 담을 변수 생성
    for a in range(len(str1)): # 범위는 str1의 길이만큼 돌면됨 제시된 문제가 길이가 같은 두 문자열이라고함
        answer += str1[a] # str[] 은 그 문자열의 인덱스 자리에 있는 값을 말함.
        answer += str2[a]
    return answer # 반복문 다돌면 출력