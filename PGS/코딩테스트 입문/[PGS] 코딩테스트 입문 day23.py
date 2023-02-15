### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 23 배열, 정렬, 문자열
# 특이한 정렬 (+2)
# 문제 설명 : 정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 
# 정수가 담긴 배열 numlist와 정수 n이 주어질 때 
# numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.

# my ver.
def solution(numlist, n):
    abs_list = list(map(lambda x: abs(n-x), numlist))
    # abs_list라는 리스트를 만들어주는데, numlist라는 리스트에서 abs(절댓값) 함수를 씌운 리스트를 만들어 줌
    # lambda 매개변수 : 표현식
    abs_order = sorted(abs_list)
    result = [ abs_order.index(a)+1 for a in abs_list ]
    idx_abs = [[idx, num] for idx, num in zip(result, numlist)]
    # zip 함수로 순위와 numlist에 저장돼있던 숫자를 묶어줌
    idx_abs.sort(key=lambda x: (x[0], -x[1]))
    # 특정 인덱스에 대해서만 정렬을 하려면 key를 이용할 수 밖에 없어서 이렇게 해줌
    # x: ( ) 의 괄호안에 튜플 형식으로 집어넣어주는데, 
    # 이 때 -를 하게되면 역으로 정렬시킬 수 있어서 큰 숫자가 먼저 나와야 하니 num을 내림차순 배열로 바꿔줌
    # 여기서는 먼저 0번째 인덱스에 대해서 오름차순으로 정렬한 뒤, 동일한 값의 경우 내림차순으로 재정렬됨
    return [ final[1] for final in idx_abs ]

# short ver.
def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer
# 왜 똑같이 lambda를 써도.. 나는 이렇게 길고 이 사람은 이렇게 짧지...
# 설명 : answer = sorted(numlist,key = lambda x : (abs(x-n), n-x)) key에 요소를 리스트 혹은 튜플로 두 개 이상 줄 수 있다. 
# 이 경우 앞에 값이 같을 때 뒤의 값을 이용해서 나열한다. 요소 하나이고 값이 같을 때는 먼저 처리된 수가 먼저 나열되는 것 같다(인덱스가 작은 것이).



# 등수 매기기 (+6)
# 문제 설명 : 영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다. 
# 영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 
# 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.

# my ver.
def solution(score):
    mean_score = [ (test[0]+test[1])/2 for test in score ]
    mean_set = sorted(mean_score)
    # 정렬된 리스트를 만들기!
    # sort()는 리스트 자체를 정렬해버리기 때문에, 정렬된 객체를 생성하는 sorted()를 써야함
    mean_set.reverse()
    # sorted() 는 오름차순이니까 내림차순으로 바꿔줌
    rank = [ mean_set.index(idx)+1 for idx in mean_score ]
    return rank

# short ver.
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]
# 나도 언제쯤 이렇게 간결하게 짤 수 있을까..



# 옹알이(1) (+1)
# 문제 설명 : 머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 
# 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 
# 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

# my ver.
from itertools import permutations                             # 순열을 이용해서 만들 수 있는 단어의 조합을 다 만들어봄..

def solution(babbling):
    one = ["aya", "ye", "woo", "ma"]
    
    two_combo = list(permutations(one, 2))
    for x in range(0, len(two_combo)):
        two_combo[x] = ''.join(list(two_combo[x]))             # permutations 사용하면 튜플로 묶인 리스트 값으로 나오기 때문에,
                                                               # 튜플을 리스트로 바꾸고, 문자열로 묶어 하나의 단어로 만들어 리스트 처리해줌
        
    three_combo = list(permutations(one, 3))
    for x in range(0, len(three_combo)):
        three_combo[x] = ''.join(list(three_combo[x]))
        
    four_combo = list(permutations(one, 4))
    for x in range(0, len(four_combo)):
        four_combo[x] = ''.join(list(four_combo[x]))
    
    saying = one + two_combo + three_combo + four_combo        # 문자열 요소로 이뤄진 리스트기 때문에 플러스로 묶어줌
    
    return len([word for word in babbling if word in saying])
# 도대체 이게 왜 1점짜리 문제지.. 정답률이 27퍼면서...
# 너무 비효율적인 코드같다! 시간이 너무 오래 걸린다. 제일 심한건 0.16ms 걸림..

# short ver.
def solution(babbling):
    return len(list(filter(lambda x: x.replace("aya", "").replace("ye", "").replace("woo", "").replace("ma", "") == "" and "ayaaya" not in x and "yeye" not in x and "woowoo" not in x and "mama" not in x, babbling)))
# 어안이 벙벙.. replace 활용할 방법을 아예! 생각 못함
# 짧긴 한데.. 주석이 없으면 이해 못할 코드일 것 같다



# 로그인 성공? (+4)
# 문제 설명 : 머쓱이는 프로그래머스에 로그인하려고 합니다. 
# 머쓱이가 입력한 아이디와 패스워드가 담긴 배열 id_pw와 회원들의 정보가 담긴 2차원 배열 db가 주어질 때, 
# 다음과 같이 로그인 성공, 실패에 따른 메시지를 return하도록 solution 함수를 완성해주세요.

# 조건 : 아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 "login"을 return합니다.
# 로그인이 실패했을 때 아이디가 일치하는 회원이 없다면 “fail”를, 
# 아이디는 일치하지만 비밀번호가 일치하는 회원이 없다면 “wrong pw”를 return 합니다.

# my ver.
def solution(id_pw, db):
    for tryin in db:
        if tryin[0] == id_pw[0]:
            if tryin[1] == id_pw[1]:
                return 'login'
            elif tryin[1] != id_pw[1]:
                return 'wrong pw'
        else:
            continue
    return 'fail'

# short ver.
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):                       # := <- python 3.8부터 새로나온 기능이라는데.. 뭐지? 다시 알아봐야할듯
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"