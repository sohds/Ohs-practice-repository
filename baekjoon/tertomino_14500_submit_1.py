import sys
input = sys.stdin.readline

def create_matrix():
    # 첫 번째 줄을 읽어서 행과 열의 크기를 결정
    first_line = input().split()
    rows = int(first_line[0])
    cols = int(first_line[1])

    # 행렬을 생성
    matrix = []
    
    # 나머지 줄들을 읽어서 행렬에 추가
    for _ in range(rows):
        row_data = list(map(int, input().split()))
        matrix.append(row_data)
    
    return matrix

def find_max_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Step 1: 이중 리스트에서 가장 큰 값을 찾고 그 인덱스를 저장
    max_value = float('-inf')
    max_position = (0, 0)
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_position = (i, j)
    
    # Step 2: 가장 큰 값의 위치에서 상하좌우로 이동하며 최대 4개의 값을 더함
    max_sum = max_value
    current_position = max_position
    visited = set()
    visited.add(current_position)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향
    for _ in range(3):
        current_max_value = float('-inf')
        next_position = None
        
        for dx, dy in directions:
            nx, ny = current_position[0] + dx, current_position[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if matrix[nx][ny] > current_max_value:
                    current_max_value = matrix[nx][ny]
                    next_position = (nx, ny)
        
        if next_position:
            visited.add(next_position)
            current_position = next_position
            max_sum += current_max_value
    
    return max_sum

if __name__ == "__main__":    
    matrix = create_matrix()
    result = find_max_sum(matrix)
    print(result)