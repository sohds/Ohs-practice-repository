### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 10 조건문, 배열, 수학, 시뮬레이션
# 점의 위치 구하기 (+2)
# 문제 설명 : 사분면은 한 평면을 x축과 y축을 기준으로 나눈 네 부분입니다. 사분면은 아래와 같이 1부터 4까지 번호를 매깁니다.
# x 좌표와 y 좌표가 모두 양수이면 제1사분면에 속합니다.
# x 좌표가 음수, y 좌표가 양수이면 제2사분면에 속합니다.
# x 좌표와 y 좌표가 모두 음수이면 제3사분면에 속합니다.
# x 좌표가 양수, y 좌표가 음수이면 제4사분면에 속합니다.
# x 좌표 (x, y)를 차례대로 담은 정수 배열 dot이 매개변수로 주어집니다.
#  좌표 dot이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return 하도록 solution 함수를 완성해주세요.
def solution(dot):
    if dot[0] * dot[1] < 0:
        if dot[0] < 0:
            return 2
        else:
            return 4
    else:
        if dot[0] < 0:
            return 3
        else:
            return 1


# 2차원으로 만들기 (+2)
# 문제 설명 : 정수 배열 num_list와 정수 n이 매개변수로 주어집니다. 
# num_list를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.
# num_list가 [1, 2, 3, 4, 5, 6, 7, 8] 로 길이가 8이고 n이 2이므로 num_list를 2 * 4 배열로 다음과 같이 변경합니다. 
# 2차원으로 바꿀 때에는 num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 변경합니다.
import numpy as np
def solution(num_list, n):
    num_list = np.array(num_list)
    return (num_list.reshape(len(num_list) // n, n)).tolist()

# 다른 사람 풀이인데.. 언제 이런 레벨에 도달할 수 있을까
def solution(num_list, n):
    return [num_list[ix-n:ix] for ix in range(n, len(num_list)+1, n)]


# 공 던지기 (+5)
# 문제 설명 : 머쓱이는 친구들과 동그랗게 서서 공 던지기 게임을 하고 있습니다. 공은 1번부터 던지며 
# 오른쪽으로 한 명을 건너뛰고 그다음 사람에게만 던질 수 있습니다. 
# 친구들의 번호가 들어있는 정수 배열 numbers와 정수 K가 주어질 때, 
# k번째로 공을 던지는 사람의 번호는 무엇인지 return 하도록 solution 함수를 완성해보세요.
def solution(numbers, k):
    players = numbers[0::2] if len(numbers) % 2 ==0 else numbers[0::2] + numbers[1::2] 
    # [0::2] 리스트의 처음부터 인덱스를 2씩 증가시키면서 끝 인덱스까지 가져옴 
    return players[(k % len(players)) -1]


# 배열 회전시키기 (+1)
# 문제 설명 : 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 
# 배열 numbers의 원소를 direction 방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.

# 왜 안되는지 이해가 안 가는 ver.
def solution(numbers, direction):
    new_numbers = numbers[1:]
    if direction == 'right':
        new_numbers.insert(0, numbers[0])
    elif direction == 'left':
        new_numbers.append(numbers[0])
    return new_numbers

# 해결한 ver.
def solution(numbers, direction):
    from collections import deque
    numbers = deque(numbers) # deque를 사용하기위해 deque를 import해준다.
    if direction == 'right':
        numbers.rotate(1)    # right면 rotate()함수를 이용하여 오른쪽으로 1칸 이동한다.
    elif direction == 'left':
        numbers.rotate(-1)   # left 면 rotate()함수를 이용하여 왼쪽으로 1칸 이동 한다.
    return list(numbers)     # deque를 사용하면 deque형으로 바뀌기 때문에 list로 변환 해주고 return 해준다.
 
# 숏 코딩 ver.
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]