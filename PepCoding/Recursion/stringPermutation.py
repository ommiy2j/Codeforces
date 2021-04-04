def printPermutation(s, ans):
    if len(s) == 0:
        print(ans)
        return
    for i in range(len(s)):
        ch = s[i]
        ros = s[0:i] + s[i + 1 :]
        printPermutation(ros,ans+ch)
        




s = input()
printPermutation(s, '')

