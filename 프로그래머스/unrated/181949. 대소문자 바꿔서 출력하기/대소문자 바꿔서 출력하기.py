# • lower()는 문자열의 모든 문자를 소문자로 바꾼다. 예를 들어 "Ups AND Downs".lower()는 'ups and downs'로 계산된다.

# • upper()는 문자열의 모든 문자를 대문자로 바꾼다. 예를 들어 "Ups AND Downs".upper()는 'UPS AND DOWNS'로 계산된다.

# • swapcase()는 대문자를 소문자로, 소문자를 대문자로 바꾼다. 예를 들어 "Ups AND Downs".swapcase()는 'uPS and dOWNS'로 계산된다.

# • capitalize()는 문자열의 첫 번째 문자만 대문자로 바꾸고 나머지 문자를 소문자로 바꾼다. 예를 들어 "a long Time Ago...".capitalize() 는 'A long time ago... '로 계산된다.

str = input()
print(str.swapcase())