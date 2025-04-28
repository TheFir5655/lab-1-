s = "Камни"
j = "Драгоценности"
count = 0
for i in s:
    if i in j:
        count +=1
print(f"Входит столько символов: {count} в из {s} в {j}")
