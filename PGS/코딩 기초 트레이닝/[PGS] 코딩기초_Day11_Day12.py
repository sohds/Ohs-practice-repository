### 51. 문자 개수 세기    (+1)
## 문제 설명
## 알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때,
## my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수, 
## my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를 
## 순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string):
    answer = [0] * 52
    chars = { "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25, "a": 26, "b": 27, "c": 28, "d": 29, "e": 30, "f": 31, "g": 32, "h": 33, "i": 34, "j": 35, "k": 36, "l": 37, "m": 38, "n": 39, "o": 40, "p": 41, "q": 42, "r": 43, "s": 44, "t": 45, "u": 46, "v": 47, "w": 48, "x": 49, "y": 50, "z": 51 }
    
    for i in my_string:
        cnt = my_string.count(i)
        answer[chars[i]] = cnt
    
    return answer

# 아스키코드
def solution(my_string):
    answer=[0]*52
    for x in my_string:
        if x.isupper():
            answer[ord(x)-65]+=1
        else:
            answer[ord(x)-71]+=1
    return answer

# SHORT
def solution(my_string):
    return [my_string.count(alphabet) for alphabet in 'abcdefghijklmnopqrstuvwxyz'.upper()+'abcdefghijklmnopqrstuvwxyz']



### 52. 배열 만들기 1    (+1)
## 문제 설명
## 정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
def solution(n, k):
    return [ num for num in range(1, n+1) if num % k == 0 ]

# 1부터 안해도 됨..
def solution(n, k):
    return [i for i in range(k,n+1,k)]



### 53. 글자 지우기     (+1)
## 문제 설명
## 문자열 my_string과 정수 배열 indices가 주어질 때,
## my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, indices):
    string = list(my_string)
    indices.sort()
    for idx in range(len(indices)):
        del string[indices[idx]-idx]
    return ''.join(string)

# simple
def solution(my_string, indices):
    return "".join([v for i,v in enumerate(my_string) if i not in indices])



### 54. 카운트 다운   (+1)
## 문제 설명
## 정수 start_num와 end_num가 주어질 때, start_num에서 end_num까지 
## 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(start, end_num):
    return [ num for num in range(start, end_num-1, -1) ]

# for문을 안 쓸 수도 있구나..
def solution(start, end):
    return list(range(start,end-1,-1))



### 55. 가까운 1 찾기    (+1)
## 문제 설명
## 정수 배열 arr가 주어집니다. 이때 arr의 원소는 1 또는 0입니다. 
## 정수 idx가 주어졌을 때, idx보다 크면서 배열의 값이 1인 가장 작은 인덱스를 찾아서 반환하는 solution 함수를 완성해 주세요.

## 단, 만약 그러한 인덱스가 없다면 -1을 반환합니다.

def solution(arr, idx):
    for idx in range(idx, len(arr)):
        if arr[idx] == 1:
            return idx
        else:
            continue
    return -1


# try-except 문
def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1

    return answer



### 56. 리스트 자르기    (+2)
## 문제 설명
## 정수 n과 정수 3개가 담긴 리스트 slicer 그리고 정수 여러 개가 담긴 리스트 num_list가 주어집니다. 
## slicer에 담긴 정수를 차례대로 a, b, c라고 할 때, n에 따라 다음과 같이 num_list를 슬라이싱 하려고 합니다.

## n = 1 : num_list의 0번 인덱스부터 b번 인덱스까지
## n = 2 : num_list의 a번 인덱스부터 마지막 인덱스까지
## n = 3 : num_list의 a번 인덱스부터 b번 인덱스까지
## n = 4 : num_list의 a번 인덱스부터 b번 인덱스까지 c 간격으로
## 올바르게 슬라이싱한 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(n, slicer, num_list):
    if n == 1:
        return num_list[:slicer[1]+1]
    
    elif n == 2:
        return num_list[slicer[0]:]
    
    elif n == 3:
        return num_list[slicer[0]:slicer[1]+1]
    
    elif n == 4:
        return num_list[slicer[0]:slicer[1]+1:slicer[2]]
    
    

### 57. 첫 번째로 나오는 음수    (+1)
## 문제 설명
## 정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 음수가 없다면 -1을 return합니다.
def solution(num_list):
    for idx in range(len(num_list)):
        if num_list[idx] < 0:
            return idx
        
        else:
            continue
        
    return -1



### 58. 배열 만들기 3    (+1)
## 문제 설명
## 정수 배열 arr와 2개의 구간이 담긴 배열 intervals가 주어집니다.

## intervals는 항상 [[a1, b1], [a2, b2]]의 꼴로 주어지며 각 구간은 닫힌 구간입니다. 
## 닫힌 구간은 양 끝값과 그 사이의 값을 모두 포함하는 구간을 의미합니다.

## 이때 배열 arr의 첫 번째 구간에 해당하는 배열과 두 번째 구간에 해당하는 배열을 앞뒤로 붙여 
## 새로운 배열을 만들어 return 하는 solution 함수를 완성해 주세요.
def solution(arr, intervals):
    answer = []
    start, end = 0, 0
    
    for idx in range(len(intervals)):
        start, end = intervals[idx][0], intervals[idx][1]
        temp_arr = arr[start:end+1]
        
        for num in temp_arr:
            answer.append(num)
            
    return answer

# simple
def solution(arr, intervals):
    s1, e1 = intervals[0]
    s2, e2 = intervals[1]
    return arr[s1:e1+1] + arr[s2:e2+1]



### 59. 2의 영역    (+1)
## 문제 설명
## 정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.

## 단, arr에 2가 없는 경우 [-1]을 return 합니다.
def solution(arr):
    if arr.count(2) == 1:
        return [2]
    
    elif arr.count(2) == 0:
        return [-1]
    
    else:
        all_index = list(filter(lambda x: arr[x] == 2, range(len(arr))))
        
        if len(all_index) == 2:
            return arr[all_index[0]:all_index[1]+1]
        
        else:
            return arr[all_index[0]:all_index[-1]+1]
        
# simple
def solution(arr):
    return [-1] if 2 not in arr else arr[arr.index(2) : len(arr) - arr[::-1].index(2)]



### 60. 배열 조각하기    (+3)
## 문제 설명
## 정수 배열 arr와 query가 주어집니다.

## query를 순회하면서 다음 작업을 반복합니다.

## 짝수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고 배열의 query[i]번 인덱스 뒷부분을 잘라서 버립니다.
## 홀수 인덱스에서는 arr에서 query[i]번 인덱스는 제외하고 배열의 query[i]번 인덱스 앞부분을 잘라서 버립니다.
## 위 작업을 마친 후 남은 arr의 부분 배열을 return 하는 solution 함수를 완성해 주세요.
def solution(arr, query):
    for th in range(len(query)):
        idx = query[th]
        if th % 2 == 0:
            arr = arr[:idx+1]
        else:
            arr = arr[idx:]
    return arr