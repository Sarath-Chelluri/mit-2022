s = input("enter something: ")
count = 0
num = 0
for i in s:
    try:
        if s[num] == "b" and s[num + 1] == "o" and s[num + 2] == "b":
            count += 1
    except:
        break
    num += 1
print(f"number of bobs = {count}")
