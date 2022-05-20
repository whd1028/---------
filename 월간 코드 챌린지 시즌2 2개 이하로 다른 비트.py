# 문제 설명
# 양의 정수 x에 대한 함수 f(x)를 다음과 같이 정의합니다.

# x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수
# 예를 들어,

# f(2) = 3 입니다. 다음 표와 같이 2보다 큰 수들 중에서 비트가 다른 지점이 2개 이하이면서 제일 작은 수가 3이기 때문입니다.
# 수	비트	    다른 비트의 개수
# 2	    000...0010	
# 3	    000...0011	1

# f(7) = 11 입니다. 
# 다음 표와 같이 7보다 큰 수들 중에서 비트가 다른 지점이 2개 이하이면서 제일 작은 수가 11이기 때문입니다.
# 수	비트	        다른 비트의 개수
# 7	    000...0111	    
# 8	    000...1000	    4
# 9	    000...1001	    3
# 10	000...1010	    3
# 11	000...1011	    2

# 정수들이 담긴 배열 numbers가 매개변수로 주어집니다. 
# numbers의 모든 수들에 대하여 각 수의 f 값을 배열에 차례대로 담아 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ numbers의 길이 ≤ 100,000
# 0 ≤ numbers의 모든 수 ≤ 1015

# 입출력 예
# numbers	result
# [2,7]	    [3,11]

def test():
    assert solution2([2,7]) == [3,11]

import itertools
def solution1(numbers):  #10,11번 문제 시간초과
    answer = []
    f = {}
    for i in numbers:
        if i in f:
            answer.append(f[i])
            continue
        for j in itertools.count(i+1):
            if f"{(j^i):b}".count("1") <= 2:
                break
        f[i] = j
        answer.append(j)

    return answer
# 채점 결과
# 정확성: 81.8
# 합계: 81.8 / 100.0

def solution2(numbers: list):
    answer = []
    for i in numbers:
        new_num: str = f"{(i):b}"
        if new_num[-1] == '0':
            answer.append(int(new_num,base=2)+1)
            continue
        if not(new_num.count('0')):
            new_num = '0' + new_num
        new_num = new_num[::-1].replace("10","01",1)[::-1]
        answer.append(int(new_num,base=2))
    return answer

def solution3(numbers):  # 이해 못 했음
    answer = []
    for val in numbers:
        answer.append(((val ^ (val+1)) >> 2) +val +1)

    return answer

test()
# int(f"{2:b}",base=2)
# f"{2:05b} xor {4:05b} = {2^4:b}"
# f"{2^3:05b}"
# (2^3).bit_count()
"01011101011".rfind("01")
"01011101011"[::-1].replace("10","01",1)[::-1]
f"{12 = :010b}"
val = -1
f"{val = :010b}"
f"{val^(val+1) = :010b}"
f"{((val^(val+1))>>2) = :010b}"
f"{((val^(val+1))>>2)+val+1 = :010b}"