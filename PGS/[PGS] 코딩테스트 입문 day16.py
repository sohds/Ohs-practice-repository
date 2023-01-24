### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 16 문자열, 수학, 배열, 조건문
# 편지 (+1)
# 문제 설명 : 머쓱이는 할머니께 생신 축하 편지를 쓰려고 합니다. 
# 할머니가 보시기 편하도록 글자 한 자 한 자를 가로 2cm 크기로 적으려고 하며, 
# 편지를 가로로만 적을 때, 축하 문구 message를 적기 위해 필요한 편지지의 최소 가로길이를 return 하도록 solution 함수를 완성해주세요.
def solution(message):
    return len(message) * 2


# 가장 큰 수 찾기 (+1)
# 문제 설명 : 정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(array):
    return [max(array), array.index(max(array))]


# 문자열 계산하기 (+8)
# 문제 설명 : my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 my_string이 매개변수로 주어질 때, 
# 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.

# 제시된 입출력 예시 '3 + 4 = 7'는 되는데, 나머지 테스트 케이스가 안되는듯..
# 왜지? 하여튼 wrong ver.
def solution(my_string):
    my_string = list(my_string)
    nums = []
    plus = 0
    for i in my_string:
        if i.isnumeric() == True:
            nums.append(int(i))
        elif i == '+':
            plus = 1
    if plus == 1:
        return nums[0] + nums[1]
    else:
        return nums[0] - nums[1]

# short ver.
def solution(my_string):
    return eval(my_string)
    # 자체 내장 함수 eval() 사용
    # 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환


# 배열의 유사도 (+1)
# 문제 설명 : 두 배열이 얼마나 유사한지 확인해보려고 합니다. 
# 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

# my answer.
def solution(s1, s2):
    answer = [ i for i in s1 if i in s2 ]
    return len(answer)



# another ver.
def solution(s1, s2):
    return len(set(s1)&set(s2))

# set 자료구조에 대해 잘 모른다.
# set에 대한 자세한 이해 필요!

# 중복을 허용하지 않는 set() 자료구조!
# e.g.) >>> a = set([0,0,0,1,2,3]) >>> a {0, 1, 2, 3}
# dict와 동일하지만 추가되는 아이템이 key 값을 갖고 있지 않음.

# 따라서 집합 연산이 가능!
# 합집합 a와 b를 set으로 각각 묶어주고 a & b를 하면 공통 요소 출력, a | b를 하면 합집합 출력, a - b를 하면 차집합 출력
# 합집합을 | 말고도 .union() 을 사용해도 됨!

# .add() (집합도 요소를 추가) / .update() (집합 전체를 업데이트 하는 기능, update 안엔 리스트를 넣기만 하면!)
# .remove() (집합의 요소 삭제) / .discard() (역시 마찬가지지만, 해당하는 요소가 없을 때 사용해도 에러 안 뜸)
# .pop() (마지막 아이템을 제거하고 그 값을 리턴! 하지만 Set는 unindexed기 때문에 어떤 아이템이 삭제될지 예상할 수 없음)
