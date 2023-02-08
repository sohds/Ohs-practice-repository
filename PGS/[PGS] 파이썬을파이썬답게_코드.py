## 프로그래머스 무료강의 <파이썬을 파이썬답게>

# 수강 전에 이 문제를 풀어보세요.
# 정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. 
# mylist에 들은 각 원소의 길이를 담은 리스트를 리턴하도록 solution 함수를 작성해주세요.
def solution(mylist):
    return [ len(mylist[i]) for i in range(0, len(mylist)) ]

# iterable: 자신의 멤버를 한 번에 하나씩 리턴할 수 있는 객체입니다. list, str, tuple, dict 등이 여기에 속합니다.
# sequence: int 타입 인덱스를 통해, 원소에 접근할 수 있는 iterable 입니다. iterable의 하위 카테고리라고 생각하시면 됩니다. 
# list, str, tuple이 여기 속합니다. ( dictionary는 다양한 타입을 통해 원소에 접근할 수 있기 때문에 sequence에 속하지 않습니다.

# unpacking: packing은 여러개의 객체를 하나의 객체로 합쳐주었습니다. unpacking은 여러개의 객체를 포함하고 있는 하나의 객체를 풀어줍니다.
# 함수에서 unpacking을 할때는, 매개변수에서 *을 붙이는게 아니라 인자 앞에 *을 붙여서 사용합니다.
# 동일하게 위치인자를 unpacking 하는 경우는 *를, 키워드인자를 unpacking하는 경우 **를 사용합니다.



# 몫과 나머지
# 문제 설명 : 숫자 a, b가 주어졌을 때 a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력해보세요.
# 입력 설명 : 입력으로는 공백으로 구분된 숫자가 두 개 주어집니다. 첫 번째 숫자는 a를 나타내며, 두 번째 숫자는 b를 나타냅니다.
# 출력 설명 : a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력하세요.

# my ver.
a, b = map(int, input().strip().split(' '))
tp = divmod(a, b)
print(tp[0], tp[1])

# what programmers wants
a = 7
b = 5
print(*divmod(a, b))

# 무조건 divmod를 사용하는 게 좋은 방법은 아님
# 가독성이나, 팀의 코드 스타일에 따라서, a//b, a%b와 같이 쓸 때가 더 좋을 수도 있음
# 또한, divmod는 작은 숫자를 다룰 때는 a//b, a%b 보다 느림 
# 대신, 큰 숫자를 다룰 때는 전자가 후자보다 더 빠름



# n진법으로 표기된 string을 10진법 숫자로 변환하기
# 문제 설명 : base 진법으로 표기된 숫자를 10진법 숫자 출력해보세요.
# 입력 설명 : 입력으로는 공백으로 구분된 숫자가 두 개 주어집니다. 첫 번째 숫자는 num을 나타내며, 두 번째 숫자는 base를 나타냅니다.
# 출력 설명 : base 진법으로 표기된 num을 10진법 숫자로 출력해보세요.
num, base = map(int, input().strip().split(' '))
print(int(str(num), base))



# 문자열 정렬하기
# 문제 설명 : 문자열 s와 자연수 n이 입력으로 주어집니다. 문자열 s를 좌측 / 가운데 / 우측 정렬한 길이 n인 문자열을 한 줄씩 프린트해보세요.
# 제한조건: s의 길이는 n보다 작습니다. (n - s의 길이)는 짝수입니다. s는 알파벳과 숫자로만 이루어져 있으며, 공백 문자가 포함되어있지 않습니다.

# my ver.
# f 문자열 포매팅
s, n = input().strip().split(' ')
left = f'{s:<{n}}'
middle = f'{s:^{n}}'
right = f'{s:>{n}}'
print(left)
print(middle)
print(right)

# what programmmers wants
# 파이썬에서는 ljust, center, rjust와 같은 string의 메소드를 사용해 코드를 획기적으로 줄일 수 있습니다.
s = '가나다라'
n = 7
s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬



