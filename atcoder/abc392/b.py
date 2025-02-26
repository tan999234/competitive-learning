n, m = map(int, input().split())
a = list(map(int, input().split()))

#setは順番を保証しないので、sortedでソートする
numbers = sorted(set(range(1, n+1)) - set(a))

print(len(numbers))
#joinは呼び出し元を区切り文字として、引数の文字のシーケンスの中身を連結する
print(" ".join(map(str, numbers)))
