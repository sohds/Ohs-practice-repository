### 81. 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기    (+1)
## 문제 설명
## 문자열 myString과 pat가 주어집니다. 
## myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.
def solution(myString, pat):
    try:
        index = myString.rindex(pat)
        l = len(pat)
        return myString[:index+l]
    except:
        print("Not found")



### 82. 문자열이 몇 번 등장하는지 세기    (+2)
## 문제 설명
## 문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.
def solution(myString, pat):
    count = 0
    
    for idx in range(len(myString)):
        if idx+len(pat) <= len(myString):
            if myString[idx:idx+len(pat)] == pat:
                count += 1
        else: break
            
    return count

# startswith 함수 사용
def solution(myString, pat):
    answer = 0
    for i, x in enumerate(myString) :
        if myString[i:].startswith(pat) :
            answer += 1
    return answer

# simple
def solution(myString, pat):
    return sum(myString[i:i + len(pat)] == pat for i in range(len(myString)))



### 83. ad 제거하기    (+1)
## 문제 설명
## 문자열 배열 strArr가 주어집니다. 배열 내의 문자열 중 "ad"라는 부분 문자열을 포함하고 있는 모든 문자열을 제거하고 
## 남은 문자열을 순서를 유지하여 배열로 return 하는 solution 함수를 완성해 주세요.
def solution(strArr):
    return [ word for word in strArr if 'ad' not in word ]



### 84. 공백으로 구분하기 1     (+1)
## 문제 설명
## 단어가 공백 한 개로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때, 
## my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string):
    return my_string.split(' ')



### 85. 공백으로 구분하기 2     (+1)
## 문제 설명
## 단어가 공백 한 개 이상으로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때, 
## my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(my_string):
    return my_string.split()