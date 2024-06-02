def selection_sort(element_list):
    for i in range(len(element_list)):
        min_ele = element_list[i]
        for j in range(i + 1, len(element_list)):
            if element_list[j] < min_ele:
                min_ele = element_list[j]
                element_list[i], element_list[j] = element_list[j], element_list[i]

if __name__ == '__main__':
    l = [5, 4, 3, 2, 1]
    selection_sort(l)
    print(l)