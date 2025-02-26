n = int(input())
words = []

for i in range(n):
    words.append(input())

sorted_words = sorted(words, key=len)

print("".join(sorted_words))