import sys
input = sys.stdin.readline

N, M = map(int,input().split())

pokemons = {}

for i in range(N):
    pokemons[i+1] = input().rstrip()

tmp = {v:k for k, v in pokemons.items()}

for i in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(pokemons[int(question)])
    else:
        print(tmp[question])
