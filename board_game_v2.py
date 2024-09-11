#The import thingies
import time
import random
import numpy as np

#The charactors you play as
piece1 = ['Grand Executioner', 2000, 20000, 1, 1, 'Amputate: "Anyone targeted by this ability loses their limbs, and can`t make any moves for the next turn"', '1', 2]
piece2 = ['Drago: The Dragon King', 4000, 12000, 2, 2, 'Blazing Breath: "Burn your target, causing them to take 250-750 damage every turn for the next 5 turns"', '2', 5]
piece3 = ['Simple Soldier', 2000, 10000, 2, 0, 'None: This charactor has no ability', '3', 0]

#The thing that figures out which character you selected
def card_select(c):
    if c == piece1[6]:
        ch = piece1
    elif c == piece2[6]:
        ch = piece2
    elif c == piece3[6]:
        ch = piece3
    else:
        print('\nYou didn`t select a valid character')
        ch = 'invalid'
    return ch

#Where you input which character you select
def p_card(P):
    i = 0
    l = 1
    while i < l:
        c = input('\n' + P + ', enter the number of the character you would like to use> ')
        ch = card_select(c)
        time.sleep(.5)
        
        if ch == 'invalid':
            l += 1
        else:
            print('\n' + P + ' your character is "' + ch[0] + '"\nTheir attack power is ' + str(ch[1]) + '\nTheir defense power is ' + str(ch[2]) + '\nTheir attack range is ' + str(ch[3]) + '\nAnd their ability is ' + ch[5])
        i += 1
    return ch

#The thing that sets your range around you
def range_set(board, row, col, range, piece1, piece2, piece3):
    s_n1 = 1
    ir1 = 1
    while ir1 <= range:
        n_row = row - s_n1
        if 0 <= n_row <= row_count - 1:
            if board[n_row][col] == 0:
                board[n_row][col] = piece1
            elif board[n_row][col] == piece2:
                board[n_row][col] = piece3
        ns_n1 = 1
        nrt1 = range - ir1
        nr1 = 1
        while nr1 <= nrt1:
            n_col = col - ns_n1
            if 0 <= n_row <= row_count - 1 and 0 <= n_col <= column_count - 1:
                if board[n_row][n_col] == 0:
                    board[n_row][n_col] = piece1
                elif board[n_row][n_col] == piece2:
                    board[n_row][n_col] = piece3
            nr1 += 1
            ns_n1 += 1
        s_n1 += 1
        ir1 += 1
        time.sleep(0.05)
        
    s_n2 = 1
    ir2 = 1
    while ir2 <= range:
        n_col = col - s_n2
        if 0 <= n_col <= column_count - 1:
            if board[row][n_col] == 0:
                board[row][n_col] = piece1
            elif board[row][n_col] == piece2:
                board[row][n_col] = piece3
        ns_n2 = 1
        nrt2 = range - ir2
        nr2 = 1
        while nr2 <= nrt2:
            n_row = row + ns_n2
            if 0 <= n_row <= row_count - 1 and 0 <= n_col <= column_count - 1:
                if board[n_row][n_col] == 0:
                    board[n_row][n_col] = piece1
                elif board[n_row][n_col] == piece2:
                    board[n_row][n_col] = piece3
            nr2 += 1
            ns_n2 += 1
        s_n2 += 1
        ir2 += 1
        time.sleep(0.05)
        
    s_n3 = 1
    ir3 = 1
    while ir3 <= range:
        n_row = row + s_n3
        if 0 <= n_row <= row_count - 1:
            if board[n_row][col] == 0:
                board[n_row][col] = piece1
            elif board[n_row][col] == piece2:
                board[n_row][col] = piece3
        ns_n3 = 1
        nrt3 = range - ir3
        nr3 = 1
        while nr3 <= nrt3:
            n_col = col + ns_n3
            if 0 <= n_row <= row_count - 1 and 0 <= n_col <= column_count - 1:
                if board[n_row][n_col] == 0:
                    board[n_row][n_col] = piece1
                elif board[n_row][n_col] == piece2:
                    board[n_row][n_col] = piece3
            nr3 += 1
            ns_n3 += 1
        s_n3 += 1
        ir3 += 1
        time.sleep(0.05) 
        
    s_n4 = 1
    ir4 = 1
    while ir4 <= range:
        n_col = col + s_n4
        if 0 <= n_col <= column_count - 1:
            if board[row][n_col] == 0:
                board[row][n_col] = piece1
            elif board[row][n_col] == piece2:
                board[row][n_col] = piece3
        ns_n4 = 1
        nrt4 = range - ir4
        nr4 = 1
        while nr4 <= nrt4:
            n_row = row - ns_n4
            if 0 <= n_row <= row_count - 1 and 0 <= n_col <= column_count - 1:
                if board[n_row][n_col] == 0:
                    board[n_row][n_col] = piece1
                elif board[n_row][n_col] == piece2:
                    board[n_row][n_col] = piece3
            nr4 += 1
            ns_n4 += 1
        s_n4 += 1
        ir4 += 1
        time.sleep(0.05)
        
