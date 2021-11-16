import os
Game_repeat = False #반복시 상태 지정
b_win = 0 # 흑색 흰색 이긴횟수 
w_win = 0
turn = 0 # 흑색 흰색 턴 판단
len_board = 7
num_game = 5
omok = [['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0']]
Eng_Num = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14],
           ['a','b','c','d','e','f','g','h','i','j','k','m','n','o'],
           ['A','B','C','D','E','F','G','H','I','J','K','M','N','O']]


def po_la_input(color):#사용자 입력값 
    if( color == 1 ):
        VAr = '검은'
        stone = 'B'
    else :
        VAr = '흰'
        stone = 'W'
    print(VAr,'색돌의 세로줄을 입력하세요',end='')
    po = input()
    print(VAr,'색돌의 가로줄을 입력하세요',end='')
    la = input()
    for x in range(1,3):
        for y in range(len_board):
            if ( la == Eng_Num[x][y] ):
                la = Eng_Num[0][y]
    for x in range(1,3):
        for y in range(len_board):
            if( po == Eng_Num[x][y] ):
                po = Eng_Num[0][y]
    try:
        int(po)
        po_is = True
    except ValueError:
        po_is = False
    try:
        int(la)
        la_is = True
    except ValueError:
        la_is = False
    if( po_is == True and la_is == True ):
        po = int(po) - 1
        la = int(la) - 1 
        if( po >= len_board or po < 0 or la >= len_board or la < 0 ):
            po_la_input(color)
        else :
            if( omok[po][la] == '0' ):
                omok[po][la] = stone
                judge_win(po,la,1,0,color)
            else :
                po_la_input(color)
        
    else :
        po_la_input(color)
        
    
    
def reset_board(): # 다시 시작할시 보드 초기화 
    for x in range(len_board):
        for y in range(len_board):
            omok[x][y] = '0'
    global turn
    turn = 1
    
def print_board(color):#보드 출력
    os.system('cls')
    if( color % 2 == 0 ) :
        VAR = '검은색'
    else :
        VAR = '흰색'
    print('오목',VAR,'차례')
    print('1 2 3 4 5 6 7')
    for x in range(len_board):
        for y in range(len_board):
            if( y == len_board - 1 ):
                if( omok[x][y] == '0' ):
                    print('  ',end='')
                    print(x+1,end='')
                else :
                    print(omok[x][y],'',end='')
                    print(x+1,end='')
            else:
                if( omok[x][y] == '0' ):
                    print('  ',end='')
                else:
                    print(omok[x][y],'',end='')
        print('')
        
        
        
def judge_win( po, la, di, score, color):#승리 판단 메인함수

    if ( di == 5 ) : return 0
    
    stack = judge_win_left( po, la, di, score, color)+judge_win_right( po, la, di, score, color) - 1
    if( stack >= num_game ) :
        global b_win
        global w_win
        global Game_repeat
        
        if color == 1:
            print_color = '검은색'
            b_win += 1
            
        else:
            print_color = '흰색'
            w_win += 1
            
        print(print_color,'승리 한번더 하시겠습니까 \'Y\'?','',end='')
        asw = input()
        if asw == 'Y':
            reset_board()
            return 0
        
        else :
            Game_repeat = True
            return 0
        
    else :
        judge_win( po, la, di + 1, score, color)
        return 0

    
def judge_win_right( po, la, di, score, color):#승리 판단 오른쪽

    if color == 1 :
        Var = 'B'
        
    else :
        Var = 'W'

    if di ==  1 :
        if ( la == len_board or la < 0 ) or ( po == len_board or po < 0 ) :
            return score
        elif omok[po][la] == Var :
            score += judge_win_right( po, la+1, di, 1,color)
            return score
        else :
            return score

    if di == 2 :
        if ( la == len_board or la < 0 ) or ( po == len_board or po < 0 ) :
            return score
        elif omok[po][la] == Var :
            score += judge_win_right( po+1, la+1, di ,1, color)
            return score
        else :
            return score

    if di == 3 :
        if ( la == len_board or la < 0 ) or ( po == len_board or po < 0 ) :
            return score
        elif omok[po][la] == Var :
            score += judge_win_right( po+1, la, di, 1, color)
            return score
        else :
            return score 
        
    if di == 4 :
        if ( la == len_board or la < 0 ) or ( po == len_board or po < 0 ) :
            return score
        elif omok[po][la] == Var:
            score += judge_win_right( po-1, la+1, di, 1, color)
            return score
        else :
            return score

        
def judge_win_left( po, la, di, score, color):#승리판단 왼쪽

    if color == 1 :
        Var = 'B'
    else :
        Var = 'W'
        
    if di == 1 :
        if ( la == len_board or la < 0 ) or ( po == len_board or po < 0 ) :
            return score
        elif omok[po][la] == Var :
            score += judge_win_left( po, la-1, di, 1, color)
            return score
        else :
            return score
        
    if di == 2 :
        if ( la == len_board or la < 0 ) or ( po == len_board or po < 0 ) :
            return score
        elif omok[po][la] == Var :
            score += judge_win_left( po-1, la-1, di, 1, color)
            return score
        else :
            return score
        
    if di == 3 :
        if ( la == len_board or la < 0 ) or ( po == len_board or po < 0 ) :
            return score
        elif omok[po][la] == Var :
            score += judge_win_left( po-1, la, di, 1, color)
            return score
        else :
            return score
        
    if di == 4 :
        if ( la == len_board or la < 0 ) or ( po == len_board or po < 0 ) :
            return score
        elif omok[po][la] == Var :
            score += judge_win_left( po+1, la-1, di, 1, color)
            return score
        else :
            return score
        
while Game_repeat == False:# main 함수 
    print_board(turn)
    if( turn % 2 == 0 ):
        po_la_input(1)   
    else :
        po_la_input(2)  
    turn += 1 


print('검은색 승리 횟수 :',b_win,'흰색 승리 횟수 :',w_win)
print('프로그램을 종료합니다')
