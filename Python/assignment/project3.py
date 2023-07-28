def add():
    a = int(input("Enter an integer"))
    b = int(input("Enter another integer"))
    addition = a + b
    print("Sum =", addition)


def minus():
    a = int(input("Enter an integer"))
    b = int(input("Enter another integer"))
    substraction = a - b
    print("Minus =", substraction)


def snake_ladder():
    import random

    lad = [(1, 38), (4, 14), (8, 30), (21, 42), (28, 76), (50, 67), (71, 92), (80, 99)]
    lader = dict(lad)
    sn = [(97, 78), (95, 56), (88, 24), (62, 18), (48, 26), (36, 6), (32, 10)]
    snake = dict(sn)
    lader = dict(lad)
    lader
    score1 = 0
    score2 = 0

    def snakeLogic(score):
        dice = random.randint(1, 6)
        if (score == 95):
            print(dice)
            if (score in snake.keys()):
                score = snake[score]

        elif (score == 96):
            print(dice)
            if (dice <= 4):
                score += dice
                print("Score", score)
        elif (score == 97):
            print(dice)
            if (score in snake.keys()):
                score = snake[score]

        elif (score == 98):
            print(dice)
            if (dice <= 2):
                score += dice
                print("Score", score)
        elif (score == 99):
            print(dice)
            if (dice <= 1):
                score += dice
                print("Score", score)

        else:
            if (score <= 94):
                print(dice)
                score += dice

            if (score in lader.keys()):
                score = lader[score]
            if (score in snake.keys()):
                score = snake[score]
            print("Score", score)
        return score

    while (score1 < 100 and score2 < 100):
        user1 = input("User 1 Turn Press 1 to continue...")
        score1 = snakeLogic(score1)
        user2 = input("User 2 Turn Press 1 to continue...")
        score2 = snakeLogic(score2)

    print("Player1 score is ", score1)
    print("Player2 score is ", score2)
    if (score1 > score2):
        print("Player 1 is Winner")
    else:
        print("Player 2 is Winner")


def rock_paper_scissor():
    import random
    game_list = ['r', 'p', 's']
    a = random.choice(game_list)
    print(a)

    b = input("Enter anyone r,p or s--")
    for i in 1, 10:

        if (a == b):
            print("Draw")
            break
        elif (a == 'r' and b == 'p'):
            print(" You won!")
            break
        elif (a == 'p' and b == 'r'):
            print("you lost")
            break
        elif (a == 's' and b == 'p'):
            print("You lost")
            break
        elif (a == 'p' and b == 's'):
            print("You won")
            break
        elif (a == 'r' and b == 's'):
            print("you lost")
            break
        elif (a == 's' and b == 'r'):
            print("You won")
            break


print("Welcome ")
print("1.For add \n2. for Sub\n3. For snake and ladder\n4.For playing rock,paper and scissors")
c = int(input("Enter 1,2,3,4"))
if c == 1:
    add()
elif c == 2:
    minus()
elif c == 3:
    snake_ladder()
elif c == 4:
    rock_paper_scissor()


