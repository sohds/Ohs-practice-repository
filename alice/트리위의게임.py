## 라이브러리 임포트
from collections import deque  # for bfs

# 너비 우선 탐색 - leaf node가 끝으로 가야 하니까!
def bfs(n, tree):
    # 방문한 곳 기록
    visited = [False] * (n + 1)
    # for dp calculation
    stack = []
    # 큐에 미리 생성 (1부터 시작이니까!)
    queue = deque([1])
    visited[1] = True

    # 큐가 완전히 빌 때까지 반복
    while queue:
        # 큐에 삽입된 순서대로 노드 하나 꺼내기
        node = queue.popleft()
        # dp 차례대로 계산을 위해 stack 쌓아줌
        stack.append(node)
        for child in tree[node]:
            if not visited[child]:
                visited[child] = True
                queue.append(child)
    return stack


def calculate_dp(n, tree, stack):
    # dp 값 저장용
    dp = [0] * (n + 1)
    # 방문 했는지 확인용
    visited = [False] * (n + 1)
    
    # 스택이 완전히 빌 때까지 반복
    while stack:
        # 스택은 후입선출이니까 pop으로 뽑아서 node 선정
        node = stack.pop()
        # 해당 노드부터 점수 계산할거니까 visited했다고 True 선정
        visited[node] = True
        # bfs 알고리즘 사용 시, 마지막에 있을수록 leaf node이니까!
        isLeaf = True
        
        # 가장 큰 값으로 선정
        minChildValue = 9999999

        for child in tree[node]:
            # 자식노드가 방문되었으면 leaf node가 아님!
            if visited[child]:
                isLeaf = False
                # 자식 노드의 dp 값 중 최솟값을 사용하도록 함
                minChildValue = min(minChildValue, dp[child])
        
        # 리프 노드일 경우 자기 자신만 하고 게임이 끝나도록 해야하기 때문!
        if isLeaf:
            dp[node] = node
        else:
            dp[node] = node - minChildValue
    
    return dp


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    index += 1
    
    tree = [[] for _ in range(n+1)]
    
    for i in range(n-1):
        u = int(data[index])
        index += 1
        v = int(data[index])
        index += 1
        tree[u].append(v)
        tree[v].append(u)

    stack = bfs(n, tree)
    dp = calculate_dp(n, tree, stack)
    
    dp_results = []
    for i in range(1, n+1):
        if dp[i] >= 0:
            dp_results.append(1)  # 선공 승리
        else:
            dp_results.append(0)  # 후공 승리
    
    print("\n".join(map(str, dp_results)))


if __name__ == "__main__":
    main()