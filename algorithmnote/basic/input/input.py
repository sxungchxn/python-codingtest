# input()으로 입력을 받으면 속도가 다소 느려서 성능상 좋지 못하다.
import sys

# input_line1 = sys.stdin.readline()
# print(f'input_line1 : {input_line1}')
# print(f'input_line1 len : {len(input_line1)}')


# # rstrip 함수를 같이 이용해야 개행문자를 제거할 수 있다.
# input_line2 = sys.stdin.readline().rstrip()
# print(f'input_line2 : {input_line2}')
# print(f'input_line2 len : {len(input_line2)}')


# 여러개의 정수를 입력 받기
a, b, c = map(int, sys.stdin.readline().rstrip().split())
print(a, b, c)


# 입력받은 정수를 리스트에 넣기
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
print(num_list)

# 함수로 저장해두면 편함


def readline():
    return sys.stdin.readline().rstrip()

#
