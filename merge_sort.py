def sorted_merge(list1: list[int], list2: list[int]):
    i: int = 0
    j: int = 0

    sorted_list: list[int] = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1

    while i < len(list1):
        sorted_list.append(list1[i])
        i += 1

    while j < len(list2):
        sorted_list.append(list2[j])
        j += 1

    return sorted_list

def merge_sort(element_list):

    if len(element_list) <= 1:
        return element_list
    else:
        mid: int = len(element_list) // 2
        left: list[int] = element_list[:mid]
        right: list[int] = element_list[mid:]

        sorted_left: list[int] = merge_sort(left)
        sorted_right: list[int] = merge_sort(right)


        return sorted_merge(sorted_left, sorted_right)




if __name__ == '__main__':
    my_list = [6, 5, 4, 3, 2, 1]
    print(merge_sort(my_list))


    