#The import thingies
import time
import random
import numpy as np

#The charactors you play as
piece = [['Grand Executioner', 2500, 20000, 1, 1, 'Amputate: "Anyone targeted by this ability loses their limbs, and can`t make any moves for the next turn"', '1', 2, 'a'], ['Drago: The Dragon King', 4000, 12000, 2, 2, 'Blazing Breath: "Burn your target, causing them to take 250-750 damage every turn for the next 5 turns"', '2', 5, 'a'], ['Simple Soldier', 2000, 10000, 2, 0, 'None: This charactor has no ability', '3', 0, 'a'], ['Great Fairy Fiona', 1500, 20000, 3, 3, 'Healing: All allies within range will be healed 2000 HP or to their max health', '4', 1, 's']]

#The thing that figures out which character you selected
def card_select(c):
    if c == piece[0][6]:
        ch = piece[0]
    elif c == piece[1][6]:
        ch = piece[1]
    elif c == piece[2][6]:
        ch = piece[2]
    elif c == piece[3][6]:
        ch = piece[3]
    else:
        print('\nYou didn`t select a valid character')
        ch = 'invalid'
    return ch

#Where you input which character you select
def p_card(P, ch_n):
    i = 0
    l = 1
    while i < l:
        c = input('\n' + P + ', enter the number of the ' + ch_n + ' character you would like to use> ')
        ch = card_select(c)
        time.sleep(.5)
        
        if ch == 'invalid':
            l += 1
        else:
            print('\n' + P + ' your ' + ch_n + ' character is "' + str(ch[0]) + '"\nTheir attack power is ' + str(ch[1]) + '\nTheir defense power is ' + str(ch[2]) + '\nTheir attack range is ' + str(ch[3]) + '\nAnd their ability is ' + str(ch[5]))
        i += 1
    return ch

#The thing that sets your range around you
def range_set(board, row, col, range, piece1, piece2, piece3, piece4, piece6, piece7, piece8):
    s_n1 = 1
    ir1 = 1
    while ir1 <= range:
        n_row = row - s_n1
        if 0 <= n_row <= row_count - 1:
            if board[n_row][col] == 0:
                board[n_row][col] = piece1
            elif board[n_row][col] == piece2:
                board[n_row][col] = piece6
            elif board[n_row][col] == piece3:
                board[n_row][col] = piece7
            elif board[n_row][col] == piece4:
                board[n_row][col] = piece8                
        ns_n1 = 1
        nrt1 = range - ir1
        nr1 = 1
        while nr1 <= nrt1:
            n_col = col - ns_n1
            if 0 <= n_row <= row_count - 1 and 0 <= n_col <= column_count - 1:
                if board[n_row][n_col] == 0:
                    board[n_row][n_col] = piece1
                elif board[n_row][n_col] == piece2:
                    board[n_row][n_col] = piece6
                elif board[n_row][n_col] == piece3:
                    board[n_row][n_col] = piece7
                elif board[n_row][n_col] == piece4:
                    board[n_row][n_col] = piece8 
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
                board[row][n_col] = piece6
            elif board[row][n_col] == piece3:
                board[row][n_col] = piece7
            elif board[row][n_col] == piece4:
                board[row][n_col] = piece8           
        ns_n2 = 1
        nrt2 = range - ir2
        nr2 = 1
        while nr2 <= nrt2:
            n_row = row + ns_n2
            if 0 <= n_row <= row_count - 1 and 0 <= n_col <= column_count - 1:
                if board[n_row][n_col] == 0:
                    board[n_row][n_col] = piece1
                elif board[n_row][n_col] == piece2:
                    board[n_row][n_col] = piece6
                elif board[n_row][n_col] == piece3:
                    board[n_row][n_col] = piece7
                elif board[n_row][n_col] == piece4:
                    board[n_row][n_col] = piece8
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
                board[n_row][col] = piece6
            elif board[n_row][col] == piece3:
                board[n_row][col] = piece7
            elif board[n_row][col] == piece4:
                board[n_row][col] = piece8
        ns_n3 = 1
        nrt3 = range - ir3
        nr3 = 1
        while nr3 <= nrt3:
            n_col = col + ns_n3
            if 0 <= n_row <= row_count - 1 and 0 <= n_col <= column_count - 1:
                if board[n_row][n_col] == 0:
                    board[n_row][n_col] = piece1
                elif board[n_row][n_col] == piece2:
                    board[n_row][n_col] = piece6
                elif board[n_row][n_col] == piece3:
                    board[n_row][n_col] = piece7
                elif board[n_row][n_col] == piece4:
                    board[n_row][n_col] = piece8
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
                board[row][n_col] = piece6
            elif board[row][n_col] == piece3:
                board[row][n_col] = piece7
            elif board[row][n_col] == piece4:
                board[row][n_col] = piece8
        ns_n4 = 1
        nrt4 = range - ir4
        nr4 = 1
        while nr4 <= nrt4:
            n_row = row - ns_n4
            if 0 <= n_row <= row_count - 1 and 0 <= n_col <= column_count - 1:
                if board[n_row][n_col] == 0:
                    board[n_row][n_col] = piece1
                elif board[n_row][n_col] == piece2:
                    board[n_row][n_col] = piece6
                elif board[n_row][n_col] == piece3:
                    board[n_row][n_col] = piece7
                elif board[n_row][n_col] == piece4:
                    board[n_row][n_col] = piece8
            nr4 += 1
            ns_n4 += 1
        s_n4 += 1
        ir4 += 1
        time.sleep(0.05)
        
