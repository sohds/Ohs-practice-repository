### 코딩테스트 연습 > 연습문제 >
 
# 코딩테스트 level 1

# 정수 제곱근 판별 (+1)
# 문제 설명 : 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.
# 제한 사항: n은 1이상, 50000000000000 이하인 양의 정수입니다.

# my ver.
from math import sqrt

def solution(n):
    if sqrt(n) == int(sqrt(n)):
        return (sqrt(n)+1) ** 2
    else:
        return -1
    
# other ver.
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'



# x만큼 간격이 있는 n개의 숫자 (+1)
# 문제 설명 : 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 
# 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
# 제한 조건 : x는 -10000000 이상, 10000000 이하인 정수입니다. n은 1000 이하인 자연수입니다.

# my ver.
def solution(x, n):
    return [ i*x for i in range(1, n+1) ]



# 문자열을 정수로 바꾸기 (+1)
# 문제 설명 : 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.
# 제한 조건 : s의 길이는 1 이상 5이하입니다. s의 맨앞에는 부호(+, -)가 올 수 있습니다.
# s는 부호와 숫자로만 이루어져있습니다. s는 "0"으로 시작하지 않습니다.

# my ver.
def solution(s):
    if '-' in s:
        s = s[1:]
        s = int(s)
        return s * -1
    else:
        return int(s)
    
# other ver.
def strToInt(str): 
    result = 0
    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)
    return result