# 문제 설명
# 정수 n이 매개변수로 주어집니다. 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 
# 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

# 1
# 2 | 9 |
# 3 | 10| 8 |
# 4 | 5 | 6 | 7


# 1
# ...
# n | n+1 | n+2 | ... | n+(n-1)

# 제한사항
# n은 1 이상 1,000 이하입니다.
# 입출력 예
# n	result
# 4	[1,2,9,3,10,8,4,5,6,7]
# 5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
# 6	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]

def test():
    assert solution4(4) == [1,2,9,3,10,8,4,5,6,7]
    assert solution4(5) == [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
    assert solution4(6) == [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]

def solution1(n):  # 시간초과 ㄷㄷ
    limit = (n*(n+1)//2)
    num = {i+1:() for i in range(limit)}
    k = 0
    row, col = 0, 0
    while k <= limit:
        for _ in range(n):
            row += 1
            k += 1
            num[k] = (row,col)
        n -= 1

        for _ in range(n):
            col += 1
            k += 1
            num[k] = (row,col)
        n -= 1

        for _ in range(n):
            col -= 1
            row -= 1
            k += 1
            num[k] = (row,col)
        n -= 1

    return sorted(num,key=lambda x: num[x])

def solution2(n):
    limit = (n*(n+1)//2)
    num = [[0]*(i+1) for i in range(n)]
    k = 1
    row, col = 0, 0
    while k <= limit:
        for m in range(n):
            num[row+m][col] = k+m
        k += m+1
        row += m
        col += 1
        n -= 1
        if k > limit:
            break

        for m in range(n):
            num[row][col+m] = k+m
        k += m+1
        row -= 1
        col += m-1
        n -= 1
        if k> limit:
            break

        for m in range(n):
            num[row-m][col-m] = k+m
        k += m+1
        row -= m-1
        col -= m
        n -= 1
        if k > limit:
            break
        
    answer = sum(num,[])
    return answer

def solution3(n):
    row, col, cnt = -1, 0, 1
    board = [[None] * i for i in range(1, n+1)]
    for i in range(n):
        for _ in range(n-i):
            if i % 3 == 0:
                row += 1
            elif i % 3 == 1:
                col += 1
            else:
                row -= 1
                col -= 1
            board[row][col] = cnt
            cnt += 1
    return sum(board,[])

def solution4(n):
    row, col, cnt = -1, 0, 1
    num = [[None]*(i+1) for i in range(n)]
    for i in range(n):
        way = i % 3
        if way == 0:
            for _ in range(n-i):
                row += 1
                num[row][col] = cnt
                cnt += 1
        elif way == 1:
            for _ in range(n-i):
                col += 1
                num[row][col] = cnt
                cnt += 1
        else:
            for _ in range(n-i):
                row -= 1
                col -= 1
                num[row][col] = cnt
                cnt += 1

    return sum(num,[])

test()