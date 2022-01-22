#Main Function
def SelectionSorting (arr, n):
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[min]>arr[j]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]

#Inputs
arr = [10,110,250,69,420,85]
n = len(arr)

#Calling our Function
SelectionSorting(arr,n)

#Printing The Function
print(arr)