### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 1 사칙연산
# 두 수의 합 (+1)
# 문제 설명 : 정수 num1과 num2가 주어질 때, num1과 num2의 합을 return하도록 soltuion 함수를 완성해주세요.
def solution(num1, num2):
  answer = int(num1) + int(num2)
  return answer
  
# 두 수의 차 (+1)
# 문제 설명 : 정수 num1과 num2가 주어질 때, num1에서 num2를 뺀 값을 return하도록 soltuion 함수를 완성해주세요.
def solution(num1, num2):
  answer = num1 - num2
  return answer
 
# 두 수의 곱 (+1)
# 문제 설명 : 정수 num1, num2가 매개변수 주어집니다. num1과 num2를 곱한 값을 return 하도록 solution 함수를 완성해주세요.
def solution(num1, num2):
    return num1 * num2
    
# 몫 구하기 (+1)
# 문제 설명 : 정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.
solution = lambda num1, num2 : num1 // num2

## Day 2 사칙연산, 조건문, 배열
# 두 수의 나눗셈 (+2)
# 문제 설명 : 정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 soltuion 함수를 완성해주세요.
def solution(num1, num2):
    answer1 = (num1 / num2) * 1000
    answer = int(answer1)
    return answer
    
# 숫자 비교하기 (+1)
# 문제 설명 : 정수 num1과 num2가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.
def solution(num1, num2):
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer
    
# 분수의 덧셈 (+9)
# 문제 설명 : 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 
# 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(numer1, denom1, numer2, denom2):
    from fractions import Fraction
    f1 = Fraction(numer1, denom1)
    f2 = Fraction(numer2, denom2)
    f3 = f1 + f2
    answer = [f3.numerator, f3.denominator]
    return answer

# 배열 두 배 만들기 (+1)
# 문제 설명 : 정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
def solution(numbers):
    answer = []
    for i in numbers:
        k = i * 2
        answer.append(k)
    return answer
