s = input()
count = 0
for i in range(len(s) - 2):
    j = 1
    while i + 2*j < len(s):
        if s[i] + s[i+j] + s[i+2*j] == "ABC":
            count += 1
        j += 1

print(count)