### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 6 문자열, 반복문, 출력, 배열, 조건문
# 문자열 뒤집기 (+1)
# 문제 설명 : 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(my_string):
    answer = my_string[::-1]
    return answer

# 직각삼각형 출력하기 (+1)
# 문제 설명 : "*"의 높이와 너비를 1이라고 했을 때, "*"을 이용해 직각 이등변 삼각형을 그리려고합니다. 
# 정수 n 이 주어지면 높이와 너비가 n 인 직각 이등변 삼각형을 출력하도록 코드를 작성해보세요.
n = int(input())

for i in range(1, n+1):
    print('*'*i)

# 짝수 홀수 개수 (+1)
# 문제 설명 : 정수가 담긴 리스트 num_list가 주어질 때, 
# num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(num_list):
    n_even = 0
    n_odd = 0
    for i in num_list:
        if i % 2 == 0:
            n_even += 1
        else:
            n_odd += 1
    answer = [n_even, n_odd]
    return answer

# 문자 반복 출력하기 (+4)
# 문제 설명 : 문자열 my_string과 정수 n이 매개변수로 주어질 때, 
# my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

# 해당 버전은 return 시켜주지 못했기 때문에 동일한 값을 출력시켜도 정답 처리가 불가능
def solution(my_string, n):
    for k in range(len(my_string)):
        print(my_string[k]*n, end = '')

# 정답
def solution(my_string, n):
    return ''.join(i*n for i in my_string)
            # join 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수
            # '구분자'.join(리스트)의 형태를 하고 있음