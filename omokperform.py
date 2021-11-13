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


def reset_board(): # 다시 시작할시 보드 초기화 
    for x in range(len_board):
        for y in range(len_board):
            omok[x][y] = '0'
    global turn
    turn = 1
    
def print_board():#보드 출력
    os.system('cls')
    print(num_game,'목')
    for x in range(len_board):
        for y in range(len_board):
            if( y == len_board - 1 ) :
                print(omok[x][y],end='')
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
        if la == len_board or la < 0 and po == len_board or po < 0 :
            return score
        elif omok[po][la] == Var :
            score += judge_win_right( po, la+1, di, 1,color)
            return score
        else :
            return score

    if di == 2 :
        if la == len_board or la < 0 and po == len_board or po < 0 :
            return score
        elif omok[po][la] == Var :
            score += judge_win_right( po+1, la+1, di ,1, color)
            return score
        else :
            return score

    if di == 3 :
        if la == len_board or la < 0 and po == len_board or po < 0 :
            return score
        elif omok[po][la] == Var :
            score += judge_win_right( po+1, la, di, 1, color)
            return score
        else :
            return score 
        
    if di == 4 :
        if la == len_board or la < 0 and po == lend_board or po < 0 :
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
        if la == len_board or la < 0 and po == len_board or po < 0 :
            return score
        elif omok[po][la] == Var :
            score += judge_win_left( po, la-1, di, 1, color)
            return score
        else :
            return score
        
    if di == 2 :
        if la == len_board or la < 0 and po == len_board or po < 0 :
            return score
        elif omok[po][la] == Var :
            score += judge_win_left( po-1, la-1, di, 1, color)
            return score
        else :
            return score
        
    if di == 3 :
        if la == len_board or la < 0 and po == len_board or po < 0 :
            return score
        elif omok[po][la] == Var :
            score += judge_win_left( po-1, la, di, 1, color)
            return score
        else :
            return score
        
    if di == 4 :
        if la == len_board or la < 0 and po == len_board or po < 0 :
            return score
        elif omok[po][la] == Var :
            score += judge_win_left( po+1, la-1, di, 1, color)
            return score
        else :
            return score
        
print_board()
while Game_repeat == False:# main 함수 

    if( turn % 2 == 0 ):
        po = int(input('검은색색돌의 세로줄을 입력하세요'))
        la = int(input('검은색돌의 가로줄을 입력하세요'))
        if( po == 829 or la == 829 ):
            print('제작자의 생일을 맞추셨군요 !! 당신의 승리 ')
            judge_win(0,0,1,100,1)
            turn += 1
        if( po == 622 or la == 622 ):
            print('대체 왜 그사람의 생일을 .. 당신의 패배 입니다..')
            judge_win(0,0,1,100,2)
            turn += 1
        if( po >= len_board or po < 0 ):continue
        if( la >= len_board or la < 0 ):continue 
        if( omok[po][la] == '0' ):
            omok[po][la] = 'B'
        else : continue
        judge_win(po,la,1,0,1)
        
        
    else :
        po = int(input('흰색돌의 세로줄을 입력하세요'))
        la = int(input('흰색돌의 가로줄을 입력하세요'))
        if( po == 829 or la == 829 ):
            print('제작자의 생일을 맞추셨군요 !! 당신의 승리 ')
            judge_win(0,0,1,100,2)
            turn += 1
        if( po == 622 or la == 622 ):
            print('대체 왜 그사람의 생일을 .. 당신의 패배 입니다..')
            judge_win(0,0,1,100,1)
            turn += 1
        if( po >= len_board or po < 0 ):continue
        if( la >= len_board or la < 0 ):continue
        
        if( omok[po][la] == '0' ):
            omok[po][la] = 'W'
        else : continue
        judge_win(po,la,1,0,2)

    print_board()    
    turn += 1 


print('검은색 승리 횟수 :',b_win,'흰색 승리 횟수 :',w_win)
print('프로그램을 종료합니다')
