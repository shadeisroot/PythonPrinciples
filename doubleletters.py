def double_letters(word):
    for i in range (len(word)-1):
        print(word)
        if word[i] == word[i+1]:
            print(i)
            return True
    return False

print(double_letters("Error"))