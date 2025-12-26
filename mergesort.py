s1 = [1,2,5,7]
s2 = [3,6,7,9,6]
i = 0
j = 0
res = []
while i < len(s1) and j < len(s2):
    if s1[i] < s2[j]:
        res.append(s1[i])
        i += 1
    else:
        res.append(s2[j])
        j += 1
res += s1[i:]
res += s2[j:]
print(res)
