### 71. 조건에 맞게 수열 변환하기 1     (+1)
## 문제 설명
## 정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱합니다. 
## 그 결과인 정수 배열을 return 하는 solution 함수를 완성해 주세요.
def solution(arr):
    for idx in range(len(arr)):
        if arr[idx] % 2 == 0:
            if arr[idx] >= 50:
                arr[idx] /= 2
        else:
             if arr[idx] < 50:
                arr[idx] *= 2
    return arr



### 72. 조건에 맞게 수열 변환하기 2     (+1)
## 문제 설명
## 정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱하고 다시 1을 더합니다.

## 이러한 작업을 x번 반복한 결과인 배열을 arr(x)라고 표현했을 때, 
## arr(x) = arr(x + 1)인 x가 항상 존재합니다. 이러한 x 중 가장 작은 값을 return 하는 solution 함수를 완성해 주세요.

## 단, 두 배열에 대한 "="는 두 배열의 크기가 서로 같으며, 같은 인덱스의 원소가 각각 서로 같음을 의미합니다.
def solution(arr):
    idx = 0
    prev = arr
    
    while True:
        change = []
        for i in prev:
            if i >= 50 and i % 2 == 0: change.append(int(i / 2))
            elif i < 50 and i % 2 == 1: change.append(i * 2 + 1)
            else: change.append(i)

        same = all(a == b for a, b in zip(prev, change))
        if same:
            break
        idx += 1

        prev = change
        


### 73. 1로 만들기       (+1)
## 문제 설명
## 정수가 있을 때, 짝수라면 반으로 나누고, 홀수라면 1을 뺀 뒤 반으로 나누면, 마지막엔 1이 됩니다. 
## 예를 들어 10이 있다면 다음과 같은 과정으로 1이 됩니다.

## 10 / 2 = 5
## (5 - 1) / 2 = 4
## 4 / 2 = 2
## 2 / 2 = 1
## 위와 같이 4번의 나누기 연산으로 1이 되었습니다.

## 정수들이 담긴 리스트 num_list가 주어질 때, 
## num_list의 모든 원소를 1로 만들기 위해서 필요한 나누기 연산의 횟수를 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    count = 0
    for idx in range(len(num_list)):
        while num_list[idx] != 1:
            count += 1
            if num_list[idx] % 2 == 0:
                num_list[idx] /= 2
            else:
                num_list[idx] = (num_list[idx]-1) / 2
    return count

# 이진수 풀이법  (다른 사람 풀이)
def solution(num_list):
    return sum(len(bin(i)) - 3 for i in num_list)
# 예를 들어 i=12 일때, bin(i) 를 하면 '0b1100' 이 됩니다. 
# 여기서 우리는 마지막으로 남겨야 하는 1; 
# 즉 2^0인 맨끝의 '0'과 과 이진수를 나타내는 앞의 '0b' 총 길이 3을 제외한 나머지 숫자들인 "110" 을 없애는 것이 목표값이 되는데, 
# 이는 각 자리마다 2를 나누는 횟수기 때문에 "110"의 길이인 3이 됩니다. 홀 수 일 때는 어차피 -1을 해서 짝수로 만들기 때문에 가능합니다.

# len(bin(i)) - 3을 통해 '0b'의 길이 2와 마지막 비트(1)의 길이 1을 뺍니다. 이는 정수 i를 1로 만드는데 필요한 연산 횟수와 일치합니다. 
# 예를 들어, 10은 이진수로 1010이고, 3번의 연산이 필요합니다 (첫 번째 '1'은 무시됩니다).



### 74. 길이에 따른 연산   (+1)
## 문제 설명
## 정수가 담긴 리스트 num_list가 주어질 때, 리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을 10 이하이면 
## 모든 원소의 곱을 return하도록 solution 함수를 완성해주세요.
from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else prod(num_list)

# not import any libraries
def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    else:
        return eval('*'.join(list(map(str, num_list))))
    


### 75. 원하는 문자열 찾기    (+1)
## 문제 설명
## 알파벳으로 이루어진 문자열 myString과 pat이 주어집니다. 
## myString의 연속된 부분 문자열 중 pat이 존재하면 1을 그렇지 않으면 0을 return 하는 solution 함수를 완성해 주세요.

## 단, 알파벳 대문자와 소문자는 구분하지 않습니다.
def solution(myString, pat):
    myString, pat = myString.lower(), pat.lower()
    return 1 if pat in myString else 0

# boolean 어차피 0과 1이니까.. int로 바꿔주기만 해도 ㅇㅋ
def solution(myString, pat):
    return int(pat.lower() in myString.lower())