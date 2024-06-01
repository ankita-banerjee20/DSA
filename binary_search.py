def binary_search(element_list, value, left_index, right_index):
    element_list.sort()

    if left_index >  right_index:
        return -1
    
    mid_index = (left_index + right_index) // 2

    if element_list[mid_index] == value:
        return mid_index
    
    elif element_list[mid_index] > value:
        right_index = mid_index - 1

    elif element_list[mid_index] < value:
        left_index = mid_index + 1
    
    return binary_search(element_list, value, left_index, right_index)
    

if __name__ == '__main__':
    element_list = [4, 8, 2, 3, 1]
    print(binary_search(element_list, 1, 0, len(element_list) - 1))