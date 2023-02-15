### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 13 문자열, 배열, 사칙연산, 수학, 조건문
# 컨트롤 제트 (+2)
# 문제 설명 : 숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다. 문자열에 있는 숫자를 차례대로 더하려고 합니다. 
# 이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다. 
# 숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.
# 입출력 예시 s: "-1 -2 -3 Z" | result: -3

# wrong ver.
# ValueError: invalid literal for int() with base 10: 'Z' <- Z는 int 가 될 수 없는 오류 발생
def solution(s):
    list_s = s.split()
    k = 0
    total = 0
    for i in list_s:
        if i == 'Z':
            total -= k
        total += int(i)
        k = int(i)
    return total

# studied ver.
# stack 자료구조: STACK (LIFO) 나중에 들어간 것이 먼저 나오는 자료구조, Last In First Out 착안 -> pop 사용
# isnumeric(), isdigit()의 경우 음수를 판별할 수 없기 때문에 해당 자료구조 사용!
def solution(s):
    stack = []
    for num in s.split():
        try:
            stack.append(int(num))
        except:
            if stack:        # stack에 데이터가 존재하면 실행
                stack.pop()
    return sum(stack)
# try ~ except 구조: try 먼저 시도할 때 error 안 나면 그대로 try 구문만, error 나면 except 구문으로 빠짐


# 배열 원소의 길이 (+1)
# 문제 설명 : 문자열 배열 strlist가 매개변수로 주어집니다. strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.
def solution(strlist):
    return [ len(strlist[i]) for i in range(len(strlist)) ]


# 중복된 문자 제거 (+1)
# 문제 설명 : 문자열 my_string이 매개변수로 주어집니다. 
# my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(my_string):
    answer = []
    for strin in list(my_string):
        if strin not in answer:
            answer.append(strin)
    return ''.join(answer)


# 삼각형의 완성조건(1) (+2)
# 문제 설명 : 선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다. 
# 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다. 삼각형의 세 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 
# 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요.
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2
