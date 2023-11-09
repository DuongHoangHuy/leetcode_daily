
# all cases can happen:
# 
def countHomogenous(s: str) -> int:
    cnt = 1
    sum = 0
    for i in range(len(s)):
        if i == len(s) - 1 or s[i] != s[i+1]:
            sum += int(((1 + cnt) * cnt) / 2)
            cnt = 1
        else:
            cnt += 1
    
    return sum % (10**9 + 7)

def countHomogenous_2(s: str) -> int:
    cnt = 1
    sum = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            sum += int(((1 + cnt) * cnt) / 2)
            cnt = 1

    if s[i] == s[i-1]:
        sum += int(((1 + cnt) * cnt) / 2)
    
    return sum % (10**9 + 7)

print(countHomogenous("xxx"))