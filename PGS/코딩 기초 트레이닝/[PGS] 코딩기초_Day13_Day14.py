### 61. n 번째 원소부터    (+1)
## 문제 설명
## 정수 리스트 num_list와 정수 n이 주어질 때, n 번째 원소부터 마지막 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(num_list, n):
    return num_list[n-1:]



### 62. 순서 바꾸기    (+1)
## 문제 설명
## 정수 리스트 num_list와 정수 n이 주어질 때, 
## num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로 나눠
## n 번째 원소 이후의 원소들을 n 번째까지의 원소들 앞에 붙인 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(num_list, n):
    fore_list = num_list[n:]
    back_list = num_list[:n]
    return fore_list + back_list



### 63. 왼쪽 오른쪽    (+4)
## 문제 설명
## 문자열 리스트 str_list에는 "u", "d", "l", "r" 네 개의 문자열이 여러 개 저장되어 있습니다. 
## str_list에서 "l"과 "r" 중 먼저 나오는 문자열이 "l"이라면 해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를, 
## 먼저 나오는 문자열이 "r"이라면 해당 문자열을 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트를 return하도록 solution 함수를 완성해주세요. 
## "l"이나 "r"이 없다면 빈 리스트를 return합니다.
def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i]=='l': return str_list[:i]
        elif str_list[i]=='r': return str_list[i+1:]
    return []



### 64. n 번째 원소까지    (+1)
## 문제 설명
## 정수 리스트 num_list와 정수 n이 주어질 때,
## num_list의 첫 번째 원소부터 n 번째 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(num_list, n):
    return num_list[:n]



### 65. n개 간격의 원소들    (+1)
## 문제 설명
## 정수 리스트 num_list와 정수 n이 주어질 때, 
## num_list의 첫 번째 원소부터 마지막 원소까지 n개 간격으로 저장되어있는 원소들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(num_list, n):
    return num_list[::n]



### 66. 홀수 vs 짝수          (+1)
## 문제 설명
## 정수 리스트 num_list가 주어집니다. 
## 가장 첫 번째 원소를 1번 원소라고 할 때, 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요. 
## 두 값이 같을 경우 그 값을 return합니다.
def solution(num_list):
    even, odd = 0, 0
    
    for idx in range(len(num_list)):
        if idx % 2 == 0:
            even += num_list[idx]
        else:
            odd += num_list[idx]
            
    answer = [even, odd]
    return max(answer)

# simple
def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))



### 67. 5명씩      (+1)
## 문제 설명
## 최대 5명씩 탑승가능한 놀이기구를 타기 위해 줄을 서있는 사람들의 이름이 담긴 문자열 리스트 names가 주어질 때, 
## 앞에서 부터 5명씩 묶은 그룹의 가장 앞에 서있는 사람들의 이름을 담은 리스트를 return하도록 solution 함수를 완성해주세요. 
## 마지막 그룹이 5명이 되지 않더라도 가장 앞에 있는 사람의 이름을 포함합니다.
def solution(names):
    return names[::5]



### 68. 할 일 목록      (+1)
## 문제 설명
## 오늘 해야 할 일이 담긴 문자열 배열 todo_list와 각각의 일을 지금 마쳤는지를 나타내는 boolean 배열 finished가 매개변수로 주어질 때, 
## todo_list에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(todo_list, finished):
    return [ todo_list[i] for i in range(len(finished)) if finished[i] == False ]



### 69. n보다 커질 때까지 더하기     (+1)
## 문제 설명
## 정수 배열 numbers와 정수 n이 매개변수로 주어집니다. 
## numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return 하는 solution 함수를 작성해 주세요.
def solution(numbers, n):
    for i in range(len(numbers)+1):
        if sum(numbers[:i]) > n:
            return sum(numbers[:i])
        else:
            continue
        


### 70. 수열과 구간 쿼리 1    (+1)
## 문제 설명
## 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e] 꼴입니다.

## 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 arr[i]에 1을 더합니다.

## 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.
def solution(arr, queries):
    for idx in range(len(queries)):
        start, end = queries[idx][0], queries[idx][1]+1
        for i in range(start, end):
            arr[i] += 1
    return arr


# for문을 튜플 형태로 받는 것도 연습해야할듯..
def solution(arr, queries):
    for (s, e) in queries:
        arr = [a+1 if s <= i <= e else a for i, a in enumerate(arr)]
    return arr