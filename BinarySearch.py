def BinarySearch (arr, n , x):
    low = 0
    high = n - 1
    while low <= high:
        mid = int((high + low)/2)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = high - 1
    return -1

#Inputs
arr = [1,54,69,120,252,368,420]
n = len(arr)
x = 120

#Function Call
Result = BinarySearch(arr, n, x)

#Checking
if Result == -1:
    print("Number Not Found ")
else:
    print("Number Found at index ", Result)