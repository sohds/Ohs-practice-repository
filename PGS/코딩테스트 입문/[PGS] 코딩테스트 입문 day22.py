### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 22 문자열, 사칙연산, 시뮬레이션, 2차원배열, 수학, 배열
# 저주의 숫자 3 (+3)
# 문제 설명 : 3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다. 3x 마을 사람들의 숫자는 다음과 같습니다.
# 1	 1	6	8
# 2	 2	7	10
# 3	 4	8	11
# 4	 5	9	14
# 5  7	10	16
# 정수 n이 매개변수로 주어질 때, n을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.
def solution(n):
    threex_num = []
    i = 1
    while len(threex_num) < 100:
        if i % 3 != 0 and '3' not in str(i):
            threex_num.append(i)
        i += 1
    return threex_num[n-1]



# 평행 (+4)
# 문제 설명 : 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.
# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

# my ver.
def solution(dots):
    idx = [ 1, 2, 3 ]
    for k in range(1, len(dots)-1):
        first_slope = (dots[k][1]-dots[0][1]) / (dots[k][0]-dots[0][0])
        idx.remove(k)
        second_slope = (dots[idx[1]][1]-dots[idx[0]][1]) / (dots[idx[1]][0]-dots[idx[0]][0])
        idx = [ 1, 2, 3 ]
        if first_slope == second_slope:
            return 1
    return 0

# other ver.
from itertools import combinations

def solution(dots):
    a = []
    for (x1,y1),(x2,y2) in combinations(dots,2):
        a.append((y2-y1,x2-x1))

    for (x1,y1),(x2,y2) in combinations(a,2):
        if x1*y2==x2*y1:
            return 1
    return 0



# 겹치는 선분의 길이 (+7)
# 문제 설명 : 선분 3개가 평행하게 놓여 있습니다. 
# 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 
# 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.
# lines가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.
# 선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 길이 2만큼 겹쳐있습니다.

# set() 자구를.. 사용했어야만 했다!
# other ver.
def solution(lines):
    table = [set([]) for _ in range(200)]
    for index, line in enumerate(lines):
        a, b = line
        for i in range(a, b):
            table[i + 100].add(index)

    count = 0
    for line in table:
        if len(line) > 1:
            count += 1

    return count

# another ver.
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])



# 유한소수 판별하기 (+8)
# 문제 설명 : 소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다. 
# 분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다. 유한소수가 되기 위한 분수의 조건은 다음과 같습니다.
# 기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.
# 두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을, 무한소수라면 2를 return하도록 solution 함수를 완성해주세요.
import math
def solution(a, b):
    c = math.gcd(a, b)
    numer = a / c
    denomi = b / c
    while denomi % 2 == 0:
        denomi //= 2    # 2로 나누어 떨어지면 2로 나눈 값 넣기
    while denomi % 5 == 0:
        denomi //= 5    # 5로 나누어 떨어지면 5로 나눈 값 넣기
    return 1 if denomi == 1 or numer % denomi == 0 else 2