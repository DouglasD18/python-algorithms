def merge_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid, end)
        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            arr[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            arr[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            arr[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            arr[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    first = first_string.lower()
    second = second_string.lower()
    if first_string == '' and second_string == '':
        return ('', '', False)
    first_list = list(first)
    second_list = list(second)
    merge_sort(first_list)
    merge_sort(second_list)
    first_ana = ''.join(first_list)
    second_ana = ''.join(second_list)
    return (first_ana, second_ana, first_ana == second_ana)


if __name__ == '__main__':
    result = is_anagram('pedra', 'perda')
    print(result)
