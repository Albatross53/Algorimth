# https://school.programmers.co.kr/learn/courses/30/lessons/181949
# 대소문자 바꿔서 출력하기

#1.
str = input()
str = ''.join([char.upper() if char.islower() else char.lower() for char in str])
print(str)

#2. swapcase()
str2 = input()
print(str2.swapcase())