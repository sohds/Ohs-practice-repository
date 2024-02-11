### 코딩테스트 연습 > 연습문제 >

## 추억 점수     (+1)
## 문제 설명
## 사진들을 보며 추억에 젖어 있던 루는 사진별로 추억 점수를 매길려고 합니다. 
## 사진 속에 나오는 인물의 그리움 점수를 모두 합산한 값이 해당 사진의 추억 점수가 됩니다. 
## 예를 들어 사진 속 인물의 이름이 ["may", "kein", "kain"]이고 
## 각 인물의 그리움 점수가 [5점, 10점, 1점]일 때 해당 사진의 추억 점수는 16(5 + 10 + 1)점이 됩니다. 
## 다른 사진 속 인물의 이름이 ["kali", "mari", "don", "tony"]이고 ["kali", "mari", "don"]의 그리움 점수가 각각 [11점, 1점, 55점]]이고, 
## "tony"는 그리움 점수가 없을 때, 이 사진의 추억 점수는 3명의 그리움 점수를 합한 67(11 + 1 + 55)점입니다.

## 그리워하는 사람의 이름을 담은 문자열 배열 name, 각 사람별 그리움 점수를 담은 정수 배열 yearning, 
## 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열 photo가 매개변수로 주어질 때, 
## 사진들의 추억 점수를 photo에 주어진 순서대로 배열에 담아 return하는 solution 함수를 완성해주세요.

def solution(name, yearning, photo):
    answer = []
    for people in photo:
        for idx in range(len(people)):
            if people[idx] in name:
                people[idx] = yearning[name.index(people[idx])]
            else:
                people[idx] = 0
        answer.append(sum(people))

    return answer


# simple
def solution(name, yearning, photo):
    return [sum(yearning[name.index(j)] for j in i if j in name) for i in photo]



## 명예의 전당 (1)        (+1)
## 문제 설명
## "명예의 전당"이라는 TV 프로그램에서는 매일 1명의 가수가 노래를 부르고, 시청자들의 문자 투표수로 가수에게 점수를 부여합니다. 
## 매일 출연한 가수의 점수가 지금까지 출연 가수들의 점수 중 상위 k번째 이내이면 해당 가수의 점수를 명예의 전당이라는 목록에 올려 기념합니다. 
## 즉 프로그램 시작 이후 초기에 k일까지는 모든 출연 가수의 점수가 명예의 전당에 오르게 됩니다. 
## k일 다음부터는 출연 가수의 점수가 기존의 명예의 전당 목록의 k번째 순위의 가수 점수보다 더 높으면, 
## 출연 가수의 점수가 명예의 전당에 오르게 되고 기존의 k번째 순위의 점수는 명예의 전당에서 내려오게 됩니다.

## 이 프로그램에서는 매일 "명예의 전당"의 최하위 점수를 발표합니다. 
## 예를 들어, k = 3이고, 7일 동안 진행된 가수의 점수가 [10, 100, 20, 150, 1, 100, 200]이라면, 명예의 전당에서 발표된 점수는 
## 아래의 그림과 같이 [10, 10, 10, 20, 20, 100, 100]입니다.

## 명예의 전당 목록의 점수의 개수 k, 1일부터 마지막 날까지 출연한 가수들의 점수인 score가 주어졌을 때, 
## 매일 발표된 명예의 전당의 최하위 점수를 return하는 solution 함수를 완성해주세요.

def solution(k, score):
    answer, honor = [], []

    for i in score:
        if (len(honor) < k):
            honor.append(i)
        else:
            if (i > min(honor)):
                honor.remove(min(honor))
                honor.append(i)
                
        honor.sort()
        answer.append(honor[0])
        
    return answer



## 카드 뭉치      (+2)
## 문제 설명
## 코니는 영어 단어가 적힌 카드 뭉치 두 개를 선물로 받았습니다. 
## 코니는 다음과 같은 규칙으로 카드에 적힌 단어들을 사용해 원하는 순서의 단어 배열을 만들 수 있는지 알고 싶습니다.

## 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용합니다.
## 한 번 사용한 카드는 다시 사용할 수 없습니다.
## 카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다.
## 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없습니다.
## 예를 들어 첫 번째 카드 뭉치에 순서대로 ["i", "drink", "water"], 
## 두 번째 카드 뭉치에 순서대로 ["want", "to"]가 적혀있을 때 ["i", "want", "to", "drink", "water"] 순서의 단어 배열을 만들려고 한다면 
## 첫 번째 카드 뭉치에서 "i"를 사용한 후 두 번째 카드 뭉치에서 "want"와 "to"를 사용하고 
## 첫 번째 카드뭉치에 "drink"와 "water"를 차례대로 사용하면 원하는 순서의 단어 배열을 만들 수 있습니다.

## 문자열로 이루어진 배열 cards1, cards2와 원하는 단어 배열 goal이 매개변수로 주어질 때, 
## cards1과 cards2에 적힌 단어들로 goal를 만들 있다면 "Yes"를, 만들 수 없다면 "No"를 return하는 solution 함수를 완성해주세요.


# first try
def solution(cards1, cards2, goal):
    for idx in range(len(cards1)):
        combo = cards1[:idx] + cards2 + cards1[idx:]
        if combo == goal:
            return "Yes"
        else:   continue
    return "No"

# 프로그래머스에서 제안한 테스트 3가지에선 잘 통과했었는데, 막상 제출하니 56점이 나왔다..
# 아마 앞 뒤로 dummy word 가 들어왔을 경우, 이를 처리하지 못해서 발생한 일인 것 같다.

# 그래서 queue 접근 방식으로, 일일이 비교해보며 하나하나씩 pop해서 접근하는 방법을 사용해보았다.
def solution(cards1, cards2, goal):
    for i in goal:
        if cards1 and i == cards1[0]:
            cards1.pop(0)
        elif cards2 and i == cards2[0]:
            cards2.pop(0)
        else:
            return 'No'
    return 'Yes'