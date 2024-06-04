def partition(my_list: list[int], start_ind: int, end_ind: int) -> int:
    pivot_ind: int = start_ind
    pivot_ele: int = my_list[pivot_ind]

    while start_ind < end_ind:
        while start_ind < len(my_list) and pivot_ele >= my_list[start_ind]:
            start_ind += 1
        while pivot_ele < my_list[end_ind]:
            end_ind -= 1
        if start_ind < end_ind:
            my_list[start_ind], my_list[end_ind] = my_list[end_ind], my_list[start_ind]

    my_list[pivot_ind], my_list[end_ind] = my_list[end_ind], my_list[pivot_ind]

    return end_ind

def quick_sort(my_list: list[int], start_ind: int, end_ind: int) -> None:
    if start_ind < end_ind:
        partition_ind = partition(my_list, start_ind, end_ind)
        quick_sort(my_list, start_ind, partition_ind - 1)
        quick_sort(my_list, partition_ind + 1, end_ind)

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6]
    quick_sort(my_list, 0, len(my_list) - 1)
    print(my_list)