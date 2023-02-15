### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 5 수학, 배열 (2)
# 옷가게 할인 받기 (+12)
# 문제 설명 : 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
# 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.
def solution(price):
    if price >= 500000:
        return int(price * 0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return int(price * 0.95)
    else:
        return price

# 아이스 아메리카노 (+1)
# 문제 설명 : 머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 아이스 아메리카노는 한잔에 5,500원입니다. 
# 머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 
# 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(money):
    ice_ame = 5500
    amount = money // ice_ame
    r_money = money % ice_ame
    answer = [amount, r_money]
    return answer

# 나이 출력 (+1)
# 문제 설명 : 머쓱이는 40살인 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 
# 나이 age가 주어질 때, 2022년을 기준 출생 연도를 return 하는 solution 함수를 완성해주세요.
def solution(age):
    return 2022-age+1

# 배열 뒤집기 (+1)
# 문제 설명 : 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. 
# num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    answer = num_list[::-1]
    return answer