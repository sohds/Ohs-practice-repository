### 코딩테스트 연습 > 연습문제 >
 
# 코딩테스트 level 1

# 짝수와 홀수 (+1)
# 문제 설명 : 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.
# 제한 조건 : num은 int 범위의 정수입니다. 0은 짝수입니다.

def solution(num):
    return 'Even' if num % 2 == 0 else 'Odd'



# 평균 구하기 (+1)
# 문제 설명 : 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
# 제한사항 : arr은 길이 1 이상, 100 이하인 배열입니다. arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.

def solution(arr):
    return sum(arr) / len(arr)
    # print("평균값 : {}".format(average(list)))



# 자릿수 더하기 (+1)
# 문제 설명 : 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
# 제한사항: N의 범위: 100,000,000 이하의 자연수

# my ver.
def solution(n):
    n = str(n)
    n_list = list(map(int, list(n)))
    return sum(n_list)

# short ver.
def sum_digit(number):
    return sum([int(i) for i in str(number)])



# 약수의 합 (+1)
# 문제 설명 : 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
# 제한 사항 : n은 0 이상 3000이하인 정수입니다.

# my ver.
def solution(n):
    answer = [ i for i in range(1, n+1) if n % i == 0 ]
    return sum(answer)

# short cut.
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상!
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])



# 자연수 뒤집어 배열로 만들기 (+1)
# 문제 설명 : 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
# 제한 조건 : n은 10,000,000,000이하인 자연수입니다.

# my ver.
def solution(n):
    n = str(n)
    return list(map(int, n[::-1]))

# other ver.
def digit_reverse(n):
    return list(map(int, reversed(str(n))))



# 문자열 내 p와 y의 개수 (+2)
# 문제 설명 : 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
# s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
# 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.
# 제한사항 : 문자열 s의 길이: 50 이하의 자연수, 문자열 s는 알파벳으로만 이루어져 있습니다.

# my ver.
def solution(s):
    num_p = s.count('p') + s.count('P')
    num_y = s.count('y') + s.count('Y')
    return True if num_p == num_y else False

# other ver.
# 전부 lower로 바꿔주고 count
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')

# Counter 사용해도 됨!
from collections import Counter
def numPY(s):
    c = Counter(s.lower())
    return c['y'] == c['p']