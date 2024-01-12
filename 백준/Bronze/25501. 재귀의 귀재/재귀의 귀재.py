def recursion(s, l, r, cnt):
    cnt += 1
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: return recursion(s, l+1, r-1, cnt)


def isPalindrome(s,cnt):
    return recursion(s, 0, len(s)-1,cnt)


for _ in range(int(input())):
    cnt = 0
    i , cnt = isPalindrome(input(), cnt)
    print(i , cnt)