#Main Function
def LinearSearch (arr, n, x):
    for i in range(0, n):
        if arr[i]==x:
            return i
    return -1

#Inputs
arr = [10,110,250,69,420,85]
n = len(arr)
x = 69

#Calling our Function
result = LinearSearch(arr,n,x)

#Printing Output
if (result==-1):
    print("Element Not Found in the list")
else:
    print("Element Found at index ", result, " in the list")