### 코딩테스트 연습 > Summer/Winter Coding(~2018) >
### 코딩테스트 연습 > 완전탐색 >


# 코딩테스트 level 1

# 예산 (+2)
# 문제 설명 : S사에서는 각 부서에 필요한 물품을 지원해 주기 위해 부서별로 물품을 구매하는데 필요한 금액을 조사했습니다. 
# 그러나, 전체 예산이 정해져 있기 때문에 모든 부서의 물품을 구매해 줄 수는 없습니다. 
# 그래서 최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 합니다.
# 물품을 구매해 줄 때는 각 부서가 신청한 금액만큼을 모두 지원해 줘야 합니다. 
# 예를 들어 1,000원을 신청한 부서에는 정확히 1,000원을 지원해야 하며, 1,000원보다 적은 금액을 지원해 줄 수는 없습니다.
# 부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때, 
# 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수를 완성해주세요.

# 제한사항 : d는 부서별로 신청한 금액이 들어있는 배열이며, 길이(전체 부서의 개수)는 1 이상 100 이하입니다.
# d의 각 원소는 부서별로 신청한 금액을 나타내며, 부서별 신청 금액은 1 이상 100,000 이하의 자연수입니다.
# budget은 예산을 나타내며, 1 이상 10,000,000 이하의 자연수입니다.

# my ver.
def solution(d, budget):
    money = 0
    answer = 0
    
    if sum(d) <= budget:
        return len(d)
    
    else:
        d_list = sorted(d)
        for idx in range(len(d_list)):
            if budget >= d_list[idx]:
                budget -= d_list[idx]
                answer += 1
        return answer
    
# other ver.
# 대박 깔끔...
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)



# 최소직사각형 (+1)
# 문제 설명 : 명함 지갑을 만드는 회사에서 지갑의 크기를 정하려고 합니다. 
# 다양한 모양과 크기의 명함들을 모두 수납할 수 있으면서, 작아서 들고 다니기 편한 지갑을 만들어야 합니다. 
# 이러한 요건을 만족하는 지갑을 만들기 위해 디자인팀은 모든 명함의 가로 길이와 세로 길이를 조사했습니다.

# 아래 표는 4가지 명함의 가로 길이와 세로 길이를 나타냅니다.

# 명함 번호	가로 길이	세로 길이
# 1	60	50
# 2	30	70
# 3	60	30
# 4	80	40

# 가장 긴 가로 길이와 세로 길이가 각각 80, 70이기 때문에 80(가로) x 70(세로) 크기의 지갑을 만들면 모든 명함들을 수납할 수 있습니다. 
# 하지만 2번 명함을 가로로 눕혀 수납한다면 80(가로) x 50(세로) 크기의 지갑으로 모든 명함들을 수납할 수 있습니다. 
# 이때의 지갑 크기는 4000(=80 x 50)입니다.

# 모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다. 
# 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.

# 제한사항 : sizes의 길이는 1 이상 10,000 이하입니다. sizes의 원소는 [w, h] 형식입니다.
# w는 명함의 가로 길이를 나타냅니다. h는 명함의 세로 길이를 나타냅니다. w와 h는 1 이상 1,000 이하인 자연수입니다.


# my ver.
def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])

    return max(w) * max(h)

# other ver.
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
# 어떻게 이런 생각을 하지 . . .