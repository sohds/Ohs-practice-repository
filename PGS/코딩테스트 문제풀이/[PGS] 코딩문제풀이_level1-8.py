### 코딩테스트 연습 > 연습문제 >
### 코딩테스트 연습 > 월간 코드 챌린지 시즌 2 >
### 코딩테스트 연습 > 위클리 챌린지 >


# 코딩테스트 level 1

# 문자열 내림차순으로 배치하기 (+1)
# 문제 설명 : 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

def solution(s):
    return (''.join(reversed(sorted(s))))



# 약수의 개수와 덧셈 (+1)
# 문제 설명 : 두 정수 left와 right가 매개변수로 주어집니다. 
# left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 
# 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

# my ver.
def solution(left, right):
    cnt = 0
    equation = ''
    for i in range(left, right+1):
        for k in range(1, i+1):
            if i % k == 0:
                cnt += 1
        if cnt % 2 == 0:
            equation += f'+{i}'
        else:
            equation += f'-{i}'
        cnt = 0
    return eval(equation)

# other ver.
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:    # 약수가 홀수개인 모든 수는 제곱수인 명제를 이용해서 푼 문제.
            answer -= i
        else:
            answer += i
    return answer



# 문자열 다루기 기본 (+4)
# 문제 설명 : 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
# 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
# 제한 사항 : s는 길이 1 이상, 길이 8 이하인 문자열입니다.
# s는 영문 알파벳 대소문자 또는 0부터 9까지 숫자로 이루어져 있습니다.

# my ver.
def solution(s):
    return s.isnumeric() if len(s) == 4 or len(s) == 6 else False

# other ver.
def alpha_string46(s):
    return s.isdigit() and len(s) in [4,6]  # 더 심플하네.. 한눈에 들어오기도 하고



# 부족한 금액 계산하기 (+3)
# 문제 설명 : 새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다. 
# 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 
# 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
# 단, 금액이 부족하지 않으면 0을 return 하세요.

# 제한사항 : 놀이기구의 이용료 price : 1 ≤ price ≤ 2,500, price는 자연수
# 처음 가지고 있던 금액 money : 1 ≤ money ≤ 1,000,000,000, money는 자연수
# 놀이기구의 이용 횟수 count : 1 ≤ count ≤ 2,500, count는 자연수

# my ver.
def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        answer += price * i
    return 0 if answer < money else answer - money

# other ver.
def solution(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))

# 산술평균 활용
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)



# 행렬의 덧셈 (+1)
# 문제 설명 : 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

# my ver.
def solution(arr1, arr2):
    answer = arr2
    for i in range(len(arr1[0])):
        for k in range(len(arr1)):
            answer[k][i] += arr1[k][i]
    return answer

# other ver.
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]  # zip 생각해보긴 했는데 그냥 이렇게 하면 되는구나..
    return answer



# 직사각형 별찍기 (+1)
# 문제 설명 : 이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다. 
# 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*'*a)