# 알파벳 출력하기
# 문제 설명 : 입력으로 0이 주어지면 영문 소문자 알파벳을, 입력으로 1이 주어지면 영문 대문자 알파벳을 사전 순으로 출력하는 코드를 짜세요.

# my ver.
num = int(input().strip())
if num == 0:
    print('abcdefghijklmnopqrstuvwxyz')
else:
    print('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
# what programmers wants

# import string 
# string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
# string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.digits # 숫자 0123456789

import string
num = int(input().strip())
if num is 1:
    print(string.ascii_uppercase)
elif num is 0:
    print(string.ascii_lowercase)
    
    

# 원본을 유지한채, 정렬된 리스트 구하기 - sorted
# 파이썬의 sort() 함수를 사용하면 리스트의 원소를 정렬할 수 있습니다. 이때, sort 함수는 원본의 멤버 순서를 변경하지요.
# 따라서 원본의 순서는 변경하지 않고, 정렬된 값을 구하려면 sorted() 함수를 써야합니다.

# 2차원 리스트 뒤집기
# 문제 설명 : 다음을 만족하는 함수, solution을 완성해주세요.
# solution 함수는 이차원 리스트, mylist를 인자로 받습니다
# solution 함수는 mylist 원소의 행과 열을 뒤집은 한 값을 리턴해야합니다.
# 예를 들어 mylist [[1, 2, 3], [4, 5, 6], [7, 8, 9]]가 주어진 경우, solution 함수는 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 리턴하면 됩니다.
def solution(mylist):
    return list(map(list, zip(*mylist)))


# i번째 원소와 i+1번째 원소
# 문제 설명 : 숫자를 담은 리스트 mylist가 solution 함수의 파라미터로 주어집니다. 
# solution 함수가 mylist의 i번째 원소와 i+1번째 원소의 차를 담은 일차원 리스트에 차례로 담아 리턴하도록 코드를 작성해주세요.
# 단, 마지막에 있는 원소는 (마지막+1)번째의 원소와의 차를 구할 수 없으니, 이 값은 구하지 않습니다.
# 제한 조건 : mylist의 길이는 1 이상 100 이하인 자연수입니다. mylist의 원소는 1 이상 100 이하인 자연수입니다.

# my ver.
def solution(mylist):
    return [ abs(mylist[i]-mylist[i+1]) for i in range(0, len(mylist)-1) ]

# what programmers wants
def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]    
    print(solution(mylist))
    


# 모든 멤버의 type 변환하기
# 문제 설명 : 문자열 리스트 mylist를 입력받아, 이 리스트를 정수형 리스트로 바꾼 값을 리턴하는 함수, solution을 만들어주세요. 
# 예를 들어 mylist가 ['1', '100', '33'] 인 경우, solution 함수는 [1, 100, 33] 을 리턴하면 됩니다.
# 제한조건 : mylist의 길이는 100 이하인 자연수입니다. mylist의 원소는 10진수 숫자로 표현할 수 있는 문자열입니다. 
# 즉, 'as2' 와 같은 문자열은 들어있지 않습니다.

# my ver.
def solution(mylist):
    return [ int(i) for i in mylist ]

# what programmers wants
list1 = ['1', '100', '33']
list2 = list(map(int, list1))



# map 함수 응용하기
# 문제 설명 : 정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. 
# solution 함수가 mylist 각 원소의 길이를 담은 리스트를 리턴하도록 빈칸을 완성해보세요.
# hint) 이전 강의에서 배운 map 함수를 활용해보세요
# 제한 조건 : mylist의 길이는 100 이하인 자연수입니다. mylist 각 원소의 길이는 100 이하인 자연수입니다.
def solution(mylist):
    answer = list(map(len, mylist))
    return answer



# sequence 멤버를 하나로 이어붙이기
# 문제 설명 : 문자열 리스트 mylist를 입력받아, 이 리스트의 원소를 모두 이어붙인 문자열을 리턴하는 함수, solution을 만들어주세요. 
# 예를 들어 mylist가 ['1', '100', '33'] 인 경우, solution 함수는 '110033'을 리턴하면 됩니다.
def solution(mylist):
    return ''.join(mylist)



