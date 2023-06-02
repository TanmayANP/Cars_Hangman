import random#

while True:
    print("                                C_A_R_S  H_A_N_G_M_A_N")
    print("""
Type 'Yes' to Play New Game
Type 'No' to Quit
          """)
    
    response = input('Ready To Play: ').lower()
    if response == 'yes':
        file = open('cars.txt')
        word_list = random.sample(file.read().upper().split(', '), 10)
        file.close()
        score = 0
        i = 0
        
        for j in range(len(word_list)):
            word = word_list[j]
            print('/nWord ' + str(j + 1) + '.')
            all_used = []
            if ' ' in word:
                i = word.index(' ')
                display_value = ['_,']*i + [' '] + ['_,']*(len(word) - i - 1)             
            else:
                display_value = ['_,']*len(word)             
            print('\n' + ''.join(display_value)[:-1] + '\n')
            
            a = 5
            print('Mistakes allowed = ', a)
            while a > 0:
                b = input('> ').upper()
                if b in all_used:
                    b = input('Already used!\n> ').upper()
                elif len(b) > 1:
                    b = input('Enter one leter only!\n> ').upper()                 
                all_used += [b]
                a -= 1
                
                for c in range(len(word)):
                    if word[c] == b:
                        display_value[c] = b
                        a += 1
                
                print('\n\n' + ''.join(display_value) + '\n\n')
                if ''.join(display_value) == word:
                    score += 1
                    print('Great!\nScore:'+str(score)+"/10\n")
                    break      
                elif a == 0:
                    print(word+"\nBetter luck next time.\n"+str(score)+"/10\n")           
                else:
                    print("Used: " + ' '.join(all_used))
                    print("Chances Remaining: " + str(a) + '\n\n')
                    
    elif response == 'no':
        break
        
    else:
        print('\nI am not able to understand!\n\n\n\n')
        
exit()
