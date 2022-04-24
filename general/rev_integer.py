# reverse the given integer

# input --> 123
# output --> 321

# input --> -123
# output --> -321

def rev_integer(num):
    is_negative = False
    rev_num = 0
    if num < 0:
        is_negative = True
        num = abs(num)
    while num:
        last_digit = num % 10
        num = num//10
        rev_num = rev_num*10 + last_digit
    return rev_num if not is_negative else -1*rev_num

print(rev_integer(-1239))