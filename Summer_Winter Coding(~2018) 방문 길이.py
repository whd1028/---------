# 문제 설명
# 게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.

# U: 위쪽으로 한 칸 가기
# D: 아래쪽으로 한 칸 가기
# R: 오른쪽으로 한 칸 가기
# L: 왼쪽으로 한 칸 가기

# 캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다

# 제한사항
# dirs는 string형으로 주어지며, 'U', 'D', 'R', 'L' 이외에 문자는 주어지지 않습니다.
# dirs의 길이는 500 이하의 자연수입니다.
# 입출력 예
# dirs	        answer
# "ULURRDLLU"	7
# "LULLLLLLU"	7

def test():
    assert solution1("ULURRDLLU") == 7
    assert solution1("LULLLLLLU") == 7

def solution1(dirs):
    posi = [0,0]  # x,y
    his = set()
    move = {'U':[0,+1], 'D':[0,-1], 'R':[1,0], 'L':[-1,0]}
    for i in dirs:
        next = list(map(sum,zip(posi,move[i])))
        if (-6 or 6) in next:
            continue
        his.add(tuple(posi+next))
        posi = next
        
    return len(his)

def solution2(dirs):
    
    ...

test()