#The thing that makes the board
row_count = 11
column_count = 9
def create_board():
    board = np.zeros((row_count, column_count))
    return board

#The thing that places your piece
def place_piece(board, piece2, piece3, piece4, row, col, range, piece5, piece6, piece7, piece8):
    board[nmove_r11][nmove_c11] = 1
    board[nmove_r12][nmove_c12] = 3
    board[nmove_r21][nmove_c21] = 2
    board[nmove_r22][nmove_c22] = 4
    range_set(board, row, col, range, piece5, piece2, piece3, piece4, piece6, piece7, piece8)

#The thing that prevents you from moving out side of your range and on other players
def is_valid_location(board, move_r, move_c):
    if move_r <= row_count and move_c <= column_count:
        return board[move_r][move_c] == 5
    else:
        pass

#The thing that checks if a player is in range of your attack
def aa_range(piece):
    r = 1
    while r <= row_count:
        rr = r - 1
        c = 1
        while c <= column_count:
            cc = c - 1
            if board[rr][cc] == piece:
                aa = True
                return aa 
            c += 1
        r += 1

#The thing that applies the effects of abilities
def ability(a):
    global p1_h1
    global p1_h2
    global p2_h1
    global p2_h2
    if a == 0:
        print('\nYour character doesn`t have an ability')
        e = 'none'
    elif a == 1:
        print('\nYou amputated your target')
        e = 'amputated'
    elif a == 2:
        print('\nYou burned your opponent')
        e = 'burned'
    elif a == 3:
        print('\nYou healed your ally')
        e = 'healed'
    return e

#The thing that checks your status effects each turn
def effect_c(p_s, p_st, pt):
    global m1_d1
    global m1_d2
    global m2_d1
    global m2_d2
    global p1_st1
    global p1_st2
    global p2_st1
    global p2_st2
    global p1_h1
    global p1_h2
    global p2_h1
    global p2_h2
    global p1_s1
    global p1_s2
    global p2_s1
    global p2_s2
    m1_d1 = False
    m1_d2 = False
    m2_d1 = False
    m2_d2 = False
    if p_st == 0:
        if pt == 'p11':
            p1_s1 = 'none'
        elif pt == 'p12':
            p1_s2 = 'none'            
        elif pt == 'p21':
            p2_s1 = 'none'
        elif pt == 'p22':
            p2_s1 = 'none'        
    if p_s == 'none':
        do_nothing = True
    elif p_s == 'amputated' and p_st > 0:
        print('\nYou have been amputated, and may not move this turn')
        if pt == 'p11':
            m1_d1 = True
            p1_st1 -= 1
        elif pt == 'p11':
            m1_d2 = True
            p1_st1 -= 1            
        elif pt == 'p21':
            m2_d1 = True
            p2_st1 -= 1
        elif pt == 'p22':
            m2_d2 = True
            p2_st2 -= 1            
    elif p_s == 'burned' and p_st > 0:
        print('\nYou have been burned, and will take damage every turn until it where`s off')
        if pt == 'p11':
            np1_h1 = p1_h1 - random.randint(250, 750)
            p1_h1 = np1_h1
            p1_st1 -= 1
        elif pt == 'p12':
            np1_h2 = p1_h2 - random.randint(250, 750)
            p1_h2 = np1_h2
            p1_st2 -= 1            
        elif pt == 'p21':
            np2_h1 = p2_h1 - random.randint(250, 750)
            p2_h1 = np2_h1
            p2_st1 -= 1
        elif pt == 'p22':
            np2_h2 = p2_h2 - random.randint(250, 750)
            p2_h2 = np2_h2
            p2_st2 -= 1 
    elif p_s == 'healed' and p_st > 0:
        print('\nYou have been healed, and your hp has been increased by 2000, or to its max')
        if pt == 'p11':
            if p1_h1 + 2000 >= ch11[2]:
                p1_h1 = ch11[2]
            else:
                p1_h1 += 2000
            p1_st1 -= 1
        elif pt == 'p12':
            if p1_h2 + 2000 >= ch12[2]:
                p1_h2 = ch12[2]
            else:
                p1_h2 += 2000 
            p1_st2 -= 1
        elif pt == 'p21':
            if p2_h1 + 2000 >= ch21[2]:
                p2_h1 = ch21[2]
            else:
                p2_h1 += 2000
            p2_st1 -= 1
        elif pt == 'p22':
            if p2_h2 + 2000 >= ch22[2]:
                p2_h2 = ch22[2]
            else:
                p2_h2 += 2000 
            p2_st2 -= 1
            
