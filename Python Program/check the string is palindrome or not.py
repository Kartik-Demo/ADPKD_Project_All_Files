def ispalindrome (s):
    s= s.lower()
    l=len(s)
    if l< 2 :
        return True
    elif s[0] == s[l-1]:
        return ispalindrome(s[1 : l - 1])
    else :
        return False
s=input("\n Enter Your String:-")
ans = ispalindrome (s)
if ans :
    print("\n Yes This String Is A palindrome")
else :
    print("\n No This String Is Note A Palindrome")
