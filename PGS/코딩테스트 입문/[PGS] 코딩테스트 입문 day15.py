### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 15 문자열, 해시, 배열, 수학
# 영어가 싫어요 (+3)
# 문제 설명 : 영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 
# 문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.
def solution(numbers):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for index, num in enumerate(nums):
        # enumerate() 함수는 기본적으로 인덱스와 원소로 이루어진 튜플(tuple) 을 만들어줌
        # start = 1 <- parameter 지정 시 인덱스가 1부터 시작하게 됨
        numbers = numbers.replace(num, str(index))
    return int(numbers)


# 인덱스 바꾸기 (+1)
# 문제 설명 : 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, 
# my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
def solution(my_string, num1, num2):
    my_string = list(my_string)
    my_string[num1], my_string[num2]  = my_string[num2], my_string[num1]
    return ''.join(my_string)


# 한 번만 등장한 문자 (+)
# 문제 설명 : 문자열 s가 매개변수로 주어집니다. 
# s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 
# 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.

# wrong ver.
# reason thinking : 두번째 for문부터가 잘못된듯..
def solution(s):
    s = list(s)
    dic_count = {}
    for i in s:
        if i not in dic_count:
            dic_count[i] = 1
        else:
            dic_count[i] += 1
        ls_dic = list(dic_count.values())
    for k in range(0, len(ls_dic)):
        if ls_dic[k] > 1:
            while s[k] in s:
                s.remove(s[k])
    s.sorted()
    return s

# short ver.
def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer

# second commit 필요.. 코드에 대한 이해를 더 하자

# 약수 구하기
# 문제 설명 : 정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
def solution(n):
    return [ i for i in range(1, n+1) if n % i == 0]