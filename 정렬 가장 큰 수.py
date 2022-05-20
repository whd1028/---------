# 문제 설명
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

# 입출력 예
# numbers	            return
# [6, 10, 2]	        "6210"
# [3, 30, 34, 5, 9]	    "9534330"

def test():
    assert solution7([0,0,0,0]) == "0"
    assert solution7([6, 10, 2]) == "6210"
    assert solution7([3, 30, 34, 5, 9]) == "9534330"
    assert solution7([3, 30, 33, 4, 5, 9]) == "95433330"
    assert solution7([3, 30, 300, 34, 5, 9]) == "9534330300"
    assert solution7([3, 30, 35, 5, 9]) == "9535330"
    assert solution7([3, 33, 30, 35, 5, 9]) == "953533330"
    assert solution7([101, 10, 232, 23]) == "2323210110"
    assert solution7([1, 2, 20, 21, 22, 23, 3, 30]) == "3302322221201"
    

from itertools import permutations

def solution1(numbers):
    new_number = []
    for i in permutations(numbers, len(numbers)):
        new_number.append(''.join(map(str,i)))

    return max(new_number)
# 시간초과 많음

import heapq as hq
def solution2(numbers):
    new_numbers = []
    for i in numbers:
        hq.heappush(new_numbers,str(i))

    ...

def solution3(numbers):
    new_numbers = sorted(map(str,numbers), reverse=True, key= lambda x: str(x).ljust(5,str(x)[0]))
    return ''.join(new_numbers)

def solution4(numbers):
    new_numbers = list(map(str,numbers))
    new_numbers = sorted(new_numbers, reverse=True, key= lambda x: x.ljust(5,x[-1]))
    return str(int(''.join(new_numbers)))

def solution5(numbers):
    new_numbers = sorted(numbers,reverse=True, key= lambda x: x/(10**len(str(x))))
    new_numbers = list(map(str,new_numbers))
    return ''.join(new_numbers)

def solution6(numbers):
    new_numbers = sorted(numbers,reverse=True, key= lambda x:x[0])

import functools
def solution7(numbers):
    def mycmp(x: int, y: int) -> int:
        return int(str(x)+str(y)) - int(str(y)+str(x))

    numbers = sorted(numbers,reverse=True,key=functools.cmp_to_key(mycmp))
    return int(str.join('',map(str,numbers)))

def solution8(numbers):  # ????????????????????????????? 누가 설명좀.....
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
    # >>> True-False
    # 1
    # >>> True+False
    # 1
    # >>> False-True
    # -1
    # >>> False+True
    # 1    

def solution9(numbers): 
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

class Node():
    numbers = []
    result = []
    def __init__(self,depth):
        self.depth = depth
    def bigger():
        ...
    def smaller():
        ...
    def sort():
        ...

# test()
def tt(N):
    n = [str(x) for x in N]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    return n
from pprint import pprint
pprint(tt([i for i in range(10000)]))
