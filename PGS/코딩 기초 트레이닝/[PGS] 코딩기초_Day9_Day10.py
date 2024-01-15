### 41. 배열 만들기 5   (+1)
## 문제 설명
## 문자열 배열 intStrs와 정수 k, s, l가 주어집니다. intStrs의 원소는 숫자로 이루어져 있습니다.

## 배열 intStrs의 각 원소마다 s번 인덱스에서 시작하는 길이 l짜리 부분 문자열을 잘라내 정수로 변환합니다. 
## 이때 변환한 정수값이 k보다 큰 값들을 담은 배열을 return 하는 solution 함수를 완성해 주세요.

def solution(intStrs, k, s, l):
    return [ int(num[s:s+l]) for num in intStrs if int(num[s:s+l]) > k ]



### 42. 부분 문자열 이어 붙여 문자열 만들기   (+1)
## 문제 설명
## 길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다. 
## parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다. 
## 각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(my_strings, parts):
    answer = ''
    for idx in range(len(parts)):
        start = parts[idx][0]
        end = parts[idx][1]
        word = my_strings[idx]
        answer += word[start:end+1]
    return answer

# simple
def solution(my_strings, parts):
    return ''.join(my_strings[i][parts[i][0]:parts[i][1]+1] for i in range(len(my_strings)))



### 43. 문자열의 뒤의 n글자   (+1)
## 문제 설명
## 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 뒤의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, n):
    return my_string[len(my_string)-n:]
    # return my_string[-n:]



### 44. 접미사 배열    (+1)
## 문제 설명
## 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 
## 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
## 문자열 my_string이 매개변수로 주어질 때, my_string의 모든 접미사를 사전순으로 정렬한 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

def solution(my_string):
    word = ''
    answer = [my_string]
    for i in range(len(my_string)-1, 0, -1):
        word = my_string[i] + word
        answer.append(word)
    answer.sort()
    return answer

# simple
def solution(my_string):
    return sorted(my_string[i:] for i in range(len(my_string)))



### 45. 접미사인지 확인하기   (+1)
## 문제 설명
## 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 
## 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
## 문자열 my_string과 is_suffix가 주어질 때, is_suffix가 my_string의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string, is_suffix):
    suffix = [ my_string[i:] for i in range(len(my_string)) ]
    return 1 if is_suffix in suffix else 0

# using method
def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))

# simple
def solution(m, s):
    if m[-len(s):]==s: return 1
    return 0