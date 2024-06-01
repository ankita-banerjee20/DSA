def bubble_sort(element_list):
    for i in range(len(element_list)):
        for i in range(len(element_list) - 1):
            if element_list[i] > element_list[i + 1]:
                element_list[i], element_list[i + 1] = element_list[i + 1], element_list[i]

if __name__ == '__main__':
    l = [5, 4, 3, 2, 1]
    bubble_sort(l)
    print(l)