a = list(map(int, input().split()))

flag = False
for i in range(len(a) - 1):
    for j in range(i+1, len(a)):
        if a[i] * a[j] == a[3 - i - j]:
            flag = True

if flag:
    print("Yes")
else:
    print("No")