#the thing that prints the board
def print_board(r, c):
    columns = [1]
    sc = 1
    while sc < c:
        sc += 1
        columns.append(sc)
    print('  ', columns)
    for i in range (len(board)):
        row = i + 1
        if row < 10:
            print(row, '', board[i])
        if row >= 10:
            print(row, board[i])        
            
#The thing that is at the center of all the other things
board = create_board()
print('Welcome to a hero-based board game')
print('\nHere is a list of all the characters:\n1. ' + piece[0][0] + '\n2. ' + piece[1][0] + '\n3. ' + piece[2][0] + '\n4. ' + piece[3][0])
ch11 = p_card('P1', 'first')
ch12 = p_card('P1', 'second')
ch21 = p_card('P2', 'first')
ch22 = p_card('P2', 'second')

start = input('\npress enter when you are ready to start')
gameover = False
c_turn = 0
t_turn = 1
p1_h1 = ch11[2]
p1_h2 = ch12[2]
p2_h1 = ch21[2]
p2_h2 = ch22[2]
p1_s1 = 'none'
p1_st1 = 0
p1_s2 = 'none'
p1_st2 = 0
p2_s1 = 'none'
p2_st1 = 0
p2_s2 = 'none'
p2_st2 = 0
m1_d1 = False
m1_d2 = False
m2_d1 = False
m2_d2 = False
p1_au1 = False
p1_au2 = False
p2_au1 = False
p2_au2 = False
nmove_r11 = 8
nmove_c11 = int((((column_count / 2) + 0.5) - ((((column_count / 2) + 0.5) / 2) - 0.5)) - 1)
nmove_r12 = 8
nmove_c12 = int((((column_count / 2) + 0.5) + ((((column_count / 2) + 0.5) / 2) - 0.5)) - 1)
nmove_r21 = 2
nmove_c21 = int((((column_count / 2) + 0.5) - ((((column_count / 2) + 0.5) / 2) - 0.5)) - 1)
nmove_r22 = 2
nmove_c22 = int((((column_count / 2) + 0.5) + ((((column_count / 2) + 0.5) / 2) - 0.5)) - 1)

