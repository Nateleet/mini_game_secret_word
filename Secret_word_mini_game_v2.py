import time
import random
def secret_word(words):
    word = words[:]
    word = random.choice(word)
    print("Hello!")
    print("\n")
    hints = input("Enable hints? y/n\n")
    print('\n')
    word = word.lower()
    lst_word = list(word)
    er = 0
    secret = ["_"] * len(lst_word)
    try:
        try_req = int(input("Enter attempts:"))
    except ValueError:
        print("Error_01: Enter number!")
        try_req = int(input("Enter attempts:"))
    

    print('\n')
    print("Secret word:",*secret)
    print('\n')
    attemp_visual = ["*"] * try_req
    if type(try_req) is not int:
        print("Enter number please!")
        

    print('Attemps:',*attemp_visual)
    while er < try_req:
        if "_" not in secret:
            print('\n')
            print("You win!")
            print('Restart? y/n')
            rest = input()
            rest = rest.lower()
            if rest == 'y':
                secret_word(words)
            if rest == 'n':
                time.sleep(1)
                return "bye"
            else:
                return "bye"


        req = input("Enter a letter:")
        req = req.lower()
        if req in lst_word:
            ind = lst_word.index(req)
            secret[ind] = req
            lst_word[ind] = '*'
            if hints == "y":
                for i in lst_word:
                    if i == req:
                        ind = lst_word.index(req)
                        secret[ind] = req
                        lst_word[ind] = '*'

                
            print("Secret word:",*secret)
            
        else:
            er+=1
            attemp_visual.pop()
            if len(attemp_visual) != 0:
                print('Attemps:',*attemp_visual)
            else:
                print("No try(")
    print('\n')
    print("You lose!")
    print("Word:", word)
    print('Restart? y/n')
    rest = input()
    rest = rest.lower()
    if rest == 'y':
            secret_word(words)
    if rest == 'n':
        time.sleep(1)
        return "bye"
    else:
        return "bye"

with open('word.txt', "r") as f:
    all_words = []
    line = f.readline().split()
    while line:
        all_words.extend(line)
        line = f.readline().split()






print(secret_word(all_words))
