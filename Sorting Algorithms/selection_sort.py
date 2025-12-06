def selection_sort(num):
    for i in range(len(num)):
        min_index = i
        for j in range(min_index+1, len(num)):
            if num[j] < num[min_index]:
                min_index = j
        
        print(f"Min Index: {min_index}, Value: {num[min_index]}")
        num[i], num[min_index] = num[min_index], num[i]
        print(num)
    return num

num = [19,2,31,45,6,11,121,27]

print (f"Original Input Array : {num}")
selection_sort(num)
print (f"Final Output : {num}")

