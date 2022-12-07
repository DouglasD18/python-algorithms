def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    index = 1
    while index <= len(word) // 2:
        if word[index - 1] != word[len(word) - index]:
            return False
        index += 1
    return True
