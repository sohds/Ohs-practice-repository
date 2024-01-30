### 111. 부분 문자열       (+1)
## 문제 설명
## 어떤 문자열 A가 다른 문자열 B안에 속하면 A를 B의 부분 문자열이라고 합니다. 예를 들어 문자열 "abc"는 문자열 "aabcc"의 부분 문자열입니다.

## 문자열 str1과 str2가 주어질 때, str1이 str2의 부분 문자열이라면 1을 부분 문자열이 아니라면 0을 return하도록 solution 함수를 완성해주세요.
def solution(str1, str2):
    return int(str1 in str2)



### 112. 꼬리 문자열        (+1)
## 문제 설명
## 문자열들이 담긴 리스트가 주어졌을 때, 모든 문자열들을 순서대로 합친 문자열을 꼬리 문자열이라고 합니다. 
## 꼬리 문자열을 만들 때 특정 문자열을 포함한 문자열은 제외시키려고 합니다. 
## 예를 들어 문자열 리스트 ["abc", "def", "ghi"]가 있고 문자열 "ef"를 포함한 문자열은 제외하고 꼬리 문자열을 만들면 "abcghi"가 됩니다.

## 문자열 리스트 str_list와 제외하려는 문자열 ex가 주어질 때, 
## str_list에서 ex를 포함한 문자열을 제외하고 만든 꼬리 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(str_list, ex):
    answer = ''
    for string in str_list:
        if ex in string:
            continue
        else:
            answer += string
    return answer

# list comprehension + join
def solution(str_list, ex):
    return ''.join([i for i in str_list if ex not in i])

# lambda filter + join
def solution(str_list, ex):
    return ''.join(filter(lambda x: ex not in x, str_list))



### 113. 정수 찾기     (+1)
## 문제 설명
## 정수 리스트 num_list와 찾으려는 정수 n이 주어질 때, num_list안에 n이 있으면 1을 없으면 0을 return하도록 solution 함수를 완성해주세요.
def solution(num_list, n):
    return int(n in num_list)



### 114. 주사위 게임 1     (+1)
## 문제 설명
## 1부터 6까지 숫자가 적힌 주사위가 두 개 있습니다. 두 주사위를 굴렸을 때 나온 숫자를 각각 a, b라고 했을 때 얻는 점수는 다음과 같습니다.

