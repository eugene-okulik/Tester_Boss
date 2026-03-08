guess = 4
guess_input = 0

while guess_input != guess:
    guess_input = int(input("Попробуй угадать число от 1 до 10: "))

    if guess_input > 10 or guess_input < 1:
        print("Мы так не договаривались, только от 1 до 10!")
    elif guess_input == guess:
        print("You win! Perfect!")
        break
    elif guess_input > guess:
        print("Попробуй меньше")
    elif guess_input < guess:
        print("Попробуй больше")
