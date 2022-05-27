import re
def palindrome(word):
    word = str(word).lower()
    word = re.sub("\W", '', word)
    return True if word == word[::-1] else False
