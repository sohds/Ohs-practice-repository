### 코딩테스트 입문
### 하루 4문제 매일 도전 task

## Day 21 문자열, 사칙연산, 시뮬레이션, 2차원배열, 수학, 배열
# 숨어있는 숫자의 덧셈(2) (+5)
# 문제 설명 : 문자열 my_string이 매개변수로 주어집니다. 
# my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

# my ver.
import re
def solution(my_string):
    full_num = re.findall(r'\d+', my_string)
    int_num = list(map(int, full_num))
    return sum(int_num)
# re 모듈은 TIL에 정리해두기

# 정규식 없이 푸는 방법
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())



# 안전지대 (+)
# 문제 설명 : 다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
# (그림 설명; 9x9 모눈이 있으면 가운데에 폭탄이 있고 나머지 부분에 X표 표시처리가 된 모습)
# 지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
# 지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

# https://velog.io/@seulki971227/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.0-%EC%95%88%EC%A0%84%EC%A7%80%EB%8C%80-Python
# 지금 내 수준에서는 절대 못 풀 것 같다.. 나는 개발자 신생아 수준인 것 같다..
# 내일 맑은 정신에 다시...


# 삼각형의 완성조건(2) (+1)
# 문제 설명 : 선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.
# 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
# 삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 
# 나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요.

# my ver.
def solution(sides):
    s1 = min(sides)
    s2 = max(sides)
    answer = [ i for i in range(1, s2+1) if s2 < s1 + i ]
    for k in range(s2+1, 2000):
        if k < s1 + s2:
            answer.append(k)
        else:
            break
    return len(answer)

# 와.. 공식을 잊은 자.. 숏코딩이 불가능하다
def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1



# 외계어 사전 (+3)
# 문제 설명 : PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 
# 알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. 
# spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.

# my ver.
# 바보 같이.. 짧은 코딩으로 해내지 못하는 내가 너무 밉다 . . .
def count_frequency(my_list):
    count = {}
    for item in my_list:
        count[item] = count.get(item, 0) + 1
        # 해당 key가 없을 때 반환되는 값을 0이 반환되게 바꾸기 위해 item 뒤에 0으로 지정해줌
    return count

def solution(spell, dic):
    spell_in_dic = []
    for i in range(0, len(spell)):
        for k in dic:
            if spell[i] in k:
                spell_in_dic.append(k)
    result = count_frequency(spell_in_dic)
    print(result.values())
    if len(spell) in result.values():
        return 1
    else:
        return 2