while not gameover:    
    #The most important players turn
    if c_turn == 0:
        if p1_h1 > 0:
            effect_c(p1_s1, p1_st1, 'p11')
            i11 = 0
            l11 = 1
            while i11 < l11:
                if m1_d1 == False:
                    board = create_board()
                    place_piece(board, 3, 2, 4, nmove_r11, nmove_c11, ch11[3], 5, 6, 7, 8)
                    print(' ')
                    print_board(row_count, column_count)
                    print('\nP1 C1 HP = ' + str(p1_h1) + '\nP1 C1 status effects = ' + p1_s1)
                    move_r11 = int(input('\nPlayer 1 select the row you would like to move to (1-11)> '))
                    move_c11 = int(input('\nPlayer 1 select the column you would like to move to (1-7)> '))
                    move_r11 -= 1
                    move_c11 -= 1
                
                if is_valid_location(board, move_r11, move_c11) or m1_d1 == True:
                    nmove_r11 = move_r11
                    nmove_c11 = move_c11
                    board = create_board()
                    place_piece(board, 3, 2, 4, nmove_r11, nmove_c11, ch11[3], 5, 6, 7, 8)
                    ii11 = 0
                    ll11 = 1
                    while ii11 < ll11:
                        print(' ')
                        print_board(row_count, column_count)
                        print('\nP1 C1 HP = ' + str(p1_h1) + '\nP1 C1 status effects = ' + p1_s1)
                        a_move11 = input('\nP1, would you like to attack, use your ability, or skip> ')
                        m11 = a_move11.lower()
                        time.sleep(.5)
                        mc11 = False
                        
                        if m11 == 'attack' and m1_d1 == False:
                            if aa_range(7):
                                print('\nYou attacked another player')
                                np2_h1 = p2_h1 - ch11[1]
                                p2_h1 = np2_h1
                                mc11 = True
                            if aa_range(8):
                                print('\nYou attacked another player')
                                np2_h2 = p2_h2 - ch11[1]
                                p2_h2 = np2_h2
                                mc11 = True                
                        elif m11 == 'ability' and t_turn >= 3 and m1_d1 == False and p1_au1 == False:
                            if aa_range(6) and ch11[8] == 's':
                                p1_s2 = ability(ch11[4])
                                p1_st2 = ch11[7]
                                if ch11[4] == 3:
                                    mc11 = True
                                else:
                                    mc11 = True
                                    p1_au1 = True
                            if aa_range(7) and ch11[8] == 'a':
                                p2_s1 = ability(ch11[4])
                                p2_st1 = ch11[7]
                                if p2_s1 == 'none':
                                    pass
                                else:
                                    mc11 = True
                                    p1_au1 = True
                            if aa_range(8) and ch11[8] == 'a':
                                p2_s2 = ability(ch11[4])
                                p2_st2 = ch11[7]
                                if p2_s2 == 'none':
                                    pass
                                else:
                                    mc11 = True
                                    p1_au1 = True
                        elif m11 == 'skip':
                            print('\nYou skipped your turn')
                            mc11 = True
                        else:
                            mc11 = False
                        
                        if mc11 == True:
                            ii11 += 1
                            time.sleep(.5)
                        else:
                            print('\nYou either didn`t input a valid move, the move you inputed was disabled, or your opponet was out of range')
                            time.sleep(.5)  
                    i11 += 1
                else:
                    print('\nyou didnt select a valid location')
        c_turn += 1
      
    #The least important players turn  
    elif c_turn == 1:
        if p2_h1 > 0:
            effect_c(p2_s1, p2_st1, 'p21')
            i21 = 0
            l21 = 1
            while i21 < l21:
                if m2_d1 == False:
                    board = create_board()
                    place_piece(board, 4, 1, 3, nmove_r21, nmove_c21, ch21[3], 5, 6, 7, 8)
                    print(' ')
                    print_board(row_count, column_count) 
                    print('\nP2 C1 HP = ' + str(p2_h1) + '\nP2 C1 status effects = ' + p2_s1)
                    move_r21 = int(input('\nPlayer 2 select where you would like to move to (1-11)> '))
                    move_c21 = int(input('\nPlayer 2 select the column you would like to move to (1-7)> '))
                    move_r21 -= 1
                    move_c21 -= 1
                
                if is_valid_location(board, move_r21, move_c21) or m2_d1 == True:
                    nmove_r21 = move_r21
                    nmove_c21 = move_c21
                    board = create_board()
                    place_piece(board, 4, 1, 3, nmove_r21, nmove_c21, ch21[3], 5, 6, 7, 8)
                    ii21 = 0
                    ll21 = 1
                    while ii21 < ll21:
                        print(' ')
                        print_board(row_count, column_count)
                        print('\nP2 C1 HP = ' + str(p2_h1) + '\nP2 C1 status effects = ' + p2_s1)
                        move21 = input('\nP2, would you like to attack, use your ability, or skip> ')
                        m21 = move21.lower()
                        time.sleep(.5)
                        mc21 = False
                        
                        if m21 == 'attack' and m2_d1 == False:
                            if aa_range(7):
                                print('\nYou attacked another player')
                                np1_h1 = p1_h1 - ch21[1]
                                p1_h1 = np1_h1
                                mc21 = True
                            if aa_range(8):
                                print('\nYou attacked another player')
                                np1_h2 = p1_h2 - ch21[1]
                                p1_h2 = np1_h2
                                mc21 = True
                        elif m21 == 'ability' and t_turn >= 3 and m2_d1 == False and p2_au1 == False:
                            if aa_range(6) and ch21[8] == 's':
                                p2_s2 = ability(ch21[4])
                                p2_st2 = ch21[7]
                                if ch21[4] == 3:
                                    mc21 = True
                                else:
                                    mc21 = True
                                    p2_au1 = True                            
                            if aa_range(7) and ch21[8] == 'a':
                                p1_s1 = ability(ch21[4])
                                p1_st1 = ch21[7]
                                if p1_s1 == 'none':
                                    pass
                                else:
                                    mc21 = True
                                    p2_au1 = True
                            if aa_range(8) and ch21[8] == 'a':
                                p1_s2 = ability(ch21[4])
                                p1_st2 = ch21[7]
                                if p1_s2 == 'none':
                                    pass
                                else:
                                    mc21 = True
                                    p2_au1 = True
                        elif m21 == 'skip':
                            print('\nYou skipped your turn')
                            mc21 = True
                        else:
                            mc21 = False
                        
                        if mc21 == True:
                            ii21 += 1
                            time.sleep(.5)
                        else:
                            print('\nYou either didn`t input a valid move, the move you inputed was disabled, or your opponet was out of range')
                            time.sleep(.5)                 
                    
                    i21 += 1
                else:
                    print('\nyou didnt select a valid location')                  
        c_turn += 1
    
    #The most important player`s least important turn   
    elif c_turn == 2:
        if p1_h2 > 0:
            effect_c(p1_s2, p1_st2, 'p12')
            i12 = 0
            l12 = 1
            while i12 < l12:
                if m1_d2 == False:
                    board = create_board()
                    place_piece(board, 1, 2, 4, nmove_r12, nmove_c12, ch12[3], 5, 6, 7, 8)
                    print(' ')
                    print_board(row_count, column_count)
                    print('\nP1 C2 HP = ' + str(p1_h2) + '\nP1 C2 status effects = ' + p1_s2)
                    move_r12 = int(input('\nPlayer 1 select the row you would like to move to (1-11)> '))
                    move_c12 = int(input('\nPlayer 1 select the column you would like to move to (1-7)> '))
                    move_r12 -= 1
                    move_c12 -= 1
                
                if is_valid_location(board, move_r12, move_c12) or m1_d2 == True:
                    nmove_r12 = move_r12
                    nmove_c12 = move_c12
                    board = create_board()
                    place_piece(board, 1, 2, 4, nmove_r12, nmove_c12, ch12[3], 5, 6, 7, 8)
                    ii12 = 0
                    ll12 = 1
                    while ii12 < ll12:
                        print(' ')
                        print_board(row_count, column_count)
                        print('\nP1 C2 HP = ' + str(p1_h2) + '\nP1 C2 status effects = ' + p1_s2)
                        a_move12 = input('\nP2, would you like to attack, use your ability, or skip> ')
                        m12 = a_move12.lower()
                        time.sleep(.5)
                        mc12 = False
                        
                        if m12 == 'attack' and m1_d2 == False:
                            if aa_range(7):
                                print('\nYou attacked another player')
                                np2_h1 = p2_h1 - ch12[1]
                                p2_h1 = np2_h1
                                mc12 = True
                            if aa_range(8):
                                print('\nYou attacked another player')
                                np2_h2 = p2_h2 - ch12[1]
                                p2_h2 = np2_h2
                                mc12 = True                
                        elif m12 == 'ability' and t_turn >= 3 and m1_d2 == False and p1_au2 == False:
                            if aa_range(6) and ch12[8] == 's':
                                p1_s1 = ability(ch12[4])
                                p1_st1 = ch12[7]
                                if ch12[4] == 3:
                                    mc12 = True
                                else:
                                    mc12 = True
                                    p1_au2 = True                            
                            if aa_range(7) and ch12[8] == 'a':
                                p2_s1 = ability(ch12[4])
                                p2_st1 = ch12[7]
                                if p2_s1 == 'none':
                                    pass
                                else:
                                    mc12 = True
                                    p1_au2 = True
                            if aa_range(8) and ch12[8] == 'a':
                                p2_s2 = ability(ch12[4])
                                p2_st2 = ch12[7]
                                if p2_s2 == 'none':
                                    pass
                                else:
                                    mc12 = True
                                    p1_au2 = True
                        elif m12 == 'skip':
                            print('\nYou skipped your turn')
                            mc12 = True
                        else:
                            mc12 = False
                        
                        if mc12 == True:
                            ii12 += 1
                            time.sleep(.5)
                        else:
                            print('\nYou either didn`t input a valid move, the move you inputed was disabled, or your opponet was out of range')
                            time.sleep(.5)  
                    i12 += 1
                else:
                    print('\nyou didnt select a valid location')
        c_turn += 1
        
    #The least important players least important turn    
    elif c_turn == 3:
        if p2_h2 > 0:
            effect_c(p2_s2, p2_st2, 'p22')
            i22 = 0
            l22 = 1
            while i22 < l22:
                if m2_d2 == False:
                    board = create_board()
                    place_piece(board, 2, 1, 3, nmove_r22, nmove_c22, ch22[3], 5, 6, 7, 8)
                    print(' ')
                    print_board(row_count, column_count)
                    print('\nP2 C2 HP = ' + str(p2_h2) + '\nP2 C2 status effects = ' + p2_s2)
                    move_r22 = int(input('\nPlayer 2 select where you would like to move to (1-11)> '))
                    move_c22 = int(input('\nPlayer 2 select the column you would like to move to (1-7)> '))
                    move_r22 -= 1
                    move_c22 -= 1
                
                if is_valid_location(board, move_r22, move_c22) or m2_d2 == True:
                    nmove_r22 = move_r22
                    nmove_c22 = move_c22
                    board = create_board()
                    place_piece(board, 2, 1, 3, nmove_r22, nmove_c22, ch22[3], 5, 6, 7, 8)
                    ii22 = 0
                    ll22 = 1
                    while ii22 < ll22:
                        print(' ')
                        print_board(row_count, column_count)
                        print('\nP2 C2 HP = ' + str(p2_h2) + '\nP2 C2 status effects = ' + p2_s2)
                        move22 = input('\nP2, would you like to attack, use your ability, or skip> ')
                        m22 = move22.lower()
                        time.sleep(.5)
                        mc22 = False
                        
                        if m22 == 'attack' and m2_d2 == False:
                            if aa_range(7):
                                print('\nYou attacked another player')
                                np1_h1 = p1_h1 - ch22[1]
                                p1_h1 = np1_h1
                                mc22 = True
                            if aa_range(8):
                                print('\nYou attacked another player')
                                np1_h2 = p1_h2 - ch22[1]
                                p1_h2 = np1_h2
                                mc22 = True
                        elif m22 == 'ability' and t_turn >= 3 and m2_d2 == False and p2_au2 == False:
                            if aa_range(6) and ch22[8] == 's':
                                p2_s1 = ability(ch22[4])
                                p2_st1 = ch22[7]
                                if ch22[4] == 3:
                                    mc22 = True
                                else:
                                    mc22 = True
                                    p2_au2 = True                            
                            if aa_range(7) and ch22[8] == 'a':
                                p1_s1 = ability(ch22[4])
                                p1_st1 = ch22[7]
                                if p1_s1 == 'none':
                                    pass
                                else:
                                    mc22 = True
                                    p2_au2 = True
                            if aa_range(8) and ch22[8] == 'a':
                                p1_s2 = ability(ch22[4])
                                p1_st2 = ch22[7]
                                if p1_s2 == 'none':
                                    pass
                                else:
                                    mc22 = True
                                    p2_au2 = True
                        elif m22 == 'skip':
                            print('\nYou skipped your turn')
                            mc22 = True
                        else:
                            mc22 = False
                        
                        if mc22 == True:
                            ii22 += 1
                            time.sleep(.5)
                        else:
                            print('\nYou either didn`t input a valid move, the move you inputed was disabled, or your opponet was out of range')
                            time.sleep(.5)                 
                    
                    i22 += 1
                else:
                    print('\nyou didnt select a valid location')          
        c_turn -= 3    
    
    t_turn += 1
    
    #The thingies that determine who won
    if p1_h1 <= 0 and p1_h2 <= 0:
        gameover = True
        print('\nP2 wins!')
    elif p2_h1 <= 0 and p2_h2 <= 0:
        gameover = True
        print('\nP1 wins')