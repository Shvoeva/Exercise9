def isPalindrome(word):
    '''
    Returns True if the word is a palindrome, otherwise False
    NOTE: returns False if the word consists of capital letters
    and/or other characters
    '''

    if not (word.isalpha() and word.islower()):
        return False

    upsideDownWord = word[::-1]
    if word == upsideDownWord:
        return True
    return False

if __name__ == '__main__':
    assert isPalindrome('lol') == True
    assert isPalindrome('hi') == False
    assert isPalindrome('l o l') == False
    assert isPalindrome('LOL') == False
    assert isPalindrome('404') == False