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
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']]
def print_board():#보드 출력
    for x in range(15):
        for y in range(15):
            print(omok[x][y],'',end='')
        print('')
def depend_turn(turn):#흰돌 검돌 판단후 함수 작동
    if turn % 2 == 0 :
        a = 1
    else : a = 2
    return a
def judge_win(po,la,di,score):#승리판단 관리
    p=judge_win_left(po,la,di,score)+judge_win_right(po,la,di,score)
    if( p >= 5 ) : return
    else :
        judge_win(po,la,di+1,score)
        return 
def judge_win_right(po,la,di,score):#승리 판단 오른쪽 
    if di ==  1 :

        if la == 15 or la < 0 and po == 15 or po < 0 :
            return score
        elif omok[po][la] == 1 :
            score += judge_win_right(po, la+1, di, 1)
            return score
        else :
            return score
    if di == 2 :

        if la == 15 or la < 0 and po == 15 or po < 0 :
            return score
        elif omok[po][la] == 1 :
            score += judge_win_right(po+1, la+1, di ,1)
            return score
        else :
            return score
    if di == 3 :

        if la == 15 or la < 0 and po == 15 or po < 0 :
            return score
        elif omok[po][la] == 1 :
            score += judge_win_right(po+1, la, di, 1)
            return score
        else :
            return score 
        
    if di == 4 :

        if la == 15 or la < 0 and po == 15 or po < 0 :
            return score
        elif omok[po][la] == 1:
            score += judge_win(po-1,la+1,di,1)
            return score
        else :
            return score
def judge_win_left(po,la,di,score):#승리판단 왼쪽
    if di == 1 :

        if la == 15 or la < 0 and po == 15 or po < 0 :
            return score
        elif omok[po][la] == 1 :
            score += judge_win_left(po,la-1,di,1)
            return score
        else :
            return score
    if di == 2 :

        if la == 15 or la < 0 and po == 15 or po < 0 :
            return score
        elif omok[po][la] == 1 :
            score += judge_win_left(po-1,la-1,di,1)
            return score
        else :
            return score
    if di == 3 :

        if la == 15 or la < 0 and po == 15 or po < 0 :
            return score
        elif omok[po][la] == 1 :
            score += judge_win_left(po-1,la,di,1)
            return score
        else :
            return score
    if di == 4 :

        if la == 15 or la < 0 and po == 15 or po < 0 :
            return score
        elif omok[po][la] == 1:
            score += judge_win_left(po+1,la-1,di,1)
            return score
        else :
            return score
        
turn = 0;
print_board()
while True:#수를 받음 
    if( turn % 2 == 0 ):
        po = int(input('검은색돌의 세로줄을 입력하세요'))
        la = int(input('검은색돌의 가로줄을 입력하세요'))
        if( po >= 15 or po < 0 ):continue
        if( la >= 15 or po < 0 ):continue 
        if( omok[po][la] == '0' ):
            omok[po][la] = 1
        else : continue
        judge_win(po,la,1,0)
        
    if( turn % 2 == 1 ):
        po = int(input('white turn po'))
        la = int(input('white turn la'))
        if( po >= 15 or po < 0 ):continue
        if( la >= 15 or po < 0 ):continue 
        if( omok[po][la] == '0' ):
            omok[po][la] = 2
        else : continue
    turn += 1
    print_board()
