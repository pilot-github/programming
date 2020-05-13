def merge(left_list, right_list):
    res = []

    while len(left_list) != 0 and len(right_list) != 0:
        if left_list[0] < right_list[0]:
            res.append(left_list[0])
            left_list.remove(left_list[0])
        elif left_list[0] > right_list[0]: 
            res.append(right_list[0])
            right_list.remove(right_list[0])

    if len(left_list) > 0:
        res = res + left_list
    if len(right_list) > 0:
        res = res + right_list
    return res


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    middle = len(unsorted_list) // 2
    left_list = merge_sort(unsorted_list[:middle])
    right_list = merge_sort(unsorted_list[middle:])

    return merge(left_list, right_list)


num = [19,2,31,45,6,11,121,27]
print (merge_sort(num))