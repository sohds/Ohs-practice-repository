### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 1 사칙연산
# 두 수의 합 (+1)
def solution(num1, num2):
  answer = int(num1) + int(num2)
  return answer
  
# 두 수의 차 (+1)
def solution(num1, num2):
  answer = num1 - num2
  return answer
 
# 두 수의 곱 (+1)
def solution(num1, num2):
    return num1 * num2
    
# 몫 구하기 (+1)
solution = lambda num1, num2 : num1 // num2

## Day 2 사칙연산, 조건문, 배열
# 두 수의 나눗셈 (+2)
def solution(num1, num2):
    answer1 = (num1 / num2) * 1000
    answer = int(answer1)
    return answer
    
# 숫자 비교하기 (+1)
def solution(num1, num2):
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer
    
# 분수의 덧셈 (+9)
def solution(numer1, denom1, numer2, denom2):
    from fractions import Fraction
    f1 = Fraction(numer1, denom1)
    f2 = Fraction(numer2, denom2)
    f3 = f1 + f2
    answer = [f3.numerator, f3.denominator]
    return answer

# 배열 두 배 만들기
def solution(numbers):
    answer = []
    for i in numbers:
        k = i * 2
        answer.append(k)
    return answer
