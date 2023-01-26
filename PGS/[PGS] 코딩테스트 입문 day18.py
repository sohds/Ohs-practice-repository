### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 18 문자열, 수학, 조건문, 정렬
# 문자열 안에 문자열 (+2)
# 문제 설명 : 문자열 str1, str2가 매개변수로 주어집니다. str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.
def solution(str1, str2):
    return 1 if str2 in str1 else 2


# 제곱수 판별하기 (+2)
# 문제 설명 : 어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 
# 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

# 런타임이 너무 긴 내 버전.. 다른 풀이 방법도 있을 것 같은데
def solution(n):
    square_num = [ k ** 2 for k in range(1, 1000001) ]
    
    if n in square_num:
        return 1
    else:
        return 2
    
# short ver.
def solution(n):
    return 1 if (n ** 0.5) % 1 == 0 else 2
# 2분의 1승을 전혀 생각 못했네 ㅋ...


# 세균 증식 (+1)
# 문제 설명 : 어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 
# 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.
def solution(n, t):
    return n * (2 ** t)