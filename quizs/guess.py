def guess_game_function():
    print("Guessing game..............")
    number = '16'
    guess = input("Enter number ")
    count = 0

    while count < 3:
        if number == guess:
            print("correct number")
            break
        elif number != guess:
            print("incorrect number")
            count = count + 1
            continue
        else:
            print("allow numbers only.")
            break


guess_game_function()
