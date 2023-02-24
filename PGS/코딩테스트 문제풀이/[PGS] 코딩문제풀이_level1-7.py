### 코딩테스트 연습 > 연습문제 >
### 코딩테스트 연습 > 월간 코드 챌린지 시즌 1 >


# 코딩테스트 level 1

# 가운데 글자 가져오기 (+1)
# 문제 설명 : 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두 글자를 반환하면 됩니다.

# my ver.
def solution(s):
    return s[len(s)//2] if len(s)%2 == 1 else s[len(s)//2-1:len(s)//2+1]
    
# other ver.
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]



# 수박수박수박수박수박수? (+1)
# 문제 설명 : 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 
# 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

# my ver.
def solution(n):
    answer = ''
    if n % 2 == 1:
        answer += '수박'*(n//2) + '수'
    else:
        answer += '수박'*(n//2)
    return answer

# other ver.
def water_melon(n):
    str = "수박" * n
    return str[:n]



# 내적 (+1)
# 문제 설명 : 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.
# 이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)

# my ver.
def solution(a, b):
    answer = [ a[i] * b[i] for i in range(len(a)) ]
    return sum(answer)

# other ver.
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])