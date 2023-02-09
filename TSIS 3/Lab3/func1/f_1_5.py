def permute(s, answer):
    if (len(s) == 0):
        print(answer)

 
    for i in range(len(s)):
        ch = s[i]
        left,right = s[0:i], s[i + 1:]
        rest = left + right
        permute(rest, answer + ch)

answer = ""
permute(input(), answer)