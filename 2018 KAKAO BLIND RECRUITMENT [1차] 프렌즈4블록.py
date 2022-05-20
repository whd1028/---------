# 문제 설명
# 프렌즈4블록
# 블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".
# 같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.
# 만약 판이 위와 같이 주어질 경우, 라이언이 2×2로 배치된 7개 블록과 콘이 2×2로 배치된 4개 블록이 지워진다. 
# 같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.
# 블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.
# 만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.

# 위 초기 배치를 문자로 표시하면 아래와 같다.
# TTTANT
# RRFACC
# RRRFCC
# TRRRAA
# TTMMMF
# TMMTTJ

# 각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다
# 입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.

# 입력 형식
# 입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
# 2 ≦ n, m ≦ 30
# board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.

# 출력 형식
# 입력으로 주어진 판 정보를 가지고 몇 개의 블록이 지워질지 출력하라.

# 입출력 예제
# m	    n	board	                                                        answer
# 4	    5	["CCBDE", "AAADE", "AAABF", "CCBBF"]	                        14
# 6	    6	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	15

# 예제에 대한 설명
# 입출력 예제 1의 경우, 첫 번째에는 A 블록 6개가 지워지고, 두 번째에는 B 블록 4개와 C 블록 4개가 지워져, 모두 14개의 블록이 지워진다.
# 입출력 예제 2는 본문 설명에 있는 그림을 옮긴 것이다. 11개와 4개의 블록이 차례로 지워지며, 모두 15개의 블록이 지워진다.

def test():
    assert solution5(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]) == 14
    assert solution5(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]) == 15    

def solution1(m, n, board):  # 파이썬스럽지 못 한듯?(미완성)
    answer = 0
    remove_set = set()
    line_check = set()
    row_limit = len(board)
    col_limit = len(board[0])
    for row_num in range(row_limit):
        for col_num in range(col_limit):
            if board[row_num][col_num] == board[row_num][col_num+1]:
                line_check.add((row_num,col_num,board[row_num][col_num]))
    for row_num,col_num,block in line_check:
        if (row_num+1,col_num,block) in line_check:
            remove_set.add((row_num,col_num))
            remove_set.add((row_num,col_num+1))
            remove_set.add((row_num+1,col_num))
            remove_set.add((row_num+1,col_num+1))
    answer += len(remove_set)
    for row_num, col_num in remove_set:
        board[row_num][col_num] = '0'
        if row_num-1 >= 0:
            board[row_num][col_num] = board[row_num-1][col_num]
            board[row_num-1][col_num] = '0'
    ...
    
def solution2(m,n,board):
    board = list(zip(*board))
    remove_set = set()
    for x in range(n-1):
        for y in range(m-1):
            ...
    for block in zip(*board):
        ...

def solution3(m,n,board):
    answer = 0
    remove_set = set()
    line_check = set()
    for i in range(m):
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                line_check.add((i,j,board[i][j]))
    for i,j,block in line_check:
        if (i+1,j,block) in line_check:
            remove_set.add((i,   j))
            remove_set.add((i+1, j))
            remove_set.add((i,   j+1))
            remove_set.add((i+1, j+1))
    board = list(map(list,board))
    for i,j in remove_set:
        board[i][j] = '0'
    
    ...

def solution4(m,n,board):  # 성공
    answer = 0
    board = list(map(list,zip(*board[::-1])))
    remove_set = set()
    line_check = set()
    while True:
        for i, col in enumerate(board):
            for j, block in enumerate(col[:-1]):
                if board[i][j] == board[i][j+1]:
                    line_check.add((i,j,block))
                    if (i-1,j,block) in line_check:
                        remove_set.add((i,j))
                        remove_set.add((i,j+1))
                        remove_set.add((i-1,j))
                        remove_set.add((i-1,j+1))
        line_check.clear()
            
        if remove_set:
            answer += len(remove_set)
        else:
            break

        for i,j in remove_set:
            board[i][j] = '0'
        for i, col in enumerate(board):
            board[i] = list(str.join('',col).replace('0',''))

        remove_set.clear()

    return answer

def solution5(m,n,board):
    answer = 0
    board = list(map(list,board))
    while True:
        remove_set = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] != '0':
                    remove_set.add((i,j))
                    remove_set.add((i+1,j))
                    remove_set.add((i,j+1))
                    remove_set.add((i+1,j+1))

        if remove_set:
            answer += len(remove_set)
        else:
            break

        for i, j in remove_set:
            board[i][j] = '0'

        for k in range(m-1,0,-1):
            for j in range(n):
                for i in range(k):
                    if board[i+1][j] == '0':
                        board[i+1][j], board[i][j] = board[i][j], '0'

    return answer


test()