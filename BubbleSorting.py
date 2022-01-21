#Main Function
def BubbleSorting (arr, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if(arr[j+1]<arr[j]):
                arr[j+1], arr[j] = arr[j], arr[j+1]

#Inputs
arr = [10,110,250,69,420,85]
n = len(arr)

#Calling our Function
BubbleSorting(arr,n)

#Printing The Function
print(arr)