## a와 b가 모두 홀수라면 a2 + b2 점을 얻습니다.
## a와 b 중 하나만 홀수라면 2 × (a + b) 점을 얻습니다.
## a와 b 모두 홀수가 아니라면 |a - b| 점을 얻습니다.
## 두 정수 a와 b가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
def solution(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return abs(a-b)
    elif a % 2 == 1 and b % 2 == 1:
        return a**2 + b**2
    else:
        return 2 * (a+b)
    
    

### 115. 날짜 비교하기      (+3)
## 문제 설명
## 정수 배열 date1과 date2가 주어집니다. 두 배열은 각각 날짜를 나타내며 [year, month, day] 꼴로 주어집니다. 
## 각 배열에서 year는 연도를, month는 월을, day는 날짜를 나타냅니다.

## 만약 date1이 date2보다 앞서는 날짜라면 1을, 아니면 0을 return 하는 solution 함수를 완성해 주세요.
def solution(date1, date2):
    year, month, day = 0, 1, 2
    
    if date1[year] != date2[year]:
        return 1 if date1[year] < date2[year] else 0
    
    elif date1[month] != date2[month]:
        return 1 if date1[month] < date2[month] else 0
    
    elif date1[day] != date2[day]:
        return 1 if date1[day] < date2[day] else 0
    
    else:
        return 0
    
# simple
def solution(date1, date2):
    return int(date1 < date2)



### 116. 커피 심부름      (+1)
## 문제 설명
## 팀의 막내인 철수는 아메리카노와 카페 라테만 판매하는 카페에서 팀원들의 커피를 사려고 합니다. 
## 아메리카노와 카페 라테의 가격은 차가운 것과 뜨거운 것 상관없이 각각 4500, 5000원입니다. 
## 각 팀원에게 마실 메뉴를 적어달라고 하였고, 그 중에서 메뉴만 적은 팀원의 것은 차가운 것으로 통일하고 
## "아무거나"를 적은 팀원의 것은 차가운 아메리카노로 통일하기로 하였습니다.

## 각 직원이 적은 메뉴가 문자열 배열 order로 주어질 때, 카페에서 결제하게 될 금액을 return 하는 solution 함수를 작성해주세요. 
## order의 원소는 아래의 것들만 들어오고, 각각의 의미는 다음과 같습니다.

## | order의 원소  |  의미  |
## | "iceamericano", "americanoice" |  차가운 아메리카노  |
## | "hotamericano", "americanohot" |  따뜻한 아메리카노  |
## | "icecafelatte", "cafelatteice" |  차가운 카페 라테  |
## | "hotcafelatte", "cafelattehot" |  따뜻한 카페 라테  |
## | "americano" |  아메리카노  |
## | "cafelatte" |  카페 라테  |
## | "anything" |  아무거나  |

def solution(order):
    cash = 0
    for each in order:
        if 'cafelatte' in each:
            cash += 5000
        else:
            cash += 4500
    return cash



### 117. 그림 확대    (+1)
## 문제 설명
## 직사각형 형태의 그림 파일이 있고, 이 그림 파일은 1 × 1 크기의 정사각형 크기의 픽셀로 이루어져 있습니다. 
## 이 그림 파일을 나타낸 문자열 배열 picture과 정수 k가 매개변수로 주어질 때, 
## 이 그림 파일을 가로 세로로 k배 늘린 그림 파일을 나타내도록 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(picture, k):
    answer = []
    for pixel in picture:
        temp = ''
        for element in pixel:
            temp += element*k
        for time in range(k):
            answer.append(temp)
    return answer

# replace
def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        for _ in range(k):
            answer.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))
    return answer



### 118. 조건에 맞게 수열 변환하기 3    (+1)
## 문제 설명
## 정수 배열 arr와 자연수 k가 주어집니다.

## 만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고, k가 짝수라면 arr의 모든 원소에 k를 더합니다.

## 이러한 변환을 마친 후의 arr를 return 하는 solution 함수를 완성해 주세요.
def solution(arr, k):
    return [ num+k if k%2==0 else num*k for num in arr ]



### 119. l로 만들기      (+1)
## 문제 설명
## 알파벳 소문자로 이루어진 문자열 myString이 주어집니다. 
## 알파벳 순서에서 "l"보다 앞서는 모든 문자를 "l"로 바꾼 문자열을 return 하는 solution 함수를 완성해 주세요.
def solution(myString):
    return ''.join(['l' if ord(letter) < ord('l') else letter for letter in myString])  # 아스키코드 사용해서 뿌듯.. ㅎㅎ

# other
def solution(myString):
    return myString.translate(str.maketrans('abcdefghijk', 'lllllllllll'))

# maketrans 예시
velog = "sunbun 개발로그 sohds.log"
ch = velog.maketrans("l", "L")
print(velog.translate(ch))
# >>> 결과값: sunbun 개발로그 sohds.Log

# 문자열 일부를 지정 문자로 대체 정의하는 매핑 테이블 생성.
# ※ 매핑 테이블 이용해 문자열 대체하는 translate() 메서드와 사용.

# 자세한 내용은 https://homzzang.com/b/py-187 참고



### 120. 특별한 이차원 배열 1    (+1)
## 문제 설명
## 정수 n이 매개변수로 주어질 때, 다음과 같은 n × n 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성해 주세요.

## arr[i][j] (0 ≤ i, j < n)의 값은 i = j라면 1, 아니라면 0입니다.
def solution(n):
    answer = [[0]*n for i in range(n)]
    for i in range(n):
        answer[i][i] = 1
    return answer