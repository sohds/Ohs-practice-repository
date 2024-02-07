### 코딩테스트 연습 > 연습문제 >
 
# 코딩테스트 level 1 
# 정렬
## K번째수     (+1)
## 문제 설명
## 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

## 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

## array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
## 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
## 2에서 나온 배열의 3번째 숫자는 5입니다.
## 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, 
## commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

def solution(array, commands):
    answer = []
    for com in commands:
        temp = sorted(array[com[0]-1:com[1]])
        answer.append(temp[com[2]-1])
    return answer

# for문 사용안하고, lambda로 해결
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))



# 월간 코드 풀이 챌린지 1
## 두 개 뽑아서 더하기      (+1)
## 문제 설명
## 정수 배열 numbers가 주어집니다. 
## numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 
## 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

def solution(numbers):
    answer = []
    for idx in range(len(numbers)):
        for idx_2 in reversed(range(len(numbers))):
            if idx == idx_2:
                break
            else:
                answer.append(numbers[idx]+numbers[idx_2])
    return sorted(list(set(answer)))

# itertools
from itertools import combinations
def solution(numbers):
    return sorted(set(sum(i) for i in list(combinations(numbers, 2))))

# short ver.
def solution(numbers): 
    return sorted({numbers[i] + numbers[j] for i in range(len(numbers)) for j in range(len(numbers)) if i>j})



## 숫자 짝꿍    (+4)
## 문제 설명
## 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다
## (단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). 
## X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

## 예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 
## 다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다
## (X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
## 두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.

def solution(X, Y):
    answer = ''

    for i in range(9, -1, -1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer