def insertion_sort(num):
    for i in range(1, len(num)):
        next = num[i]
        j = i-1

        while next < num[j] and j >= 0:
            num[j+1] = num[j]
            j = j-1
            print(num)
        num[j+1] = next

    return num

num = [19,2,31,45,6,11,121,27]

print (insertion_sort(num))
