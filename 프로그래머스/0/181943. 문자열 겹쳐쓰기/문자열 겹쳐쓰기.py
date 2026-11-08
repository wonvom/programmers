def solution(my_string, overwrite_string, s):
    a = my_string[:s]
    answer = a + overwrite_string + my_string[s+len(overwrite_string):]
    return answer