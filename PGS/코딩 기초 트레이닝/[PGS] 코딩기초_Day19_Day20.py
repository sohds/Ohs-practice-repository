### 91. 세 개의 구분자     (+1)
## 문제 설명
## 임의의 문자열이 주어졌을 때 문자 "a", "b", "c"를 구분자로 사용해 문자열을 나누고자 합니다.

## 예를 들어 주어진 문자열이 "baconlettucetomato"라면 나눠진 문자열 목록은 ["onlettu", "etom", "to"] 가 됩니다.

## 문자열 myStr이 주어졌을 때 위 예시와 같이 "a", "b", "c"를 사용해 나눠진 문자열을 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

## 단, 두 구분자 사이에 다른 문자가 없을 경우에는 아무것도 저장하지 않으며, return할 배열이 빈 배열이라면 ["EMPTY"]를 return 합니다.

import re

def solution(myStr):
    answer = re.sub("[a-c]", " ", myStr).split()
    return answer if len(answer) > 0 else ["EMPTY"]

# re split ver
import re
def solution(myStr):
    answer = [m for m in re.split('a|b|c',myStr) if m]
    if len(answer)==0:
        answer=["EMPTY"]

    return answer

# no import libraries
def solution(myStr):
    answer = [x for x in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if x]
    return answer if answer else ['EMPTY']



### 92. 배열의 원소만큼 추가하기      (+1)
## 문제 설명
## 아무 원소도 들어있지 않은 빈 배열 X가 있습니다. 양의 정수 배열 arr가 매개변수로 주어질 때, 
## arr의 앞에서부터 차례대로 원소를 보면서 원소가 a라면 X의 맨 뒤에 a를 a번 추가하는 일을 반복한 뒤의 
## 배열 X를 return 하는 solution 함수를 작성해 주세요.
def solution(arr):
    answer = []
    for num in arr:
        for i in range(num):
            answer.append(num)
    return answer

# list comprehension
def solution(arr):
    return [i for i in arr for j in range(i)]



### 93. 빈 배열에 추가, 삭제하기     (+1)
## 문제 설명
## 아무 원소도 들어있지 않은 빈 배열 X가 있습니다. 
## 길이가 같은 정수 배열 arr과 boolean 배열 flag가 매개변수로 주어질 때, 
## flag를 차례대로 순회하며 flag[i]가 true라면 X의 뒤에 arr[i]를 arr[i] × 2 번 추가하고, 
## flag[i]가 false라면 X에서 마지막 arr[i]개의 원소를 제거한 뒤 X를 return 하는 solution 함수를 작성해 주세요.
def solution(arr, flag):
    X = []
    
    for i in range(len(arr)):
        if (flag[i]):
            for num in range(arr[i]*2):
                X.append(arr[i])
        else:  X = X[:-(arr[i])]
        
    return X


# other ver
def solution(arr, flag):
    arr1 = []
    for i, j in zip(arr, flag):
        if j:
            arr1 += [i] * i * 2
        else:
            arr1 = arr1[:-i]
    return arr1



### 94. 배열 만들기 6     (+1)
## 문제 설명
## 0과 1로만 이루어진 정수 배열 arr가 주어집니다. arr를 이용해 새로운 배열 stk을 만드려고 합니다.

## i의 초기값을 0으로 설정하고 i가 arr의 길이보다 작으면 다음을 반복합니다.

## 만약 stk이 빈 배열이라면 arr[i]를 stk에 추가하고 i에 1을 더합니다.
## stk에 원소가 있고, stk의 마지막 원소가 arr[i]와 같으면 stk의 마지막 원소를 stk에서 제거하고 i에 1을 더합니다.
## stk에 원소가 있는데 stk의 마지막 원소가 arr[i]와 다르면 stk의 맨 마지막에 arr[i]를 추가하고 i에 1을 더합니다.
## 위 작업을 마친 후 만들어진 stk을 return 하는 solution 함수를 완성해 주세요.

