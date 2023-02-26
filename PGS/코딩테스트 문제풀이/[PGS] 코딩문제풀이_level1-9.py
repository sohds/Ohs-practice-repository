### 코딩테스트 연습 > 연습문제 >
### 코딩테스트 연습 > 스택/큐 >
### 코딩테스트 연습 > 월간 코드 챌린지 시즌1 >


# 코딩테스트 level 1


# 같은 숫자는 싫어 (+1)
# 문제 설명 : 배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 
# 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 
# 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 
# 예를 들면, arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
# arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

# first try.
# 코드 자체는 맞으나 효율성 테스트에서 fail.
# 배열에서 삭제하는 것이 조금 시간이 더 걸려서 바꿔서 재시도를 해봐야할 듯함.
def solution(arr):
    idx_list = [ i for i in range(1, len(arr)) if arr[i-1] == arr[i] ]
    cnt = 0
    for idx in idx_list:
        del arr[idx-cnt]
        cnt += 1
    return arr

# second try.
# 새롭게 배열을 만들어서 풀이. 효율성 테스트도 통과!
def solution(arr):
    new_arr = [ arr[i] for i in range(1, len(arr)) if arr[i-1] != arr[i] ]
    new_arr.insert(0, arr[0])
    return new_arr

# other ver.
# 스택/큐에 있던 문제로, stack을 적용해서 푼 문제라 가장 정답에 근접할듯.
def no_continuous(s):
    result = []
    for c in s:
        if len(result) == 0 or result[-1] != c:
            result.append(c)
    return result



# 최대공약수와 최소공배수 (+1)
# 문제 설명 : 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 
# 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
# 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

# my ver.
import math
def solution(n, m):
    if n > m:
        n, m = m, n
        
    common_divisor = [ i for i in range(1, m+1) if n % i == 0 and m % i == 0 ]
    gcd = max(common_divisor)
    
    answer = [gcd]
    
    for k in range(max(n, m), n*m+1):
        if k % n == 0 and  k % m == 0:
            answer.append(k)
            break
            
    return answer

# other ver.
# 유클라디안 알고리즘
def gcdlcm(a, b):
    c,d = max(a, b), min(a, b)
    t = 1
    while t>0:
        t = c%d
        c, d = d, t
    answer = [ c, int (a*b/c)]
    return answer



# 이상한 문자 만들기 (+6)
# 문제 설명 : 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
# 제한 사항 : 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

# my ver.
def solution(s):
    answer = ''
    new_list = s.split(' ')
    for i in new_list:
        for k in range(len(i)):
            if k % 2 == 0:
                answer += i[k].upper()
            else:
                answer += i[k].lower()
        answer+= ' '
    return answer[0:-1]

# other ver.
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))



# 3진법 뒤집기 (+1)
# 문제 설명 : 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 
# 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

# my ver.

def solution(n):
    answer = ''

    while n > 0:			
        n, re = divmod(n, 3)	# n을 3으로 나눈 몫과 나머지
        answer += str(re)
        
    return int(answer, 3)
# divmod() : 몫과 나머지를 리턴. 리턴 값이 2개이므로 튜플을 사용.
# int(x, base) : base 진법으로 구성된 str 형식의 수를 10진법으로 변환해 줌



# 시저 암호 (+3)
# 문제 설명 : 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
# 제한 조건 : 공백은 아무리 밀어도 공백입니다. s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# s의 길이는 8000이하입니다. n은 1 이상, 25이하인 자연수입니다.

# my ver.
# 넘나 비효율적인 것 ㅎ..
def solution(s, n):
    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    lower_list = list(alphabet.split())
    upper_list = list(alphabet.upper().split())
    
    idx = 0
    answer = ''
    
    for i in range(len(s)):
        if s[i] in lower_list:
            idx = lower_list.index(s[i])
            if idx+n >= len(lower_list):
                answer += lower_list[n-(len(lower_list) - idx)]
            else:   
                answer += lower_list[idx+n]
                
        elif s[i] in upper_list:
            idx = upper_list.index(s[i])
            if idx+n >= len(upper_list):
                answer += upper_list[n-(len(upper_list) - idx)]
            else:   
                answer += upper_list[idx+n]
            
        else:
            answer += ' '
    
    return answer

# other ver.
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

# ord(문자) : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
# ord('a')를 넣으면 정수 97을 반환합니다.

# chr(정수) : 하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환합니다.
# 인자(정수)의 유효 범위는 0 ~ 1,114,111 (16진수 0x10 FFFF)까지 입니다.
# chr(97)을 하면 문자 'a'를 반환합니다.

# if문과 elif문에서 +ord('A')나 +ord('a')를 왜 해주는지?
# 앞에서 %로 나머지를 구하면 0부터 25가 나오게 되는데 
# 아스키코드의 a는 시작 값은 97 A의 시작 값은 65이기 때문에 더해줌!
# 값을 더해줌으로써 chr로 형변환 했을 때 알파벳이 저장되기 때문.

# 더 공부가 필요하다.. 아스키코드를 몰라서 무슨 이야긴지 잘 이해가 가지 않는다!