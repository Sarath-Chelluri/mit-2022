s = input("enter something ")
x = []
substring = " "
for i in s:
    y = len(substring)

    if substring[y - 1] <= i:
        if substring == " ":
            substring = ""
        substring += i
    else:
        x.append(substring)
        substring = i

lst2 = sorted(x, key=len)
print(lst2[-1])
