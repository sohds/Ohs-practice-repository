### 21. 코드 처리하기   (+2)
## 문제 설명
## 문자열 code가 주어집니다.
## code를 앞에서부터 읽으면서 만약 문자가 "1"이면 mode를 바꿉니다. mode에 따라 code를 읽어가면서 문자열 ret을 만들어냅니다.

## mode는 0과 1이 있으며, idx를 0 부터 code의 길이 - 1 까지 1씩 키워나가면서 code[idx]의 값에 따라 다음과 같이 행동합니다.

## mode가 0일 때
## code[idx]가 "1"이 아니면 idx가 짝수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
## code[idx]가 "1"이면 mode를 0에서 1로 바꿉니다.
## mode가 1일 때
## code[idx]가 "1"이 아니면 idx가 홀수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
## code[idx]가 "1"이면 mode를 1에서 0으로 바꿉니다.
## 문자열 code를 통해 만들어진 문자열 ret를 return 하는 solution 함수를 완성해 주세요.

## 단, 시작할 때 mode는 0이며, return 하려는 ret가 만약 빈 문자열이라면 대신 "EMPTY"를 return 합니다.


def solution(code):
    mode = 0
    ret = ''
    
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] == '1':
                mode = 1
            elif code[idx] != '1' and idx % 2 == 0:
                ret += code[idx]
                
        else:
            if code[idx] == '1':
                mode = 0
            elif code[idx] != '1' and idx % 2 == 1:
                ret += code[idx]
    
    if len(ret) != 0:
        return ret
    else:
        return 'EMPTY'
    
    

### 22. 등차수열의 특정한 항만 더하기   (+1)
## 문제 설명
## 두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다. 첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때, 이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.

def solution(a, d, included):
    seq = [ a+(idx-1)*d for idx in range(1, len(included)+1) ]
    hap = 0
    for i,(a,n) in enumerate(zip(seq, included)):
        # print(i,a,n)
        if n:
            hap += a
    return hap

# simple
# def solution(a, d, included):
#    return sum(a + i * d for i, f in enumerate(included) if f)



### 23. 주사위 게임 2   (+1)
## 문제 설명
## 1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.

## 세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
## 세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
## 세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
## 세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

def solution(a, b, c):
    if a == b and b == c and c == a:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a != b and b != c and c != a:
        return a + b + c
    else:
        return (a + b + c) * (a**2 + b**2 + c**2)
    
# set로 동일값 추출하는 방법도 존재!
# def solution(a, b, c):
#     check=len(set([a,b,c]))
#     if check==1:
#         return 3*a*3*(a**2)*3*(a**3)
#     elif check==2:
#         return (a+b+c)*(a**2+b**2+c**2)
#     else:
#         return (a+b+c)



### 24. 원소들의 곱과 합   (+1)
## 문제 설명
## 정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 
## 크면 0을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    times, hap = 1, 0
    
    for idx in range(len(num_list)):
        times *= num_list[idx]
        hap += num_list[idx]
        
    f_hap = hap ** 2
    
    return 1 if times < f_hap else 0



### 25. 이어 붙인 수   (+1)
## 문제 설명
## 정수가 담긴 리스트 num_list가 주어집니다. n
## um_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    odd = [ str(n) for n in num_list if n%2==0 ]
    even = [ str(n) for n in num_list if n%2==1 ]
    odd, even = ''.join(odd), ''.join(even)
    return int(odd) + int(even)



### 26. 마지막 두 원소   (+1)
## 문제 설명
## 정수 리스트 num_list가 주어질 때, 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을 
## 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(num_list[-1] * 2)
    return num_list



### 27. 수 조작하기 1   (+1)
## 문제 설명
## 정수 n과 문자열 control이 주어집니다. 
# control은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며, control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.

## "w" : n이 1 커집니다.
## "s" : n이 1 작아집니다.
## "d" : n이 10 커집니다.
## "a" : n이 10 작아집니다.
## 위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return 하는 solution 함수를 완성해 주세요.

def solution(n, control):
    control = list(control)
    
    for letter in control:
        if letter == 'w':
            n += 1
        elif letter == 's':
            n -= 1
        elif letter == 'd':
            n += 10
        elif letter == 'a':
            n -= 10
            
    return n

# simple
# def solution(n, control):
#     key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
#     return n + sum([key[c] for c in control])



### 28. 수 조작하기 2    (+1)
## 문제 설명
## 정수 배열 numLog가 주어집니다. 
# 처음에 numLog[0]에서 부터 시작해 "w", "a", "s", "d"로 이루어진 문자열을 입력으로 받아 순서대로 다음과 같은 조작을 했다고 합시다.

## "w" : 수에 1을 더한다.
## "s" : 수에 1을 뺀다.
## "d" : 수에 10을 더한다.
## "a" : 수에 10을 뺀다.
## 그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 numLog입니다. 
## 즉, numLog[i]는 numLog[0]로부터 총 i번의 조작을 가한 결과가 저장되어 있습니다.

## 주어진 정수 배열 numLog에 대해 조작을 위해 입력받은 문자열을 return 하는 solution 함수를 완성해 주세요.

def solution(numLog):
    answer = ''
    real = [ numLog[idx] - numLog[idx-1] for idx in range(1, len(numLog))]
    key = dict(zip([1, -1, 10, -10], ['w', 's', 'd', 'a']))
    for n in real:
        answer += key[n]
    return answer



### 29. 수열과 구간 쿼리 3    (+1)
## 문제 설명
## 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [i, j] 꼴입니다.
## 각 query마다 순서대로 arr[i]의 값과 arr[j]의 값을 서로 바꿉니다.
## 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.
def solution(arr, queries):
    for i in queries:
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]
    
    return arr



### 30. 수열과 구간 쿼리 2    (+1)
## 문제 설명
## 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.

## 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i]를 찾습니다.

## 각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수를 완성해 주세요.
## 단, 특정 쿼리의 답이 존재하지 않으면 -1을 저장합니다.
def solution(arr, queries):
    result = []
    for query in queries:
        temp_list = []
        for i in range(query[0], query[1] + 1):
            if arr[i] > query[2]:
                temp_list.append(arr[i])
        try:   
            result.append(min(temp_list))
        except:
            result.append(-1)
    return result

# bit simple
# def solution(arr, queries):
#     answer = []
#     for s, e, k in queries:
#         l = [i for i in arr[s:e+1] if i > k]
#         answer.append(-1 if len(l) == 0 else min(l))
#     return answer