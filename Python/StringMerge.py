# https://school.programmers.co.kr/learn/courses/30/lessons/181943
# 문자열 겹쳐쓰기

# 문자열 슬라이싱
def solution(my_string, overwrite_string, s):
    return my_string[0:s] + overwrite_string + my_string[s+len(overwrite_string):]