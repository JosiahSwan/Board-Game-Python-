#The import thingies
import time
import random

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
        print('\nYou have been burned, and cannot move for until it where`s off')
        if pt == 'p1':
            p1_h -= random.randint(250, 750)
            p1_st -= 1
        if pt == 'p2':
            p2_h -= random.randint(250, 750)
            p2_st -= 1
            
#The thing that is the center of all the other things
print('Welcome to a hero-based board game')
print('\nHere is a list of all the characters:\n1. ' + piece1[0] + '\n2. ' + piece2[0] + '\n3. ' + piece3[0])
ch1 = p_card('P1')
ch2 = p_card('P2')

start = input('\npress enter when you are ready to start')
gameover = False
c_turn = 1
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
while not gameover:   
    #The most important player`s turn
    if c_turn == 1:
        effect_c(p1_s, p1_st, 'p1')
        i1 = 0
        l1 = 1
        while i1 < l1:
            print('\nP1 HP = ' + str(p1_h) + '\nP1 status effects = ' + p1_s)
            move1 = input('\nP1, would you like to attack, use your ability, or skip> ')
            m1 = move1.lower()
            time.sleep(.5)
            
            if m1 == 'attack' and m1_d == False:
                p2_h -= ch1[1]
                print('\nYou attacked the other player')
                mc1 = True
            elif m1 == 'ability' and t_turn >= 3 and m1_d == False and p1_au == False:
                p2_s = ability(ch1[4])
                p2_st = ch1[7]
                if p2_s == 'none':
                    mc1 = False
                else:
                    mc1 = True
                    p1_au = True
            elif m1 == 'skip':
                print('\nYou skipped your turn')
                mc1 = True
            else:
                mc1 = False
            
            if mc1 == True:
                c_turn -= 1
                t_turn += 1
                i1 += 1
                time.sleep(.5)
            else:
                print('\nYou either didn`t input a valid move, or the move you inputed was disabled')
                time.sleep(.5)
    #The Least important player`s turn
    elif c_turn == 0:
        effect_c(p2_s, p2_st, 'p2')
        i2 = 0
        l2 = 1
        while i2 < l2:
            print('\nP2 HP = ' + str(p2_h) + '\nP2 status effects = ' + p2_s)
            move2 = input('\nP2, would you like to attack, use your ability, or skip> ')
            m2 = move2.lower()
            time.sleep(.5)
            
            if m2 == 'attack' and m2_d == False:
                p1_h -= ch2[1]
                print('\nYou attacked the other player')
                mc2 = True
            elif m2 == 'ability' and t_turn >= 3 and m2_d == False and p2_au == False:
                p1_s = ability(ch2[4])
                p1_st = ch2[7]
                if p1_s == 'none':
                    mc2 = False
                else:
                    mc2 = True
                    p2_au = True
            elif m2 == 'skip':
                print('\nYou skipped your turn')
                mc2 = True
            else:
                mc2 = False
            
            if mc2 == True:
                c_turn += 1
                t_turn += 1
                i2 += 1
                time.sleep(.5)
            else:
                print('\nYou either didn`t input a valid move, or the move you inputed was disabled')
                time.sleep(.5)
    
    #If somebody wins            
    if p1_h <= 0:
        print('\nP2 wins!')
        gameover = True
    elif p2_h <= 0:
        print('\nP1 wins!')
        gameover = True 