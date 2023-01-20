### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 11 수학, 반복문
# 주사위의 개수 (+1)
# 문제 설명 : 머쓱이는 직육면체 모양의 상자를 하나 가지고 있는데 이 상자에 정육면체 모양의 주사위를 최대한 많이 채우고 싶습니다. 
# 상자의 가로, 세로, 높이가 저장되어있는 배열 box와 주사위 모서리의 길이 정수 n이 매개변수로 주어졌을 때, 
# 상자에 들어갈 수 있는 주사위의 최대 개수를 return 하도록 solution 함수를 완성해주세요.
def solution(box, n):
    return (box[0]//n) * (box[1]//n) * (box[2]//n)


# 합성수 찾기 (+2)
# 문제 설명 : 약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 
# 자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.
def solution(n):
    composition = []
    for i in range(1, n+1):
        number = 0
        for k in range(1, n+1):
            if i % k == 0:
                number += 1
        if number > 2:
            composition.append(i)
    return len(composition)


# 최댓값 만들기(1) (+1)
# 문제 설명 : 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.
def solution(numbers):
    numbers.sort(reverse=True)
    a = numbers[0]
    b = numbers[1]
    return a * b


# 팩토리얼 (+5)
# 문제 설명 : i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다. 
# 정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.
# i! ≤ n
def solution(n):
    import math
    number = 10
    while n < math.factorial(number):
        number -= 1
    return number