## 단, 만약 빈 배열을 return 해야한다면 [-1]을 return 합니다.
def solution(arr):
    stk = []
    
    for i in range(len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
        else:
            if stk[-1] == arr[i]:
                del stk[-1]
            else:
                stk.append(arr[i])
                
    return [-1] if len(stk) == 0 else stk



### 95. 무작위로 K개의 수 뽑기     (+2)
## 문제 설명
## 랜덤으로 서로 다른 k개의 수를 저장한 배열을 만드려고 합니다. 적절한 방법이 떠오르지 않기 때문에 일정한 범위 내에서 무작위로 수를 뽑은 후, 
## 지금까지 나온적이 없는 수이면 배열 맨 뒤에 추가하는 방식으로 만들기로 합니다.

## 이미 어떤 수가 무작위로 주어질지 알고 있다고 가정하고, 실제 만들어질 길이 k의 배열을 예상해봅시다.

## 정수 배열 arr가 주어집니다. 문제에서의 무작위의 수는 arr에 저장된 순서대로 주어질 예정이라고 했을 때, 
## 완성될 배열을 return 하는 solution 함수를 완성해 주세요.

## 단, 완성될 배열의 길이가 k보다 작으면 나머지 값을 전부 -1로 채워서 return 합니다.
def solution(arr, k):
    ret = []
    for i in arr:
        if i not in ret:
            ret.append(i)
        if len(ret) == k:
            break

    return ret + [-1] * (k - len(ret))



### 96. 배열의 길이를 2의 거듭제곱으로 만들기     (+3)
## 문제 설명
## 정수 배열 arr이 매개변수로 주어집니다. arr의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 정수 0을 추가하려고 합니다. 
## arr에 최소한의 개수로 0을 추가한 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(arr):
    length = [ 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 ]
    diff = list(map(lambda x: x-len(arr), length))
    
    for i in range(len(diff)):
        if diff[i] >= 0:
            diff_arr = diff[i]
            return arr + [0] * diff_arr
        
        

### 97. 배열 비교하기       (+1)
## 문제 설명
## 이 문제에서 두 정수 배열의 대소관계를 다음과 같이 정의합니다.

## 두 배열의 길이가 다르다면, 배열의 길이가 긴 쪽이 더 큽니다.
## 배열의 길이가 같다면 각 배열에 있는 모든 원소의 합을 비교하여 다르다면 더 큰 쪽이 크고, 같다면 같습니다.
## 두 정수 배열 arr1과 arr2가 주어질 때, 위에서 정의한 배열의 대소관계에 대하여 arr2가 크다면 -1, 
## arr1이 크다면 1, 두 배열이 같다면 0을 return 하는 solution 함수를 작성해 주세요.
def solution(arr1, arr2):
    if len(arr1) != len(arr2):
        if len(arr1) > len(arr2):
            return 1
        else:
            return -1
    else:
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) == sum(arr2):
            return 0
        else:
            return -1
        


### 98. 문자열 묶기     (+2)
## 문제 설명
## 문자열 배열 strArr이 주어집니다. 
## strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.
def solution(strArr):
    answer = [len(i) for i in strArr]
    tmp = []
    for i in set(answer):
        tmp.append(answer.count(i))
    
    return max(tmp)



### 99. 배열의 길이에 따라 다른 연산하기      (+1)
## 문제 설명
## 정수 배열 arr과 정수 n이 매개변수로 주어집니다. arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을, 
## arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(arr, n):
    if len(arr) % 2 == 0:
        return [ arr[idx]+n if idx % 2 == 1 else arr[idx] for idx in range(len(arr)) ]
    else:
        return [ arr[idx]+n if idx % 2 == 0 else arr[idx] for idx in range(len(arr)) ]
    
    

### 100. 뒤에서 5등까지       (+1)
# 문제 설명
# 정수로 이루어진 리스트 num_list가 주어집니다. 
# num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(num_list):    
    return sorted(num_list)[:5]