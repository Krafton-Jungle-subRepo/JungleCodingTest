# 1, input().split() 사용자 입력 받아 리스트로 만듬 
# 2. map(int,...) 리스트의 각 요소를 정수로 변환
# 3. 변환된 정수를 a와 b에 할당  
a, b = map(int, input().split())

# 두 정수의 차를 계산하고 출력
print(a - b)