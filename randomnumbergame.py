from random import randint

def run_game(guess, answer):
    if  0< guess < 11:
        if guess == answer:
            return True
    else:
        print ('1-10. try again')
        return False

if __name__ == '__main__':
    answer = randint(1, 10)
    print(answer)

    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if run_game(guess, answer):
                print('correct!')
                break
        except ValueError:
            print('pls enter a number')
            continue





