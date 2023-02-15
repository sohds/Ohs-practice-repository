### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 3 사칙연산, 배열, 수학
# 나머지 구하기 (+1)
# 문제 상황 : 정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.
def solution(num1: int, num2: int) -> int:
    return num1 % num2

# 중앙값 구하기 (+3)
# 문제 상황 : 중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 
# 예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.
def solution(array):
    array.sort()
    if len(array) % 2 == 1:
        return array[(len(array) // 2)]
    else:
        md1 = array[(len(array) / 2 - 1)]
        md2 = array[((len(array) / 2))]
        return (md1 + md2) / 2

# 최빈값 구하기
# 문제 상황 : 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
# 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

# (ver1, 이 버전으로 했을 시 최빈값 여러 개 나오는 경우 -1 반환 불가능)
def solution(array):
    numbers = []
    for i in range(0, 1000):
        numbers.append(i)
        
    max_occurence = 0
    max_number = numbers[0]
    
    for number in numbers:
        occurence = 0
        for k in array:
            if k == number:
                occurence += 1
            
            if occurence > max_occurence:
                max_occurence = occurence
                max_number = number
                
    return max_number
  
# (ver2, +9)
def solution(array):
    numbers = []
    n_numbers = []
    for j in range(0, 1000):
        numbers.append(j)
        n_numbers.append(0)
    
    for number in numbers:
        for num in array:
            if num == number:
                n_numbers[number] += 1
    
    m = max(n_numbers)
    find_mode_index = [i for i, v in enumerate(n_numbers) if v == m]
    if len(find_mode_index) > 1:
        return -1
    else:
        return numbers[n_numbers.index(max(n_numbers))]
      
# 짝수는 싫어요 (+1)
# 문제 상황 : 정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.
def solution(n):
    answer = []
    for i in range(1, n+1):
        if i % 2 == 1:
            answer.append(i)
        else:
            continue
    return answer
