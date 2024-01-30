### 121. 정수를 나선형으로 배치하기   (+1)
## 문제 설명
## 양의 정수 n이 매개변수로 주어집니다. 
## n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(n):
    if n == 1:
        return [[1]]
    
    answer = [[0]*n for i in range(n)]
    x, y = 0, 0
    dir = 'r'
    
    for i in range(n*n):
        answer[x][y] = i + 1
        if dir == 'r':
            y += 1
            if y == n-1 or answer[x][y+1] != 0:
                dir = 'd'
        elif dir == 'd':
            x += 1
            if x == n-1 or answer[x+1][y] != 0:
                dir = 'l'
        elif dir == 'l':
            y -= 1
            if y == 0 or answer[x][y-1] != 0:
                dir = 'u'
        elif dir == 'u':
            x -= 1
            if x == n-1 or answer[x-1][y] != 0:
                dir = 'r'
                
    return answer



### 122. 특별한 이차원 배열 2     (+1)
## 문제 설명
## n × n 크기의 이차원 배열 arr이 매개변수로 주어질 때, arr이 다음을 만족하면 1을 아니라면 0을 return 하는 solution 함수를 작성해 주세요.

## 0 ≤ i, j < n인 정수 i, j에 대하여 arr[i][j] = arr[j][i]
def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[j][i]:
                continue
            else:
                return 0
    
    return 1



### 123. 정사각형으로 만들기    (+2)
## 문제 설명
## 이차원 정수 배열 arr이 매개변수로 주어집니다. 
## arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고, 
## 열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 각 열의 끝에 0을 추가한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.
def solution(arr):
    for i in range(len(arr)):
        if len(arr) > len(arr[i]):
            diff = len(arr) - len(arr[i])
            for _ in range(diff):
                arr[i].append(0)
        elif len(arr) < len(arr[i]):
            diff = len(arr[i]) - len(arr)
            for _ in range(diff):
                arr.append([0]*len(arr[i]))
        
        else: break
    return arr



### 124. 이차원 배열 대각선 순회하기     (+2)
## 문제 설명
## 2차원 정수 배열 board와 정수 k가 주어집니다.

## i + j <= k를 만족하는 모든 (i, j)에 대한 board[i][j]의 합을 return 하는 solution 함수를 완성해 주세요.
def solution(board, k):
    hap = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i+j <= k:
                hap += board[i][j]
    return hap

# list comprehension
def solution(board, k):
    return sum(board[i][j] for i in range(len(board)) for j in range(len(board[0])) if i + j <= k)