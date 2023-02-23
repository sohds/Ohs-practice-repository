### 코딩테스트 연습 > 연습문제 >
### 코딩테스트 연습 > 월간 코드 챌린지 시즌 2 >
### 코딩테스트 연습 > 월간 코드 챌린지 시즌 3 >

# 코딩테스트 level 1

# 나누어 떨어지는 숫자 배열 (+1)
# 문제 설명 : array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
# 제한사항 : arr은 자연수를 담은 배열입니다. 정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
# divisor는 자연수입니다. array는 길이 1 이상인 배열입니다.

# my ver.
def solution(arr, divisor):
    answer = [ i for i in arr if i % divisor == 0 ]
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
    return answer

# other ver.
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]



# 핸드폰 번호 가리기 (+1)
# 문제 설명 : 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 
# 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

def solution(phone_number):
    num = len(phone_number) - 4
    return '*'*num + phone_number[-4:]



# 제일 작은 수 제거하기 (+3)
# 문제 설명 : 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 
# 예를 들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.
# 제한 조건 : arr은 길이 1 이상인 배열입니다. 인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.

def solution(arr):
    answer = []
    if len(arr) < 2:
        answer.append(-1)
        return answer
    else:
        arr.remove(min(arr))
        return arr
    


# 음양 더하기 (+1)
# 문제 설명 : 어떤 정수들이 있습니다. 
# 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 
# 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
# 제한사항 : absolutes의 길이는 1 이상 1,000 이하입니다. absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.
# signs의 길이는 absolutes의 길이와 같습니다. signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.

# my ver.
def solution(absolutes, signs):
    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] *= -1
    return sum(absolutes)

# other ver.
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
    # zip 함수 쓸 생각 해보긴 했는데 이렇게도 써먹을 수 있을 줄이야..
    


# 없는 숫자 더하기 (+1)
# 문제 설명 : 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

# my ver.
def solution(numbers):
    answer = [ i for i in range(10) if i not in numbers ]
    return sum(answer)

# other ver.
def solution(numbers):
    return 45 - sum(numbers) # 수학 바보 된 기분 레전드...