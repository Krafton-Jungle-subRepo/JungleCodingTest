# 2920 - 음계
import sys
input = sys.stdin.readline

# 문자열 입력
music = input().strip()
# ascending, descending 선언 후 비교
ascending = '1 2 3 4 5 6 7 8'
descending = '8 7 6 5 4 3 2 1'
# 결과 출력
if music == ascending:
    print("ascending")
elif music == descending:
    print("descending")
else:
    print("mixed")