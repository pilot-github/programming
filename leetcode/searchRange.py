 def my_searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        for i in range(len(nums)):
            if target == nums[i] and first == -1:
                first = i
                last = i
                continue
            if first != -1 and target == nums[i]:
                last += 1
                
        return [first, last]
 
 
 def searchRange(self, arr, target):
        first = self.binarySearch(arr, 0, len(arr) -1,target, True)
        last = self.binarySearch(arr, 0, len(arr) -1, target, False)
        return [first, last]

    def binarySearch(self, arr, low, high, target, findFirst): #Recursion
        if high < low:
            return -1
        mid = low + (high - low)//2
        if findFirst:
            if(mid== 0 or target > arr[mid-1]) and arr[mid] == target:
                return mid
            if target > arr[mid]:
                return self.binarySearch(arr, mid+1, high, target, findFirst)
            else:
                return self.binarySearch(arr, low, mid-1, target, findFirst)
        
        else:
            if(mid==len(arr)-1 or target < arr[mid+1]) and arr[mid] == target:
                return mid
            elif target < arr[mid]:
                return self.binarySearch(arr, low, mid-1, target, findFirst)
            else:
                return self.binarySearch(arr, mid+1, high, target, findFirst)

    def binarySearchIterative(self, arr, low, high, target, findFirst):
        while True:
            if high<low:
                return -1
            mid = low + (high-low) // 2
            if findFirst:
                if(mid==0 or target>arr[mid-1]) and arr[mid] == target:
                    return mid
                if target > arr[mid]:
                    low = mid+1
                else:
                    high = mid -1
            
            else:
                if(mid== len(arr) -1 or target < arr[mid+1]) and arr[mid] == target:
                    return mid
                elif target< arr[mid]:
                    high = mid -1
                else:
                    low = mid +1
