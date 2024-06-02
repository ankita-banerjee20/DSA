def insertion_sort(element_list):
    for i in range(1, len(element_list)):
        anchor = element_list[i]
        for j in range(i - 1, -1, -1):
            if anchor < element_list[j]:
                element_list[j], element_list[j + 1] = element_list[j + 1], element_list[j]

            
                

if __name__ == '__main__':
    l = [5, 15, 3, 2, 1]
    insertion_sort(l)
    print(l)



