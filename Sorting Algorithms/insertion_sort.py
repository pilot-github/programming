def insertion_sort(num):
    for i in range(1, len(num)):
        key = num[i]
        print(f"Key: {key}")
        j = i-1

        while key < num[j] and j >= 0:
            num[j+1] = num[j]
            j = j-1
        num[j+1] = key
        print(num)

    return num

num = [19,2,31,45,6,11,121,27]
print(f"Original Input Array : {num}")
insertion_sort(num)
print(f"Final Output Array : {num}")





