### 11. 문자열 섞기   (+1)
## 문제 설명
## 길이가 같은 두 문자열 str1과 str2가 주어집니다.
## 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 
## return 하는 solution 함수를 완성해 주세요.
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i]
        answer += str2[i]
    return answer

# def solution(str1, str2):
#     answer = ''.join([str1[i] + str2[i] for i in range(len(str1))])
#     return answer


### 12. 문자 리스트를 문자열로 변환하기  (+1)
## 문제 설명
## 문자들이 담겨있는 배열 arr가 주어집니다. 
# arr의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(arr):
    answer = ''.join(arr)
    return answer


### 13. 문자열 곱하기   (+1)
## 문제 설명
## 문자열 my_string과 정수 k가 주어질 때, 
# my_string을 k번 반복한 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, k):
    return my_string * k


### 14. 더 크게 합치기   (+1)
## 문제 설명
## 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 
## 예를 들면 다음과 같습니다.

## 12 ⊕ 3 = 123
## 3 ⊕ 12 = 312
## 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.
## 단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.

def solution(a, b):
    a, b = str(a), str(b)
    res1, res2 = a + b, b + a
    
    if int(res1) > int(res2):
        return int(res1)
    else:
        return int(res2)
    
# simply
# def solution(a, b):
#    a, b = str(a), str(b)
#    return int(max(a+b, b+a))



### 15. 두 수의 연산값 비교하기  (+1)
## 문제 설명
## 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

## 12 ⊕ 3 = 123
## 3 ⊕ 12 = 312
## 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 2 * a * b 중 더 큰 값을 return하는 solution 함수를 완성해 주세요.

## 단, a ⊕ b와 2 * a * b가 같으면 a ⊕ b를 return 합니다.
def solution(a, b):
    res1 = int(str(a)+str(b))
    res2 = 2 * a * b
    return max(res1, res2)


### 16. n의 배수   (+1)
## 문제 설명
## 정수 num과 n이 매개 변수로 주어질 때, 
# num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.
def solution(num, n):
    return 1 if num % n == 0 else 0

# bool 사용법
# def solution(num, n):
#     return int(not(num % n))


### 17. 공배수    (+1)
## 문제 설명
## 정수 number와 n, m이 주어집니다. 
# number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.
def solution(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0
    # return int(number % n == 0 and number % m == 0)
    
    
    
### 18. 홀짝에 따라 다른 값 반환하기    (+1)
## 문제 설명
## 양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 
# n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.
def solution(n):
    answer = 0
    
    if n % 2 == 0:
        for i in range(1, n+1):
            if i % 2 == 0:
                answer += i**2
    
    else:
        for i in range(1, n+1):
            if i % 2 == 1:
                answer += i
                
    return answer

# 제곱의 합 공식..
# def solution(n):
#    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)



### 19. 조건 문자열   (+1)
## 문제 설명
## 문자열에 따라 다음과 같이 두 수의 크기를 비교하려고 합니다.

## 두 수가 n과 m이라면
## ">", "=" : n >= m
## "<", "=" : n <= m
## ">", "!" : n > m
## "<", "!" : n < m
##  두 문자열 ineq와 eq가 주어집니다. ineq는 "<"와 ">"중 하나고, eq는 "="와 "!"중 하나입니다. 
# 그리고 두 정수 n과 m이 주어질 때, n과 m이 ineq와 eq의 조건에 맞으면 1을 아니면 0을 return하도록 solution 함수를 완성해주세요.
def solution(ineq, eq, n, m):
    equation = str(n) + ineq
    if eq == '=':
        equation += eq + str(m)
    else:
        equation += str(m)
    return int(eval(equation))

# simple
# def solution(ineq, eq, n, m):
#     return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))



### 20. flag에 따라 다른 값 반환하기  (+1)
## 문제 설명
## 두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, 
# flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.
def solution(a, b, flag):
    return a+b if flag == True else a-b