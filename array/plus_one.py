def plusOne(digits):
        i = len(digits)-1
        carry = 0
        while i >= 0:
            new_num = digits[i] + 1 if i == len(digits)-1 else digits[i] + carry
            if new_num > 9:
                digits[i] = new_num % 10
                carry = 1 if i!=0 else digits.insert(0,1)
            else:
                carry = 0 
                digits[i] = new_num
            i -= 1
        return digits

print(plusOne([9,9]))
# print(plusOne([1,2,3]))