### 코딩테스트 입문
### 하루 4문제 매일 도전 task

# Day 25 시뮬레이션, 조건문, 수학
# 문자열 밀기 (+1)
# 문제 설명 : 문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 
# 이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때, 
# A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

# my ver.
def solution(A, B):
    if A == B:
        return 0
    else:
        array = [A, A[-1]+A[:-1]]
        for _ in range(len(A)-2):
            factor = array[-1]
            array.append(factor[-1]+factor[:-1])
            
        if B in array:
            return array.index(B)
        
        else:
            return -1

# short ver.
# 나 코딩 왜 배움? ㅋㅋㅋㅋㅋ,,,
solution=lambda a,b:(b*2).find(a)



# 종이 자르기 (+1)
# 문제 설명 : 머쓱이는 큰 종이를 1 x 1 크기로 자르려고 합니다. 
# 예를 들어 2 x 2 크기의 종이를 1 x 1 크기로 자르려면 최소 가위질 세 번이 필요합니다.
# 정수 M, N이 매개변수로 주어질 때, M x N 크기의 종이를 최소로 가위질 해야하는 횟수를 return 하도록 solution 함수를 완성해보세요.

# my ver.
def solution(M, N):
    cut_M = 0
    if M > 1 or N > 1:
        if M > 1:
            cut_M = M - 1
        if N > 1:
            N -= 1
        return M * N + cut_M
    elif M == 1 and N == 1:
        return 0

# short ver.
def solution(M, N):
    return (M * N) - 1
# 설마 했는데 그냥 수학 공식으로 풀어도 되나봄..



# 연속된 수의 합 (+1)
# 문제 설명 : 연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 두 정수 num과 total이 주어집니다. 
# 연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.
def solution(num, total):
    average = total // num
    return [i for i in range(average - (num-1)//2, average + (num + 2)//2)] 
    # 좌, 우측 숫자의 개수는 num이 짝수이냐 홀수이냐에 따라 다르기 때문에 왼쪽 끝 값을 구하기 위해서는 
    # num - 1로 하고 우측은 num + 2를 하면 짝수, 홀수를 구분하지 않고 연속적인 리스트를 구할 수 있음!
# 왜 자꾸 수학문제가 나오지 . . .



# 다음에 올 숫자 (+1)
# 문제 설명 : 등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 
# 마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.
def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
        return common[-1] + (common[1] - common[0])
    else:
        return common[-1] * (common[1] / common[0])
