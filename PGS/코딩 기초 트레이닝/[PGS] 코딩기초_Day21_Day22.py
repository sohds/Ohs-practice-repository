### 101. 뒤에서 5등 위로     (+1)
## 문제 설명
## 정수로 이루어진 리스트 num_list가 주어집니다. 
## num_list에서 가장 작은 5개의 수를 제외한 수들을 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    return sorted(num_list)[5:]



### 102. 전국 대회 선발 고사    (+1)
## 문제 설명
## 0번부터 n - 1번까지 n명의 학생 중 3명을 선발하는 전국 대회 선발 고사를 보았습니다. 
## 등수가 높은 3명을 선발해야 하지만, 개인 사정으로 전국 대회에 참여하지 못하는 학생들이 있어 
## 참여가 가능한 학생 중 등수가 높은 3명을 선발하기로 했습니다.

## 각 학생들의 선발 고사 등수를 담은 정수 배열 rank와 전국 대회 참여 가능 여부가 담긴 boolean 배열 attendance가 매개변수로 주어집니다. 
## 전국 대회에 선발된 학생 번호들을 등수가 높은 순서대로 각각 a, b, c번이라고 할 때 
## 10000 × a + 100 × b + c를 return 하는 solution 함수를 작성해 주세요.
def solution(rank, attendance):
    real = []
    for i, (ranking, attend) in enumerate(zip(rank, attendance)):
        if (attend):    real.append([ranking, i])
    sorting = sorted(real)
    return sorting[0][1]*10000 + sorting[1][1]*100 + sorting[2][1]*1

# be simple
def solution(rank, attendance):
    arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
    return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]



### 103. 정수 부분     (+1)
## 문제 설명
## 실수 flo가 매개 변수로 주어질 때, flo의 정수 부분을 return하도록 solution 함수를 완성해주세요.
def solution(flo):
    return int(flo)

# other
def solution(flo):
    return flo//1



### 104. 문자열 정수의 합   (+1)
## 문제 설명
## 한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.
def solution(num_str):
    return sum(list(int(num_str[idx]) for idx in range(len(num_str))))



### 105. 문자열을 정수로 변환하기    (+1)
## 문제 설명
## 숫자로만 이루어진 문자열 n_str이 주어질 때, n_str을 정수로 변환하여 return하도록 solution 함수를 완성해주세요.
def solution(n_str):
    return int(n_str)



### 106. 0 떼기    (+1)
## 문제 설명
## 정수로 이루어진 문자열 n_str이 주어질 때, n_str의 가장 왼쪽에 처음으로 등장하는 0들을 뗀 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(n_str):
    for i in range(len(n_str)):
        if n_str[i] == '0':
            continue
        else:
            return n_str[i:]
        
# simple
def solution(n_str):
    return n_str.lstrip('0')

# 생각해보니 이런 방법도...
def solution(n_str):
    return str(int(n_str))



### 107. 두 수의 합     (+1)
## 문제 설명
## 0 이상의 두 정수가 문자열 a, b로 주어질 때, a + b의 값을 문자열로 return 하는 solution 함수를 작성해 주세요.
def solution(a, b):
    return str(int(a)+int(b))



### 108. 문자열로 변환      (+1)
## 문제 설명
## 정수 n이 주어질 때, n을 문자열로 변환하여 return하도록 solution 함수를 완성해주세요.
def solution(n):
    return str(n)



### 109. 배열의 원소 삭제하기     (+1)
## 문제 설명
## 정수 배열 arr과 delete_list가 있습니다. 
## arr의 원소 중 delete_list의 원소를 모두 삭제하고 
## 남은 원소들은 기존의 arr에 있던 순서를 유지한 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(arr, delete_list):
    for delete in delete_list:
        if delete in arr:  arr.remove(delete)
        else:   continue
    return arr



### 110. 부분 문자열인지 확인하기      (+1)
## 문제 설명
## 부분 문자열이란 문자열에서 연속된 일부분에 해당하는 문자열을 의미합니다. 
## 예를 들어, 문자열 "ana", "ban", "anana", "banana", "n"는 모두 문자열 "banana"의 부분 문자열이지만, 
## "aaa", "bnana", "wxyz"는 모두 "banana"의 부분 문자열이 아닙니다.

## 문자열 my_string과 target이 매개변수로 주어질 때, target이 문자열 my_string의 부분 문자열이라면 1을, 
## 아니라면 0을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, target):
    return 1 if target in my_string else 0

# in은 boolean으로 반환해서 int만 적용 시켜도 된다는걸 잊는다...
def solution(my_string, target):
    return int(target in my_string)