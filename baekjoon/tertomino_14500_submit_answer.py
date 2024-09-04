import sys
input = sys.stdin.readline

# direction 정의 - ['x축 이동', 'y축 이동']
# 상[0], 하[1], 좌[2], 우[3]
direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]

# 최종 return 값
total = -1

def dfs(num, x, y, temp):
    global total
    if num == 4:
        total = max(total, temp)
        return
        
    # 현재 값에서 max_score 값을 나머지 칸 수만큼 더해도 작거나 같으면 탐색 중단
    # 이 경로에서는 최댓값을 구할 가능성이 없음
    if (temp + max_score * (4 - num)) <= total:
        return
    
    else:
        for i in range(4):
            # 상, 하, 좌, 우 탐색
            x_pos = x + direction[i][0]
            y_pos = y + direction[i][1]
            
            if 0 <= x_pos < rows and 0 <= y_pos < cols and board[x_pos][y_pos] == 0:
                board[x_pos][y_pos] = 1
                if num == 2:    # T자 모양을 처리하기 위한 조건
                    dfs(num+1, x, y, temp + matrix[x_pos][y_pos])
                dfs(num+1, x_pos, y_pos, temp + matrix[x_pos][y_pos])
                # 탐색 끝나서 0으로 되돌려둠
                board[x_pos][y_pos] = 0
            

if __name__ == "__main__":    
    # 첫 번째 줄을 읽어서 행과 열의 크기를 결정
    first_line = input().split()
    rows = int(first_line[0])
    cols = int(first_line[1])

    # 행렬을 생성
    matrix = [list(map(int, input().split())) for _ in range(rows)]
    # 테트로미노 위치 확인
    board = [[0]*cols for _ in range(rows)]
    # 최댓값 찾기
    max_score = max(map(max, matrix))
    
    for p in range(rows):
        for j in range(cols):
            board[p][j] = 1
            dfs(1, p, j, matrix[p][j])
            board[p][j] = 0
            
    print(total)