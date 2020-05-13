def bubble_sort(num):
    l = len(num)
    for i in range(l):
        for j in range(l-1-i): ## (l-i-1) is more efficient than (i-1) since last i elements are already sorted
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
        
    return num

num = [19,2,31,45,6,11,121,27]
print (bubble_sort(num))