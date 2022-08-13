import re
def palindrome(word):
    word = str(word).lower()
    word = re.sub("\W", '', word)
    return True if word == word[::-1] else False


def palindrome_r(word):
    
    def is_palindrome(input_str):
        if len(input_str) == 0:
            return ''
        return f"{input_str[-1]}{is_palindrome(input_str[:len(input_str)-1])}"
        
    my_word = word.lower()
    re.sub('\W', '', word)
    return my_word == is_palindrome(my_word)


print(palindrome_r("racecar racecar"))
