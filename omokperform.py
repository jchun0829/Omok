import os
Game_repeat = False #반복시 상태 지정
b_win = 0 # 흑색 흰색 이긴횟수 
w_win = 0
turn = 0 # 흑색 흰색 턴 판단
len_board = 7
num_game = 5
count_y = 0
count_n = 0
omok = [['0']*len_board for i in range(len_board)]
Eng_Num = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14],
           ['a','b','c','d','e','f','g','h','i','j','k','m','n','o'],
           ['A','B','C','D','E','F','G','H','I','J','K','M','N','O']]

def repeat_game():#게임의 반복 여부
    global count_y
    global count_n
    print('한 판 더 하시겠습니까? : ',end='')
    user_re = input()
    if user_re == 'Y' or user_re == 'y' :
        count_y += 1
        return 
    elif user_re == 'N' or user_re == 'n' :
        count_n += 1
        return 
    repeat_game()

def game_ready():#게임이 시작시 오목판 초기화 
    global len_board
    global omok
    print('오목판의 크기를 정해주세요. ( 7 ~ 9 ) : ',end='')
    len_board = input()
    try:
        int(len_board)
        lenboard_is = True
    except ValueError:
        lenboard_is = False
    if lenboard_is == True :
        len_board = int(len_board)
        if len_board >= 7 and len_board <= 9 :
            omok = [['0']*len_board for i in range(len_board)]
            return
        else :
            print('범위에 맞는 숫자를 입력해주세요. ( 7 ~ 9 ) ')
            game_ready()
    else :
        print('오목판의 크기를 숫자로 입력해주세요.')
        game_ready()
            
def reset_board():# 다시 시작할시 보드 초기화 
    for x in range(len_board):
        for y in range(len_board):
            omok[x][y] = '0'
    global turn
    turn = -1
    game_ready()    

def Easter_egg(po, la, color):#특수 입력값 상호작용
    if color == 1 :
        other = 2
    else :
        other = 1
    if po == '0829' or la == '0829' :
        print('제작자의 생일!! 당신의 승리!!')
        judge_win(1,1,1,100,color)
        return True
    if po == '0622' or la == '0622' :
        print('당신의 패배입니다..')
        judge_win(1, 1, 1, 100, other)
        return True
    return False

def po_la_input(color):#사용자 입력값 
    if color == 1 :
        VAr = '검은'
        stone = '●'
    else :
        VAr = '흰'
        stone = '○'
    print(VAr,'색돌의 세로줄을 입력하세요 : ',end='')
    po = input()
    print(VAr,'색돌의 가로줄을 입력하세요 : ',end='')
    la = input()
    if Easter_egg(po, la, color) == True :
        return 0
    for x in range(1,3):
        for y in range(len_board):
            if la == Eng_Num[x][y] :
                la = Eng_Num[0][y]
    for x in range(1,3):
        for y in range(len_board):
            if po == Eng_Num[x][y] :
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
    if po_is == True and la_is == True :
        po = int(po) - 1
        la = int(la) - 1 
        if( po >= len_board or po < 0 ) or ( la >= len_board or la < 0 ) :
            print('범위를 벗어난 좌표입니다')
            po_la_input(color)
        else :
            if omok[po][la] == '0' :
                omok[po][la] = stone
                judge_win(po,la,1,0,color)
            elif omok[po][la] == '○' :
                print('그곳에는 흰색돌이 있습니다.')
                po_la_input(color)
            else :
                print('그곳에는 검은색돌이 있습니다.')
                po_la_input(color)        
    else :
        print('범위에 맞는 숫자나 알파벳을 입력해주세요')
        po_la_input(color)
    
def print_board(color):#보드 출력
    os.system('cls')
    if color % 2 == 0 :
        VAR = '검은색'
    else :
        VAR = '흰색'
    print('오목',VAR,'차례')
    print(' ',end='')
    for x in range(len_board):
        if x >= 10 :
            x -= 10 
            print(x+1,'',end='')
        else :
            print(x+1,'',end='')
    print()
        
    for x in range(len_board):
        for y in range(len_board):
            if( y == len_board - 1 ):
                if omok[x][y] == '0' :
                    print('  ',end='')
                    print(x+1,end='')
                else :
                    print(omok[x][y],end='')
                    print(x+1,end='')
            else:
                if( omok[x][y] == '0' ):
                    print('  ',end='')
                else:
                    print(omok[x][y],end='')
        print('')
        