#The thing that makes the board
row_count = 11
column_count = 7
def create_board():
    board = np.zeros((row_count, column_count))
    return board

#The thing that places your piece
def place_piece(board, piece1, piece2, piece3, piece4, row, col, range):
    board[nmove_r1][nmove_c1] = piece1
    board[nmove_r2][nmove_c2] = piece2
    if c_turn == 0:
        range_set(board, row, col, range, piece3, 2, piece4)
    elif c_turn == 1:
        range_set(board, row, col, range, piece3, 1, piece4)

#The thing that prevents you from moving out side of your range and on other players
def is_valid_location(board, move_r, move_c):
    if move_r <= row_count and move_c <= column_count:
        return board[move_r][move_c] == 3
    else:
        pass

#The thing that checks if a player is in range of your attack
def aa_range():
    r = 1
    while r <= row_count:
        rr = r - 1
        c = 1
        while c <= column_count:
            cc = c - 1
            if board[rr][cc] == 4:
                aa = True
                return aa 
            c += 1
        r += 1

#The thing that applies the effects of abilities
def ability(a):
    if a == 0:
        print('\nYour character doesn`t have an ability')
        e = 'none'
    elif a == 1:
        print('\nYou amputated your target')
        e = 'amputated'
    elif a == 2:
        print('\nYou burned your opponent')
        e = 'burned'
    return e

#The thing that checks your status effects each turn
def effect_c(p_s, p_st, pt):
    global m1_d
    global m2_d
    global p1_st
    global p2_st
    global p1_h
    global p2_h
    global p1_s
    global p2_s
    m1_d = False
    m2_d = False
    if p_st == 0:
        if pt == 'p1':
            p1_s = 'none'
        if pt == 'p2':
            p2_s = 'none'        
    if p_s == 'none':
        do_nothing = True
    elif p_s == 'amputated' and p_st > 0:
        print('\nYou have been amputated, and may not move this turn')
        if pt == 'p1':
            m1_d = True
            p1_st -= 1
        elif pt == 'p2':
            m2_d = True
            p2_st -= 1
    elif p_s == 'burned' and p_st > 0:
        print('\nYou have been burned, and will take damage every turn until it where`s off')
        if pt == 'p1':
            np1_h = p1_h - random.randint(250, 750)
            p1_h = np1_h
            p1_st -= 1
        if pt == 'p2':
            np2_h = p2_h - random.randint(250, 750)
            p2_h = np2_h
            p2_st -= 1
            
#The thing that is the center of all the other things
board = create_board()
print('Welcome to a hero-based board game')
print('\nHere is a list of all the characters:\n1. ' + piece1[0] + '\n2. ' + piece2[0] + '\n3. ' + piece3[0])
ch1 = p_card('P1')
ch2 = p_card('P2')

