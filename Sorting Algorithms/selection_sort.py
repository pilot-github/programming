def selection_sort(num):
    for i in range(len(num)):
        min_index = i
        for j in range(min_index+1, len(num)):
            if num[min_index] > num[j]:
                min_index = j
        
        num[i], num[min_index] = num[min_index], num[i]

    return num

num = [19,2,31,45,6,11,121,27]
print (selection_sort(num))