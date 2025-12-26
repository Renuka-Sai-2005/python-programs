def find_missing(arr,n):
    for i in range(1,n+1):
        if i not in arr:
            return i
arr=[1,2,3,4,5]
n=6
print("missing numbers:",find_missing(arr,n))
