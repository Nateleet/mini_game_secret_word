import time
import random
from english_words import get_english_words_set
def secret_word(word):
    word = random.choice(word)
    print('\n'*1000)
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
        time.sleep(1)
        return "Restart, please"
    print('\n')
    print("Secret word:",*secret)
    print('\n')
    attemp_visual = ["*"] * try_req
    if type(try_req) is not int:
        print("Enter number please!")
        print(try_req)

    print('Attemps:',*attemp_visual)
    while er < try_req:
        if "_" not in secret:
            print('\n')
            print("You win!")
            print('Restart? y/n')
            rest = input()
            rest = rest.lower()
            if rest == 'y':
                secret_word(word)
            else:
                time.sleep(1)
                print("bye")
                return ':)'

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
    print("Word: ", word)
    print('Restart? y/n')
    rest = input()
    rest = rest.lower()
    if rest == 'y':
            secret_word(word)
    if rest == 'n':
        time.sleep(1)
        return "bye"


# words = input("Enter your word:")




words = get_english_words_set(['web2'])
words = list(words)




print(secret_word(words))