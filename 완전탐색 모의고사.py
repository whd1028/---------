# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5,/ 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5,/ 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,/ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

# 입출력 예
# answers	    return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]

# 입출력 예 설명
# 입출력 예 #1
# 수포자 1은 모든 문제를 맞혔습니다.
# 수포자 2는 모든 문제를 틀렸습니다.
# 수포자 3은 모든 문제를 틀렸습니다.
# 따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

# 입출력 예 #2
# 모든 사람이 2문제씩을 맞췄습니다.

def test():
    assert solution3([1,2,3,4,5]) == [1]
    assert solution3([1,3,2,4,2]) == [1,2,3]

def solution1(answers):
    a,b,c = [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0,0,0]
    
    for i, v in enumerate(answers):
        if a[i%len(a)] == v:
            count[0] += 1
        if b[i%len(b)] == v:
            count[1] += 1
        if c[i%len(c)] == v:
            count[2] += 1

    result = []
    for i, v in enumerate(count):
        if max(count) == v:
            result.append(i+1)

    return result

def solution2(answers):
    from itertools import cycle
    a_cycle = cycle([1, 2, 3, 4, 5])
    b_cycle = cycle([2, 1, 2, 3, 2, 4, 2, 5])
    c_cycle = cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    score = [0,0,0]

    for answer, a, b, c in zip(answers,a_cycle,b_cycle,c_cycle):
        if answer == a:
            score[0] += 1
        if answer == b:
            score[1] += 1
        if answer == c:
            score[2] += 1

    return [i+1 for i, v in enumerate(score) if max(score) == v]

def solution3(answers):  # 미완성
    from itertools import cycle
    patt = [cycle([1, 2, 3, 4, 5]),
            cycle([2, 1, 2, 3, 2, 4, 2, 5]),
            cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])]

    for answer, *pat in zip(answers,*patt):
        
        ...

def solution4(answers):  # 미완성
    patterns = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i, v in enumerate(answers):
        map(lambda x: x[i%len(x)])

test()