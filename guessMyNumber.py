print('Please think of a number between 0 and 100')
low = 0
high = 100
ans = ''
secret = (high + low) // 2
while True:
    print("Is your secret number", secret, end='')
    print("?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if ans == 'h':
        high = secret
        secret = (high + low) // 2
    elif ans == 'l':
        low = secret
        secret = (high + low) // 2
    elif ans == 'c':
        print('Game over. Your secret number was:', secret)
        break
    else:
        print('Sorry, I did not understand your input.')