# 삼각형 별찍기
# 문제 설명 : 이 문제에는 표준 입력으로 정수 n이 주어집니다. 별(*) 문자를 이용해 높이가 n인 삼각형을 출력해보세요.
# 제한 조건 : n은 100 이하인 자연수입니다.
n = int(input().strip())
for i in range(1, n+1):
    print('*'*i)
    
    

# 파이썬에서는 itertools.product를 이용하면, for 문을 사용하지 않고도 곱집합을 구할 수 있습니다.
# 두 스트링 'ABCD', 'xy' 의 곱집합은 Ax Ay Bx By Cx Cy Dx Dy 입니다.
import itertools
iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3))) 



# 2차원 리스트를 1차원 리스트로 만들기
# 문제 설명 : 문자열을 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. 
# solution 함수가 mylist를 일차원 리스트로 만들어 리턴하도록 코드를 작성해주세요.
# 제한 조건 : arr의 길이는 1 이상 100 이하인 자연수입니다. arr 원소의 길이는 5를 넘지 않습니다.

# my ver.
import numpy as np
def solution(mylist):
    return np.concatenate(mylist).tolist()

# what programmers wants
my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))

# 방법 7 - numpy 라이브러리의 flatten 이용 (제한적인 방법, 각 원소의 길이가 동일한 경우에만 가능)
import numpy as np
np.array(my_list).flatten().tolist()



# 순열과 조합
# 문제 설명 : 숫자를 담은 일차원 리스트, mylist에 대해 mylist의 원소로 이루어진 모든 순열을 사전순으로 리턴하는 함수 solution을 완성해주세요.
# 제한 조건 : ylist 의 길이는 1 이상 100 이하인 자연수입니다.

# my ver.
from itertools import permutations

def solution(mylist):
    answer = list(permutations(mylist, len(mylist)))
    answer.sort()
    return answer

# what programmers wants
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 순열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 순열 만들기



# 가장 많이 등장하는 알파벳 찾기
# 문제 설명 : 이 문제에는 표준 입력으로 문자열, mystr이 주어집니다. 
# mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성해주세요.
# 제한 조건 : mystr의 원소는 알파벳 소문자로만 주어집니다. mystr의 길이는 1 이상 100 이하입니다.

# my ver.
my_str = input().strip()

from collections import Counter
count_alphabet = dict(Counter(my_str))
max_value = max(count_alphabet.values())
max_alphabet = ''
for i in count_alphabet:
    if count_alphabet[i] == max_value:
        max_alphabet += i
answer = ''.join(sorted(max_alphabet))
print(answer)

# other ver.
from collections import Counter
my_str = input().strip()
max_count = max(Counter(my_str).values())
print(''.join(sorted([k for k,v in Counter(my_str).items() if v == max_count])))



# what programmers wants
# 파이썬의 collections.Counter 클래스를 사용하면 이 코드를 간략하게 만들 수 있습니다.

import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0



# for 문과 if문을 한번에
# 문제 설명 : 정수를 담은 리스트 mylist를 입력받아, 이 리스트의 원소 중 짝수인 값만을 제곱해 담은 새 리스트를 리턴하는 solution함수를 완성해주세요. 
# 예를 들어, [3, 2, 6, 7]이 주어진 경우 3은 홀수이므로 무시합니다. 2는 짝수이므로 제곱합니다.
# 6은 짝수이므로 제곱합니다. 7은 홀수이므로 무시합니다.
# 따라서 2의 제곱과 6의 제곱을 담은 리스트인 [4, 36]을 리턴해야합니다.
# 제한 조건 : mylist는 길이가 100이하인 배열입니다. mylist의 원소는 1이상 100 이하인 정수입니다.
def solution(mylist):
    return [ i**2 for i in mylist if i%2==0 ]