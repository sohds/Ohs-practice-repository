### 코딩테스트 연습 > 연습문제 >
### 코딩테스트 연습 > 월간 코드 챌린지 시즌 3 >

# 코딩테스트 level 1

# 정수 내림차순으로 배치하기 (+1)
# 문제 설명 : 함수 solution은 정수 n을 매개변수로 입력받습니다. 
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
# 예를 들어 n이 118372면 873211을 리턴하면 됩니다.

# my ver.
def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    answer = ''.join(n)
    return int(answer)


# short ver.
def solution(n):
    return int("".join(sorted(list(str(int(n))), reverse=True)))



# 나머지가 1이 되는 수 찾기 (+1)
# 문제 설명 : 자연수 n이 매개변수로 주어집니다.
# n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 
# 답이 항상 존재함은 증명될 수 있습니다.

# my ver.
def solution(n):
    answer = 0
    for i in range(1, n):
        if n % i == 1:
            answer = i
            break
    return answer

# other ver.
def solution(n):
    return [x for x in range(1,n+1) if n%x==1][0]



# 하샤드 수 (+1)
# 문제 설명 : 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 
# 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 
# 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

# my ver.
def solution(x):
    xx = list(str(x))
    X = sum(list(map(int, xx)))
    return True if x % X == 0 else False

# short ver.
solution = lambda x : x%sum(int(i) for i in str(x))==0



# 두 정수 사이의 합 (+1)
# 문제 설명 : 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
# 제한 조건 : a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요. a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
# a와 b의 대소관계는 정해져있지 않습니다.

# my ver.
def solution(a, b):
    if a > b:
        a, b = b, a
    answer = 0
    for i in range(a, b+1):
        answer += i
    return answer

# other ver.
def adder(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))  # sum을 돌리는 방법을 생각 못함...



# 콜라츠 추측 (+1)
# 문제 설명 : 1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될 때까지 다음 작업을 반복하면, 
# 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.

# 1-1. 입력된 수가 짝수라면 2로 나눕니다. 
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다. 
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. 
# 예를 들어, 주어진 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 됩니다.
 
# 위 작업을 몇 번이나 반복해야 하는지 반환하는 함수, solution을 완성해 주세요. 
# 단, 주어진 수가 1인 경우에는 0을, 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환해 주세요.

# my ver.
def solution(num):
    count = 0
    
    while count < 500:
        if num % 2 == 0:
            num /= 2
        elif num == 1:
            break
        else:
            num = num*3 + 1
        count += 1
        
    if count < 500:
        return count
    else:
        return -1

# other ver.
def collatz(num):
    for i in range(500):
        num=num/2 if num%2==0 else num*3+1
        if num==1:
            return i+1
    return -1



# 서울에서 김서방 찾기 (missing)
# 문제 설명 : String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. 
# seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

# my ver.
def solution(seoul):
    answer = ''
    for x, name in enumerate(seoul):
        if name == 'Kim':
            answer = '김서방은 '+str(x)+'에 있다'
    return answer

# other ver.
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))