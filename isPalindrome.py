# A palindrome is a word that is spelt the same backwards
def isPalindrome(word):
    word=word.lower()

    start_index=0
    end_index=len(word)-1

    for x in word:
        if word[start_index] != word[end_index]:
            return False
        start_index+=1
        end_index-=1
    return True

print(isPalindrome("python")) #false
print(isPalindrome("racecar")) #true
