# 문제 설명
# 1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다. 
# 표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요. 
# (단, 정사각형이란 축에 평행한 정사각형을 말합니다.)

# 예를 들어
# 1	2 3	4
# 0	1 1	1
# 1	1 1	1
# 1	1 1	1
# 0	0 1	0
# 가 있다면 가장 큰 정사각형은

# 1	2 3	4
# 0	1 1	1
# 1	1 1	1
# 1	1 1	1
# 0	0 1	0
# 가 되며 넓이는 9가 되므로 9를 반환해 주면 됩니다.

# 제한사항
# 표(board)는 2차원 배열로 주어집니다.
# 표(board)의 행(row)의 크기 : 1,000 이하의 자연수
# 표(board)의 열(column)의 크기 : 1,000 이하의 자연수
# 표(board)의 값은 1또는 0으로만 이루어져 있습니다.

# 입출력 예
# board	                                        answer
# [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]	    9
# [[0,0,1,1],[1,1,1,1]]	                        4

# 입출력 예 설명
# 입출력 예 #1
# 위의 예시와 같습니다.

# 입출력 예 #2
# | 0 | 0 | 1 | 1 |
# | 1 | 1 | 1 | 1 |
# 로 가장 큰 정사각형의 넓이는 4가 되므로 4를 return합니다.



def test():
    assert solution4([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]) == 9
    assert solution4([[0,0,1,1],[1,1,1,1]]) == 4

def solution1(board):
    answer = 0
    check_line = [0]*len(board[0])
    for row in board:
        check_line = [a*b+b for a,b in zip(check_line,row)]
        if f"{answer+1}"*(answer+1) in str.join('',[str(i) for i in check_line]):
            answer += 1
            
    return answer*answer
    # 정확성: 37.7
    # 효율성: 13.5
    # 합계: 51.1 / 100.0

def solution2(board):  # 변수 이름이 맘에 안들어서 솔루션3에서 다시함
    answer = 0
    row_size = len(board[0])
    check_col = [0]*row_size
    for row in board:
        check_col = [a*b+b for a,b in zip(check_col,row)]
        col_min = min(check_col)
        if col_min > answer:
            check_row = 0
            for v in check_col:
                if v < col_min:
                    check_row = 0
                    continue
                check_row += 1
                if check_row == col_min:
                    answer = col_min
                    break
    
    return answer**2

def solution3(board):
    answer = 0
    row_size = len(board[0])
    line_check = [0] * row_size
    for row in board:
        hori_min = row_size
        verti_size = 0
        for i in range(row_size):
            line_check[i] = line_check[i]*row[i]+row[i]

            if line_check[i] > 0:
                verti_size += 1
            else:
                verti_size = 0
                hori_min = row_size
                continue


            if line_check[i] < hori_min:
                hori_min = line_check[i]

            if (hori_min >= answer+1) and (verti_size >= answer+1):
                answer += 1
    
    return answer ** 2

def solution4(board):
    answer = 0
    row_size = len(board[0])
    line_check = [0] * row_size
    for row in board:
        # 정사각형의 왼쪽점의 [위치,높이]
        left = [row_size,0]
        # 각 열의 세로선길이 계산
        for i in range(row_size):
            line_check[i] = line_check[i]*row[i]+row[i]
            # 해당하는 열의 세로선이 가장 큰 정사각형의 한변의 길이보다 크다면 실행
            if line_check[i] > answer:
                # 왼쪽점 위치 재설정
                if left[0] > i:
                    left = [i,line_check[i]]
                # 사각형의 높이 재설정
                if left[1] > line_check[i]:
                    left[1] = line_check[i]
                # 가로선확인 후 answer재설정    
                if (i - left[0]+1) > answer:
                    answer = min(i-left[0]+1,line_check[i])
            # 세로선이 끊였다면 사각형의 왼쪽점 초기화
            elif line_check[i] == 0:
                left = [row_size,0]
    
    return answer ** 2
    # 채점 결과
    # 정확성: 37.7
    # 효율성: 40.4
    # 합계: 78.0 / 100.0

# 왼쪽 위 부터 오른쪽 아래 방향으로 탐색하면 무조건 정사각형은 1*1,2*2,3*3,4*4,...순으로 발견한다.
def solution5(board):
    answer = 0
    row_size = len(board[0])
    line_check = [0] * row_size
    for row in board:
        verti_count = 0
        for i in range(row_size):
            line_check[i] = line_check[i]*row[i]+row[i]
            if line_check[i] > answer:
                verti_count += 1
                if verti_count == answer+1:
                    answer += 1
            else:
                verti_count = 0
    
    return answer ** 2
# 채점 결과
# 정확성: 53.3
# 효율성: 40.4
# 합계: 93.7 / 100.0

# test()

import random
import pprint
row = random.randint(5,15)
col = random.randint(5,15)
print(f"{row=}\n{col=}")
test_board = []
for i in range(row):
    test_board.append([random.choice([1,1,0]) for _ in range(col)])
pprint.pprint(test_board)
print(solution5(test_board))
