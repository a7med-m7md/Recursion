def decimalToBinary(num, result):
    if num%2 == 1:
        result = str(1) + result
    else:
        result = str(0) + result
    if num != 0:
        return decimalToBinary(num//2, result)
    return result
        
print(decimalToBinary(100, ''))
