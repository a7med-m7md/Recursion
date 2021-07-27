def check(word, s, e):
    if word == '' or s>=e:
        return True
    if word[s] != word[e]:
        return False
    if word[s] == word[e]:
        return check(word, s+1, e-1)
    


word = 'a'
print(check(word, 0, len(word)-1))
    
