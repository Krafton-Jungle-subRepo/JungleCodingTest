# 사용자 입력 받기 
a, b, c = map(int,(input().split()))

# 나머지 출력하기 
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
