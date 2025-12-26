numbers=[1,34,56,23,56,40,1,2,7]
even=[]
odd=[]
for num in numbers:
    if num %2==0:
        even.append(num)
    else:
        odd.append(num)
print("even numbers:",even)
print("odd numbers:",odd)
