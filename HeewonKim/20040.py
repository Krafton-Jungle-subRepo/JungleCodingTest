# 사이클 게임
import sys

N, M = map(int, sys.stdin.readline().split())
line = []
for _ in range(M):
    line.append(list(map(int, sys.stdin.readline().split())))

parent = [i for i in range(N)]
res = 0
count = 1

def FindRoot(node):
    if(parent[node] != node):
        parent[node] = FindRoot(parent[node])
    return parent[node]

def FindeParent(node1, node2):
    root1 = FindRoot(node1)
    root2 = FindRoot(node2)

    if(root1 == root2):
        return True
    if root1 < root2:
        parent[root2] = root1
    else:
        parent[root1] = root2
    return False


for node1, node2 in line:
    if(FindeParent(node1, node2 )):
        res = count
        break
    count += 1
print(res)