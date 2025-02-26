N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

for a in range(N - M + 1):
    for b in range(N - M + 1):
        for k in range(M):
            if S[a + k][b:b + M] != T[k]:
                break
        else:
            print(a+1, b+1)
