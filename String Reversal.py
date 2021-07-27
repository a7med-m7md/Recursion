def string_reversal(word, index):
    if index == -1:
        return ''
    return str(word[index]) + string_reversal(word, index - 1) 

print(string_reversal('ahmed', len('ahmed')-1))
