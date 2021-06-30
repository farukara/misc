#!python
# a recursive code that finds if a word is palindrome
# TODO can be improved to strip anything other than letters
# so that can accept any text.

ans =[]
def pal(stir):
    if len(stir) == 0 or len(stir) == 1:
        ans.append(True)
    elif len(stir) ==2:
        if stir[0] == stir[-1]:
            ans.append(True)
        else:
            ans.append(False)
    elif len(stir) > 2:
        if stir[0] == stir[-1]:
            pal(stir[1:-1])
        else:
            ans.append(False)
    return ans
print(pal("acrattarca"))
