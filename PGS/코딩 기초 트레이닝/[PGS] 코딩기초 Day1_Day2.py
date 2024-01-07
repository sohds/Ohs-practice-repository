### 1. 문자열 출력하기   (+1)
## 문제 설명
## 문자열 str이 주어질 때, str을 출력하는 코드를 작성해 보세요.

str = input()
print(str)


### 2. a와 b 출력하기  (+1)
## 문제 설명
## 정수 a와 b가 주어집니다. 
## 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.

a, b = map(int, input().strip().split(' '))
# print('a =', a)
# print('b =', b)
print('a = %d\nb = %d' % (a, b))


### 3. 문자열 반복해서 출력하기  (+1)
## 문제 설명
## 문자열 str과 정수 n이 주어집니다.
## str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.
a, b = input().strip().split(' ')
b = int(b)

print(a*b)


### 4. 대소문자 바꿔서 출력하기  (+1)
## 문제 설명
## 영어 알파벳으로 이루어진 문자열 str이 주어집니다. 
## 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.
str = input()
print(str.swapcase())
# print(''.join(x.upper() if x == x.lower() else x.lower() for x in input()))


### 5. 특수문자 출력하기   (+1)
## 문제 설명
## 다음과 같이 출력하도록 코드를 작성해 주세요.
print("!@#$%^&*(\\'\"<>?:;")


### 6. 덧셈식 출력하기    (+1)
## 문제 설명
## 두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.
## a + b = c
a, b = map(int, input().strip().split(' '))
c = a + b
print(a, '+', b, '=', c)
# print("%d + %d = %d", % (a, b, a+b))

# a, b = map(int, input().strip().split(' '))
# print(f"{a} + {b} = {a + b}")


### 7. 문자열 붙여서 출력하기   (+1)
## 문제 설명
## 두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다.
## 입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.
str1, str2 = input().strip().split(' ')

result = str1 + str2

print(result)
# print(input().strip().replace(' ', ''))


### 8. 문자열 돌리기   (+1)
## 문제 설명
## 문자열 str이 주어집니다.
## 문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.
str = input()
str = list(str)

for i in str:
    print(i)

# print('\n'.join(input()))


#!# 9. 홀짝 구분하기    (+1)
## 문제 설명
## 자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 
# 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.
a = int(input())

if a % 2 == 0:
    print(a, 'is even')
else:
    print(a, 'is odd')
    
# n = int(input())
# print(f"{n} is odd" if n % 2 else f"{n} is even")


### 10. 문자열 겹쳐쓰기   (+1)
## 문제 설명
## 문자열 my_string, overwrite_string과 정수 s가 주어집니다. 
# 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 
# 문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer