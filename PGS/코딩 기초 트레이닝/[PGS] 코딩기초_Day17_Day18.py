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



### 86. x 사이의 개수     (+1)
## 문제 설명
## 문자열 myString이 주어집니다. myString을 문자 "x"를 기준으로 나눴을 때 
## 나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
def solution(myString):
    answer = myString.split('x')
    return [ len(letter) for letter in answer ]

# simple
def solution(myString):
    return [len(w) for w in myString.split('x')]



### 87. 문자열 잘라서 정렬하기    (+3)
## 문제 설명
## 문자열 myString이 주어집니다. 
## "x"를 기준으로 해당 문자열을 잘라내 배열을 만든 후 사전순으로 정렬한 배열을 return 하는 solution 함수를 완성해 주세요.
## 단, 빈 문자열은 반환할 배열에 넣지 않습니다.
def solution(myString):
    myString = myString.strip().split('x')
    myString.sort()
    return [ word for word in myString if word != '' ]

# simple
def solution(myString):
    return sorted(ch for ch in myString.split('x') if ch)



### 88. 간단한 식 계산하기    (+1)
## 문제 설명
## 문자열 binomial이 매개변수로 주어집니다. 
## binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다. 
## 주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.
def solution(binomial):
    return eval(binomial.strip())



### 89. 문자열 바꿔서 찾기      (+1)
## 문제 설명
## 문자 "A"와 "B"로 이루어진 문자열 myString과 pat가 주어집니다. myString의 "A"를 "B"로, 
## "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중 pat이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.
def solution(myString, pat):
    change = ''
    for letter in list(myString):
        if letter == 'A':
            change += 'B'
        elif letter == 'B':
            change += 'A'
    return 1 if pat in change else 0

# simple
def solution(myString, pat):
    return int(''.join(['A' if i == 'B' else 'B' for i in pat]) in myString)



### 90. rny_string    (+1)
## 문제 설명
## 'm'과 "rn"이 모양이 비슷하게 생긴 점을 활용해 문자열에 장난을 하려고 합니다. 
## 문자열 rny_string이 주어질 때, rny_string의 모든 'm'을 "rn"으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
def solution(rny_string):
    return ''.join(['rn' if letter == 'm' else letter for letter in rny_string ])

# replace
def solution(rny_string):
    return rny_string.replace('m', 'rn')