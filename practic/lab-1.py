j = input()
s = input()
result = 0
for i in j:
    for k in s:
        if i == k:
            result += 1
print(result)
