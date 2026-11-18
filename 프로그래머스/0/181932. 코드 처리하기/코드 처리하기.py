def solution(code):
    ret = "" # 문자열을 담을 변수 생성
    mode = 0
    for idx in range(len(code)):
        if code[idx] == "1" :
            if mode == 1 :
                mode = 0
            else:
                mode = 1
        else :
            if mode == 0 :
                if idx % 2 == 0:
                    ret = ret + code[idx]
            else:
                if idx % 2 == 1:
                    ret = ret + code[idx]
    if ret == "":
        ret = "EMPTY"
    return ret