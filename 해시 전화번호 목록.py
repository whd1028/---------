# 문제 설명
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.

# 입출력 예제
# phone_book	                        return
# ["119", "97674223", "1195524421"]	    false
# ["123","456","789"]	                true
# ["12","123","1235","567","88"]	    false

# 입출력 예 설명
# 입출력 예 #1
# 앞에서 설명한 예와 같습니다.

# 입출력 예 #2
# 한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

# 입출력 예 #3
# 첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.

from ast import pattern


def test():
    assert solution6(["119", "97674223", "1195524421"]) == False
    assert solution6(["123","456","789"]) == True
    assert solution6(["12","123","1235","567","88"]) == False


def solution1(phone_book):  # 효율성 실패 91점
    import re
    for i in phone_book:
        check = phone_book[:]
        check.remove(i)
        for j in check:
            result = re.match(i,j)
            if result:
                return False

    return True
# 채점 결과
# 정확성: 83.3
# 효율성: 8.3
# 합계: 91.7 / 100.0

def solution2(phone_book): 
    for i in phone_book:
        check = phone_book[:]
        check.remove(i)
        for j in check:
            if i in j:
                return False

    return True
# 채점 결과
# 정확성: 66.7
# 효율성: 8.3
# 합계: 75.0 / 100.0

def solution3(phone_book):
    new_book = sorted(phone_book)
    for i, v in enumerate(new_book):
        check = new_book[i:]
        for j in check:
            ...

def solution4(phone_book):
    import re
    while phone_book:
        patt = phone_book.pop(0)
        for i in phone_book:
            if len(patt) > len(i):
                continue
            if re.match(patt, i):
                return False
    return True
# 채점 결과
# 정확성: 70.8
# 효율성: 8.3
# 합계: 79.2 / 100.0
            
def solution5(phone_book):
    phone_book = sorted(phone_book,key=lambda x: len(x))
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            if phone_book[i] in phone_book[j]:
                return False
    else:
        return True
# 정확성: 66.7
# 효율성: 8.3
# 합계: 75.0 / 100.0

def solution6(phone_book):
    phones = "," + ",".join(phone_book)
    for number in phone_book:
        cnt = phones.count("," + number)
        if cnt >= 2:
            return False
    return True

def solution7(phoneBook): # 통과
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

def solution8(p):  # 통과
    p.sort()
    for i in range(len(p)-1): 
        if p[i] == (p[i+1])[:len(p[i])] : 
            return False

    return True

test()

