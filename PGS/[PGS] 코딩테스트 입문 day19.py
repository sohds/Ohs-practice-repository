### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 19 문자열, 배열, 조건문
# 7의 개수 (+1)
# 문제 설명 : 머쓱이는 행운의 숫자 7을 가장 좋아합니다. 
# 정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.

# my ver.
def solution(array):
    cnt = 0
    str_array = ''.join(map(str, array))
    ls_array = list(str_array)
    for i in range(0, len(ls_array)):
        if ls_array[i] == '7':
            cnt += 1
    return cnt

# other ver.
def solution(array):
    return str(array).count('7')

# the other ver.
def solution(array):
    return ''.join(map(str, array)).count('7')


# 잘라서 배열로 저장하기 (+2)
# 문제 설명 : 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.
def solution(my_str, n):
    answer = [my_str[i:i+n] for i in range(0, len(my_str), n)]
    return answer


# 중복된 숫자 개수 (+1)
# 문제 설명 : 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.

# my ver.
def solution(array, n):
    cnt = 0
    for i in array:
        if i == n:
            cnt += 1
    return cnt

# another ver. (sum 활용)
def solution(array, n):
    return sum(1 for x in array if x == n)



# 머쓱이보다 키 큰 사람 (+1)
# 문제 설명 : 머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 
# 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 
# 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.
def solution(array, height):
    answer = [i for i in array if i > height]
    return len(answer)
