def is_palindrome_recursive(word, low_index, high_index):
    if high_index == -1:
        return False

    if word[low_index] != word[high_index]:
        return False
    elif high_index > 1:
        return is_palindrome_recursive(word[1:high_index], 0, high_index - 2)
    else:
        return True
