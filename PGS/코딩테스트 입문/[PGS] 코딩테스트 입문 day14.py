### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 14 조건문, 반복문, 시뮬레이션, 문자열
# 가까운 수 (+13)
# 문제 설명 : 정수 배열 array와 정수 n이 매개변수로 주어질 때, 
# array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.
# 제한 사항: 1 ≤ array의 길이 ≤ 100  /n  1 ≤ array의 원소 ≤ 100  /n  1 ≤ n ≤ 100
# 가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.

# wrong ver.
# reason thinking : 가까운 수가 여러 개일 경우 더 작은 수를 return 해야하는데 그러지 못하는 것으로 추정됨.
def solution(array, n):
    minus_arr = [ abs(n-array[i]) for i in range(len(array)) ]
    idx = minus_arr.index(min(minus_arr))
    return array[idx]

# solved ver.
def solution(array, n):
    abs_array = []
    array.sort()
    for i in array:
        abs_array.append(abs(n-i))
    answer = [array[abs_array.index(min(abs_array))]]
    if len(answer) > 1:
        return min(answer)
    else:
        return answer[0]

# short ver.
solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]
# 어떻게 이렇게 해결하지..
# lambda 함수 공부 필요할듯.


# 369게임 (+5)
# 문제 설명 : 머쓱이는 친구들과 369게임을 하고 있습니다. 
# 369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는 숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다. 
# 머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때, 머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.
def solution(order):
    answer = str(order).count('3') + str(order).count('6') + str(order).count('9')
    return answer


# 암호 해독 (+1)
# 문제 설명 : 군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다. 암호화된 문자열 cipher를 주고받습니다.
# 그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다. 
# 문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(cipher, code):
    real_code = [ cipher[k] for k in range(code-1, len(cipher), code) ]
    return ''.join(real_code)


# 대문자와 소문자 (+1)
# 문제 설명 : 문자열 my_string이 매개변수로 주어질 때, 
# 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.

# my ver.
def solution(my_string):
    str_list = []
    for i in my_string:
        if i.isupper() == True:
            str_list.append(i.lower())
        else:
            str_list.append(i.upper())
    return ''.join(str_list)

# use swap ver.
def solution(my_string):
    return my_string.swapcase()

# short ver.
def solution(my_string):
    return ''.join([x.upper() if x.islower() else x.lower() for x in my_string])