start = input('\npress enter when you are ready to start')
gameover = False
c_turn = 0
t_turn = 1
p1_h = ch1[2]
p2_h = ch2[2]
p1_s = 'none'
p1_st = 0
p2_s = 'none'
p2_st = 0
m1_d = False
m2_d = False
p1_au = False
p2_au = False
nmove_r1 = 8
nmove_c1 = 3
nmove_r2 = 2
nmove_c2 = 3
while not gameover:    
    #The most important players turn
    if c_turn == 0:
        effect_c(p1_s, p1_st, 'p1')
        i1 = 0
        l1 = 1
        while i1 < l1:
            if m1_d == False:
                board = create_board()
                place_piece(board, 1, 2, 3, 4, nmove_r1, nmove_c1, ch1[3])
                print(' ')
                print(board)
                print('\nP1 HP = ' + str(p1_h) + '\nP1 status effects = ' + p1_s)
                move_r1 = int(input('\nPlayer 1 select the row you would like to move to (1-11)> '))
                move_c1 = int(input('\nPlayer 1 select the column you would like to move to (1-7)> '))
                move_r1 -= 1
                move_c1 -= 1
            
            if is_valid_location(board, move_r1, move_c1) or m1_d == True:
                nmove_r1 = move_r1
                nmove_c1 = move_c1
                board = create_board()
                place_piece(board, 1, 2, 3, 4, nmove_r1, nmove_c1, ch1[3])
                ii1 = 0
                ll1 = 1
                while ii1 < ll1:
                    print(' ')
                    print(board)
                    print('\nP1 HP = ' + str(p1_h) + '\nP1 status effects = ' + p1_s)
                    move1 = input('\nP1, would you like to attack, use your ability, or skip> ')
                    m1 = move1.lower()
                    time.sleep(.5)
                    
                    if m1 == 'attack' and m1_d == False:
                        if aa_range():
                            print('\nYou attacked the other player')
                            np2_h = p2_h - ch1[1]
                            p2_h = np2_h
                            mc1 = True
                        else:
                            mc1 = False
                    elif m1 == 'ability' and t_turn >= 3 and m1_d == False and p1_au == False:
                        if aa_range():
                            p2_s = ability(ch1[4])
                            p2_st = ch1[7]
                            if p2_s == 'none':
                                mc1 = False
                            else:
                                mc1 = True
                                p1_au = True
                        else:
                            mc1 = False
                    elif m1 == 'skip':
                        print('\nYou skipped your turn')
                        mc1 = True
                    else:
                        mc1 = False
                    
                    if mc1 == True:
                        ii1 += 1
                        time.sleep(.5)
                    else:
                        print('\nYou either didn`t input a valid move, the move you inputed was disabled, or your opponet was out of range')
                        time.sleep(.5)  
                i1 += 1
            else:
                print('\nyou didnt select a valid location')
        c_turn += 1
      
    #The least important players turn  
    elif c_turn == 1:
        effect_c(p2_s, p2_st, 'p2')
        i2 = 0
        l2 = 1
        while i2 < l2:
            if m2_d == False:
                board = create_board()
                place_piece(board, 1, 2, 3, 4, nmove_r2, nmove_c2, ch2[3])
                print(' ')
                print(board) 
                print('\nP2 HP = ' + str(p2_h) + '\nP2 status effects = ' + p2_s)
                move_r2 = int(input('\nPlayer 2 select where you would like to move to (1-11)> '))
                move_c2 = int(input('\nPlayer 2 select the column you would like to move to (1-7)> '))
                move_r2 -= 1
                move_c2 -= 1
            
            if is_valid_location(board, move_r2, move_c2) or m2_d == True:
                nmove_r2 = move_r2
                nmove_c2 = move_c2
                board = create_board()
                place_piece(board, 1, 2, 3, 4, nmove_r2, nmove_c2, ch2[3])
                ii2 = 0
                ll2 = 1
                while ii2 < ll2:
                    print(' ')
                    print(board)
                    print('\nP2 HP = ' + str(p2_h) + '\nP2 status effects = ' + p2_s)
                    move2 = input('\nP2, would you like to attack, use your ability, or skip> ')
                    m2 = move2.lower()
                    time.sleep(.5)
                    
                    if m2 == 'attack' and m2_d == False:
                        if aa_range():
                            print('\nYou attacked the other player')
                            np1_h = p1_h - ch2[1]
                            p1_h = np1_h
                            mc2 = True
                        else:
                            mc2 = False
                    elif m2 == 'ability' and t_turn >= 3 and m2_d == False and p2_au == False:
                        if aa_range():
                            p1_s = ability(ch2[4])
                            p1_st = ch2[7]
                            if p1_s == 'none':
                                mc2 = False
                            else:
                                mc2 = True
                                p2_au = True
                        else:
                            mc2 = False
                    elif m2 == 'skip':
                        print('\nYou skipped your turn')
                        mc2 = True
                    else:
                        mc2 = False
                    
                    if mc2 == True:
                        ii2 += 1
                        time.sleep(.5)
                    else:
                        print('\nYou either didn`t input a valid move, the move you inputed was disabled, or your opponet was out of range')
                        time.sleep(.5)                 
                
                i2 += 1
            else:
                print('\nyou didnt select a valid location')        
          
        c_turn -= 1
    t_turn += 1
    
    #The thingies that determine who won
    if p1_h <= 0:
        gameover = True
        print('\nP2 wins!')
    elif p2_h <= 0:
        gameover = True
        print('\nP1 wins')