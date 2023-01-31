### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 20 수학, 시뮬레이션, 문자열, 사칙연산
# 직사각형 넓이 구하기 (+8)
# 문제 설명 : 2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다. 
# 직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열 dots가 매개변수로 주어질 때, 
# 직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.

# my ver.
def solution(dots):
    x_dot = []
    y_dot = []
    for dot in dots:
        if dot[0] not in x_dot:
            x_dot.append(dot[0])
        if dot[1] not in y_dot:
            y_dot.append(dot[1])
    len_x = abs(x_dot[0]-x_dot[1])
    len_y = abs(y_dot[0]-y_dot[1])
    return len_x * len_y

# short ver.
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])



# 캐릭터의 좌표 (+10)
# 문제 설명 : 머쓱이는 RPG게임을 하고 있습니다. 
# 게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다. 
# 예를 들어 [0,0]에서 up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1], left를 누른다면 [-1, 0], right를 누른다면 [1, 0]입니다. 
# 머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다. 
# 캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.
    # [0, 0]은 board의 정 중앙에 위치합니다. 
    # 예를 들어 board의 가로 크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지 오른쪽으로 최대 [4, 0]까지 이동할 수 있습니다.

# my ver.. 8번 테스트 케이스에서만 오류
def solution(keyinput, board):
    result = [0, 0]
    map_size = [ k//2 for k in board ]
    print(map_size)
    for i in keyinput:
        if i == 'left':
            result[0] -= 1
        elif i == 'right':
            result[0] += 1
        elif i == 'up':
            result[1] += 1
        elif i == 'down':
            result[1] -= 1
    if abs(result[0]) > map_size[0]:
        if result[0] * map_size[0] <= 0:
            result[0] = -(map_size[0])
        else:
            result[0] = map_size[0]
    if abs(result[1]) > map_size[1]:
        if result[1] * map_size[1] <= 0:
            result[1] = -(map_size[1])
        else:
            result[1] = map_size[1]
    return result

# web ver.
# 전형적인 시뮬레이션.. 의 문제라는데 조금 더 공부가 필요할듯 하다.
def solution(keyinput, board):
    limit_x = (board[0] - 1) // 2
    limit_y = (board[1] - 1) // 2

    commands = {
        "up": [0, 1],
        "down": [0, -1],
        "left": [-1, 0],
        "right": [1, 0],
    }

    x = y = 0
    for command in keyinput:
        dx, dy = commands[command]
        nx, ny = x + dx, y + dy
        if abs(nx) <= limit_x and abs(ny) <= limit_y:
            x, y = nx, ny

    return [x, y]



# 최댓값 만들기(2) (+7)
# 문제 설명 : 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

# my ver.. but 런타임에러 2문제 발생
def solution(numbers):
    neg_num = [ k for k in numbers if k < 0 ]
    pos_num = [ j for j in numbers if j >= 0 ]
    pos_num.sort(reverse=True)
    if len(neg_num) > 1:
        multi_neg = [ neg_num[i] * neg_num[i+1] for i in range(0, len(neg_num)-1)]
        if pos_num[0] * pos_num[1] < max(multi_neg):
            return max(multi_neg)
        else:
            return pos_num[0] * pos_num[1]
    else:
        return pos_num[0] * pos_num[1]

# short ver.
def solution(numbers):
    numbers.sort(reverse = True)
    return max(numbers[0] * numbers[1],numbers[-1] * numbers[-2])



# 다항식 더하기 (+15)
# 문제 설명 : 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 
# 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 
# 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 
# 같은 식이라면 가장 짧은 수식을 return 합니다.

# my ver.. 가히 어떻게 풀어야할지 감도 안 잡힘
def solution(polynomial):
    answer = ''
    n = 0
    num  = 0
    poly = polynomial.split(' + ') 
    for p in poly:
        if p.isnumeric():
            num += int(p)
        else:
            if 'x' in p:
                if len(p) == 1:
                    n += 1
                else: 
                    n += int(p[:-1])
    if num != 0:
        if n == 1:
            answer = 'x + '+str(num)
        elif n > 1:
            answer = str(n)+'x + '+str(num)
        else:
            answer = str(num)
    else:
        if n == 1:
            answer = 'x'
        else:
            answer = str(n)+'x'
    return answer

# 오늘 문제들은 대체적으로 다 오래 걸리는 것들이라 더 지치는 것 같다..
# 앞으로도 지속적으로 계속 코테 문제를 풀어야겠다. 