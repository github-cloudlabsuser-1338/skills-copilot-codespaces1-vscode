def mergesort(list):
    if len(list) <= 1:
        return list
    # Find the middle point and divide it
    middle = len(list) // 2
    left_list = list[:middle]
    right_list = list[middle:]

    left_list = mergesort(left_list)
    right_list = mergesort(right_list)

    return list(merge(left_list, right_list))