import os
isFinished = False
b_win = 0
w_win = 0
turn = 0
omok = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']]

def reset_board():
    for x in range(15):
        for y in range(15):
            omok[x][y] = '0'
    global turn
    turn = 1
def print_board():#보드 출력
    os.system('cls')
    for x in range(15):
        for y in range(15):
            print(omok[x][y],'',end='')
        print('')
def judge_win(po,la,di,score,color):#승리판단 관리
    if ( di == 5 ) : return 0
    p = judge_win_left(po,la,di,score,color)+judge_win_right(po,la,di,score,color) - 1 
    if( p >= 5 ) :
        global b_win
        global isFinished
        b_win += 1
        temp = ''
        if color == 1:
            temp = '검은색'
        else:
            temp = '흰색'
        temp += ' 승리 다시 한번더? Y or N '
        asw = input(temp)
        if asw == 'Y':
            reset_board()
            return 0
        else :
            isFinished = True
            return 0
    else :
        judge_win(po,la,di+1,score,color)
        return 0
def judge_win_right(po,la,di,score,color):#승리 판단 오른쪽
    if color == 1 :
        Var = 'B'
    else :
        Var = 'W'
    if di ==  1 :


        if la == 15 or la < 0 and po == 15 or po < 0 :
            return score
        elif omok[po][la] == Var :
            score += judge_win_right(po, la+1, di, 1,color)
            return score
        else :
            return score
    if di == 2 :

        if la == 15 or la < 0 and po == 15 or po < 0 :
            return score
        elif omok[po][la] == Var :
            score += judge_win_right(po+1, la+1, di ,1, color)
            return score
        else :
            return score
    if di == 3 :

        if la == 15 or la < 0 and po == 15 or po < 0 :
            return score
        elif omok[po][la] == Var :
            score += judge_win_right(po+1, la, di, 1, color)
            return score
        else :
            return score 
        
    if di == 4 :

        if la == 15 or la < 0 and po == 15 or po < 0 :
            return score
        elif omok[po][la] == Var:
            score += judge_win(po-1,la+1,di,1, color)
            return score
        else :
            return score
def judge_win_left(po,la,di,score,color):#승리판단 왼쪽
    if color == 1 :
        Var = 'B'
    else :
        Var = 'W'
    if di == 1 :

        if la == 15 or la < 0 and po == 15 or po < 0 :
            return score
        elif omok[po][la] == Var :
            score += judge_win_left(po,la-1,di,1, color)
            return score
        else :
            return score
    if di == 2 :

        if la == 15 or la < 0 and po == 15 or po < 0 :
            return score
        elif omok[po][la] == Var :
            score += judge_win_left(po-1,la-1,di,1, color)
            return score
        else :
            return score
    if di == 3 :

        if la == 15 or la < 0 and po == 15 or po < 0 :
            return score
        elif omok[po][la] == Var :
            score += judge_win_left(po-1,la,di,1, color)
            return score
        else :
            return score
    if di == 4 :

        if la == 15 or la < 0 and po == 15 or po < 0 :
            return score
        elif omok[po][la] == Var :
            score += judge_win_left(po+1,la-1,di,1,color)
            return score
        else :
            return score
        

while isFinished == False:#수를 받음
    print_board()
    if( turn % 2 == 0 ):
        po = int(input('검은색돌의 세로줄을 입력하세요'))
        la = int(input('검은색돌의 가로줄을 입력하세요'))
        if( po >= 15 or po < 0 ):continue
        if( la >= 15 or la < 0 ):continue 
        if( omok[po][la] == '0' ):
            omok[po][la] = 'B'
        else : continue
        judge_win(po,la,1,0,1)
        
        
    else :
        po = int(input('흰색돌의 세로줄을 입력하세요'))
        la = int(input('흰색돌의 가로줄을 입력하세요'))
        if( po >= 15 or po < 0 ):continue
        if( la >= 15 or la < 0 ):continue 
        if( omok[po][la] == '0' ):
            omok[po][la] = 'W'
        else : continue
        judge_win(po,la,1,0,2)
    turn += 1 
    
print('검은색 승리 횟수 :',b_win,'흰색 승리 횟수 :',w_win)
print('프로그램을 종료합니다')
