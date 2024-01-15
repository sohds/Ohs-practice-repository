### 31. 수열과 구간 쿼리 4   (+1)
## 문제 설명
## 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.

## 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 i가 k의 배수이면 arr[i]에 1을 더합니다.

## 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.

def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e+1):
            if i % k == 0:
                arr[i] += 1
    return arr



### 32. 배열 만들기 2   (+1)
## 문제 설명
## 정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 
## 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

## 만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.

def solution(l, r):
    answer = [ num for num in range(l, r+1) if not set(str(num)) - {'0', '5'}]
    # for num in range(l, r+1):
    #     if not set(str(num)) - {'0', '5'}:
    #         answer.append(num)
    return answer if len(answer) != 0 else [-1]



### 33. 카운트 업    (+1)
## 문제 설명
## 정수 start_num와 end_num가 주어질 때, start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

def solution(start_num, end_num):
    return [ n for n in range(start_num, end_num+1) ]



### 34. 콜라츠 수열 만들기   (+1)
## 문제 설명
## 모든 자연수 x에 대해서 현재 값이 x이면 x가 짝수일 때는 2로 나누고, 
# x가 홀수일 때는 3 * x + 1로 바꾸는 계산을 계속해서 반복하면 언젠가는 반드시 x가 1이 되는지 묻는 문제를 콜라츠 문제라고 부릅니다.
## 그리고 위 과정에서 거쳐간 모든 수를 기록한 수열을 콜라츠 수열이라고 부릅니다.

## 계산 결과 1,000 보다 작거나 같은 수에 대해서는 전부 언젠가 1에 도달한다는 것이 알려져 있습니다.
## 임의의 1,000 보다 작거나 같은 양의 정수 n이 주어질 때 초기값이 n인 콜라츠 수열을 return 하는 solution 함수를 완성해 주세요.

def solution(n):
    answer = []
    
    while n != 1:
        answer.append(int(n))
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1  
    answer.append(1)
    
    return answer



### 35. 배열 만들기 4   (+1)
## 문제 설명
## 정수 배열 arr가 주어집니다. arr를 이용해 새로운 배열 stk를 만드려고 합니다.

## 변수 i를 만들어 초기값을 0으로 설정한 후 i가 arr의 길이보다 작으면 다음 작업을 반복합니다.

## 만약 stk가 빈 배열이라면 arr[i]를 stk에 추가하고 i에 1을 더합니다.
## stk에 원소가 있고, stk의 마지막 원소가 arr[i]보다 작으면 arr[i]를 stk의 뒤에 추가하고 i에 1을 더합니다.
## stk에 원소가 있는데 stk의 마지막 원소가 arr[i]보다 크거나 같으면 stk의 마지막 원소를 stk에서 제거합니다.
## 위 작업을 마친 후 만들어진 stk를 return 하는 solution 함수를 완성해 주세요.

def solution(arr):
    stk = []
    i = 0
    while i != len(arr):
        
        # if len(stk) == 0:
        #     stk.append(arr[i])
        #     i += 1
        # elif len(stk) != 0 and stk[-1] < arr[i]:
        #     stk.append(arr[i])
        #     i += 1
        # elif len(stk) != 0 and stk[-1] >= arr[i]:
        #     del stk[-1]
        
        if len(stk) != 0 and stk[-1] >= arr[i]:
             del stk[-1]
        
        else:
            stk.append(arr[i])
            i += 1
            
    return stk

# other ver.
def solution(arr):
    stk = []
    for i in range(len(arr)):
        while stk and stk[-1] >= arr[i]:
            stk.pop()
        stk.append(arr[i])
    return stk



### 36. 간단한 논리 연산    (+1)
## 문제 설명
## boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때, 다음의 식의 true/false를 return 하는 solution 함수를 작성해 주세요.

## (x1 ∨ x2) ∧ (x3 ∨ x4)

def solution(x1, x2, x3, x4):
    # r1 = x1 or x2
    # r2 = x3 or x4
    # r3 = r1 and r2
    # return r3
    return (x1 or x2) and (x3 or x4)



### 37. 주사위 게임 3       (+1)
## 문제 설명
## 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

## 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
## 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
## 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
## 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
## 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
## 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.


# my ver.. 근데 너무 길고 시간복잡도가 그리 좋아보이지 않음
import collections

def solution(a, b, c, d):
    dice = [a, b, c, d]
    numbers = set(dice)
    
    if len(numbers) == 1:
        return a * 1000 + b * 100 + c * 10 + d
    
    elif len(numbers) == 4:
        return min(numbers)
    
    elif len(numbers) == 3:
        check = []
        for idx in range(4):
            if dice[idx] not in check:
                check.append(dice[idx])
            else:
                numbers.remove(dice[idx])
                nums = list(numbers)
                break
        return min(nums) * max(nums)
    
    else:
        counts = collections.Counter(dice)
        d_count = list(counts.values())
        d_num = list(counts.keys())
        if 2 in d_count:
            p = max(d_num)
            q = min(d_num)
            return (p+q) * abs(p-q)
        else:
            for idx in range(2):
                if d_count[idx] == 1:
                    q = d_num[idx]
                else:
                    p = d_num[idx]
            return (10 * p + q) ** 2
        
        

### 38. 글자 이어 붙여 문자열 만들기   (+1)
## 문제 설명
## 문자열 my_string과 정수 배열 index_list가 매개변수로 주어집니다. 
## my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(my_string, index_list):
    my_string = list(my_string)
    answer = ''
    for idx in index_list:
        answer += my_string[idx]
    return answer


# simple
def solution(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])



### 39. 9로 나눈 나머지    (+1)
## 문제 설명
## 음이 아닌 정수를 9로 나눈 나머지는 그 정수의 각 자리 숫자의 합을 9로 나눈 나머지와 같은 것이 알려져 있습니다.
## 이 사실을 이용하여 음이 아닌 정수가 문자열 number로 주어질 때, 이 정수를 9로 나눈 나머지를 return 하는 solution 함수를 작성해주세요.

def solution(number):
    return sum((map(int, number))) % 9
    # return int(number) % 9
    
    

### 40. 문자열 여러 번 뒤집기   (+1)
## 문제 설명
## 문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다. 
## queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다. 
## my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(my_string, queries):
    for query in queries:
        start = query[0]
        end = query[1]
        want = my_string[start:end+1]
        my_string = my_string[:start] + want[::-1] + my_string[end+1:]
    return my_string

# simple
def solution(my_string, queries):
    for (s, e) in queries:
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return my_string