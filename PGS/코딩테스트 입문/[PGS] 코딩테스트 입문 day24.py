### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 24 수학, 시뮬레이션, 문자열, 조건문, 반복문
# 치킨 쿠폰 (+6)
# 문제 설명 : 프로그래머스 치킨은 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다. 
# 쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 서비스 치킨에도 쿠폰이 발급됩니다. 
# 시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때 받을 수 있는 최대 서비스 치킨의 수를 return하도록 solution 함수를 완성해주세요.
def solution(chicken):
    answer = 0
    
    while chicken >= 10:
        div = chicken // 10
        mod = chicken % 10
        
        answer += div
        chicken = div + mod
        
    return answer



# 이진수 더하기 (+ 몇점.. 이더라 ㅎ.. 가물가물)
# 문제 설명 : 이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.
def solution(bin1, bin2):
    a = int(bin1, 2)     # bin1을 int로 묶어주는데 2진법의 형태로 묶어줌
    b = int(bin2, 2)
    answer = bin(a+b)    # bin 함수를 통해서 숫자를 2진수의 형태의 문자열로 변환할 수 있음
                         # 2진수 형태 문자열인 이유! 0을 살려주려면 문자열이어야 하기 때문
    return answer[2:]    # 2진수라는 것인걸 표기하기 위해 0b 라는 접두어가 붙어서 이를 제외시키고 출력



# A로 B 만들기 (+2)
# 문제 설명 : 문자열 before와 after가 매개변수로 주어질 때, 
# before의 순서를 바꾸어 after를 만들 수 있으면 1을, 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

# my ver.
def solution(before, after):
    before = list(before)
    after = list(after)
    before.sort()
    after.sort()
    return 1 if after == before else 0

# short ver.
def solution(before, after):
    return 1 if sorted(before)==sorted(after) else 0
# 굳이 리스트로 바꾸지 않아도, 문자열에서 바로 sorted 해줘도 됨.. 자꾸 잊네 이거를



# k의 개수 (+1)
# 문제 설명 : 1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다. 
# 정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.

# my ver.
def solution(i, j, k):
    answer = 0
    k = str(k)
    for num in range(i, j+1):
        if k in str(num):
            answer += str(num).count(k)
    return answer

# short ver.
def solution(i, j, k):
    return sum(map(lambda v: str(v).count(str(k)), range(i, j+1)))
# lambda에 익숙해졌으니 이제 lambda를 자주 써먹어보도록 하자..!