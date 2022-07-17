def palindrome(num):
    if num<0:
        return False
    elif str(num) == str(num)[::-1]:
        return True
    else:
        return False
print(palindrome(121))