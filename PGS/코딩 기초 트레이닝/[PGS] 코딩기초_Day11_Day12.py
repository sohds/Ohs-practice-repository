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