def judge_win(po, la, di, score, color):#승리 판단 메인함수
    global b_win
    global w_win
    global Game_repeat
    global count_y
    if color == 3 :
        print('무승부입니다 ',end='')
        repeat_game()
        if count_y == 1 :
            count_y = 0
            reset_board()
            return 0 
        elif count_n == 1 :
            Game_repeat = True
            return 0
        
    if di == 5 : return 0
    
    stack = judge_win_left(po, la, di, score, color) + judge_win_right(po, la, di, score, color) - 1
    if stack >= num_game :
        
        
        if color == 1:
            print_color = '검은색'
            b_win += 1
            
        else:
            print_color = '흰색'
            w_win += 1
            
        print(print_color,'승리 한번더 하시겠습니까 \'Y\'?','',end='')
        repeat_game()
        if count_y == 1 :
            count_y = 0
            reset_board()
            return 0
        
        else :
            Game_repeat = True
            return 0
        
    else :
        judge_win(po, la, di + 1, score, color)
        return 0        
            
def judge_win_right(po, la, di, score, color):#승리 판단 오른쪽

    if color == 1 :
        Var = '●'
        
    else :
        Var = '○'

    if di ==  1 :
        if ( la == len_board or la < 0 ) or ( po == len_board or po < 0 ) :
            return score
        elif omok[po][la] == Var :
            score += judge_win_right(po, la+1, di, 1,color)
            return score
        else :
            return score

    if di == 2 :
        if ( la == len_board or la < 0 ) or ( po == len_board or po < 0 ) :
            return score
        elif omok[po][la] == Var :
            score += judge_win_right(po+1, la+1, di ,1, color)
            return score
        else :
            return score

    if di == 3 :
        if ( la == len_board or la < 0 ) or ( po == len_board or po < 0 ) :
            return score
        elif omok[po][la] == Var :
            score += judge_win_right(po+1, la, di, 1, color)
            return score
        else :
            return score 
        
    if di == 4 :
        if ( la == len_board or la < 0 ) or ( po == len_board or po < 0 ) :
            return score
        elif omok[po][la] == Var:
            score += judge_win_right(po-1, la+1, di, 1, color)
            return score
        else :
            return score

        
def judge_win_left(po, la, di, score, color):#승리판단 왼쪽

    if color == 1 :
        Var = '●'
    else :
        Var = '○'
        
    if di == 1 :
        if ( la == len_board or la < 0 ) or ( po == len_board or po < 0 ) :
            return score
        elif omok[po][la] == Var :
            score += judge_win_left(po, la-1, di, 1, color)
            return score
        else :
            return score
        
    if di == 2 :
        if ( la == len_board or la < 0 ) or ( po == len_board or po < 0 ) :
            return score
        elif omok[po][la] == Var :
            score += judge_win_left(po-1, la-1, di, 1, color)
            return score
        else :
            return score
        
    if di == 3 :
        if ( la == len_board or la < 0 ) or ( po == len_board or po < 0 ) :
            return score
        elif omok[po][la] == Var :
            score += judge_win_left(po-1, la, di, 1, color)
            return score
        else :
            return score
        
    if di == 4 :
        if ( la == len_board or la < 0 ) or ( po == len_board or po < 0 ) :
            return score
        elif omok[po][la] == Var :
            score += judge_win_left(po+1, la-1, di, 1, color)
            return score
        else :
            return score

#main 함수
game_ready()
while Game_repeat == False:
    if ( turn == len_board * len_board ):
        judge_win(1, 1, 1, 0, 3)
        turn += 1
    print_board(turn)
    if( turn % 2 == 0 ):
        po_la_input(1)   
    else :
        po_la_input(2)  
    turn += 1
    


print('검은색 승리 횟수 :',b_win,'흰색 승리 횟수 :',w_win)
print('프로그램을 종료합니다.')
