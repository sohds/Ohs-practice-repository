### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 12 문자열, 정렬, 사칙연산, 수학
# 모음 제거 (+1)
# 문제 설명 : 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 
# 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

# solved ver.
def solution(my_string):
    my_lsstring = list(my_string)
    while 'a' in my_lsstring:
        my_lsstring.remove('a')
    while 'e' in my_lsstring:
        my_lsstring.remove('e')
    while 'i' in my_lsstring:
        my_lsstring.remove('i')
    while 'o' in my_lsstring:
        my_lsstring.remove('o')
    while 'u' in my_lsstring:
        my_lsstring.remove('u')
    return ''.join(my_lsstring)

# short ver.
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])


# 문자열 정렬하기(1) (+1)
# 문제 설명 : 문자열 my_string이 매개변수로 주어질 때, 
# my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.

# solved ver.
def solution(my_string):
    my_string = list(my_string)
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    result = [ int(i) for i in my_string if i in numbers ]
    result.sort(reverse=False)
    return result

# short ver.
def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])  
    # .isdigit() 문자열이 숫자(digit)로만 구성되어있으면 true를 리턴하며, 그렇지 않으면 false를 리턴


# 숨어있는 숫자의 덧셈 (1) (+1)
# 문제 설명 : 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
def solution(my_string):
    return sum(int(c) for c in my_string if c.isdigit())


# 소인수분해 (+9)
# 문제 설명 : 소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 
# 예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 따라서 12의 소인수는 2와 3입니다. 
# 자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
def solution(n):
    prime = []
    answer = []
    
    i = 2
    
    while i <= n:
        if n % i == 0:
            prime.append(i)
            n = n // i
        else:
            i += 1
    
    for i in prime:
        if i not in answer:
            answer.append(i)
            
    return answer