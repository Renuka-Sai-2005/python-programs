s = [1,2,3,2,1]
is_palindrome = True
for i in range(len(s)//2):
    if s[i] != s[len(s)-1-i]:
        is_palindrome = False
        break
if is_palindrome:
    print("palindrome")
else:
    print("not palindrome")
