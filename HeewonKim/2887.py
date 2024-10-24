# 행성 터널
import sys
import heapq

N = int(sys.stdin.readline())
nodeX = []
nodeY = []
nodeZ = []
for i in range(1, N+1):
    X, Y, Z = map(int, sys.stdin.readline().split())
    nodeX.append([X, i])
    nodeY.append([Y, i])
    nodeZ.append([Z, i])

edge = []

nodeX.sort()
nodeY.sort()
nodeZ.sort()

for i in range(N-1):
    distance = abs(nodeX[i][0]-nodeX[i+1][0])
    heapq.heappush(edge, [distance, nodeX[i][1], nodeX[i+1][1]])

    distance = abs(nodeY[i][0]-nodeY[i+1][0])
    heapq.heappush(edge, [distance, nodeY[i][1], nodeY[i+1][1]])

    distance = abs(nodeZ[i][0]-nodeZ[i+1][0])
    heapq.heappush(edge, [distance, nodeZ[i][1], nodeZ[i+1][1]])

parent = [i for i in range(N+1)]
rank = [0] * (N+1)
res = 0

def FindRoot(node):
    if node != parent[node]:
        parent[node] = FindRoot(parent[node])  
    return parent[node]

def CompareRoot(Node1, Node2):
    root1 = FindRoot(Node1)
    root2 = FindRoot(Node2)

    if(root1 == root2):
        return True
    
    if(rank[root1] > rank[root2]):
        parent[root2] = root1
    elif(rank[root2] > rank[root1]):
        parent[root1] = root2
    else:
        parent[root1] = root2
        root2 += 1
    return False

count = 1
while(edge):
    if(count == N):
        break
    cost, poppedNode1, poppedNode2 = heapq.heappop(edge)
    if(not CompareRoot(poppedNode1, poppedNode2)):
        res += cost
        count += 1

print(res)


