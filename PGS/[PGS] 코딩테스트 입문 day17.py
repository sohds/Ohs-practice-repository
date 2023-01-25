### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 17 문자열, 수학, 조건문, 배열, 사칙연산
# 숫자 찾기 (+2)
# 문제 설명 : 정수 num과 k가 매개변수로 주어질 때, 
# num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.
def solution(num, k):
    nums = list(str(num))
    answer = [ i+1 for i in range(0, len(nums)) if nums[i] == str(k) ]
    if str(k) not in nums:
        return -1
    else:
        return answer[0]


# n의 배수 고르기 (+1)
# 문제 설명 : 정수 n과 정수 배열 numlist가 매개변수로 주어질 때, 
# numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.

# my ver.
def solution(n, numlist):
    answer = [ numlist[i] for i in range(0, len(numlist)) if numlist[i] % n == 0 ]
    return answer

# lambda ver.
def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))
# lambda 공부해야하는데 ...


# 자릿수 더하기 (+1)
# 문제 설명 : 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요
def solution(n):
    answer = sum(list(map(int, str(n))))
    return answer


# OX퀴즈 (+2)
# 문제 설명 : 덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 
# 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.
def solution(quiz):
    return ['O' if eval(i.replace('=', '==')) else 'X' for i in quiz]