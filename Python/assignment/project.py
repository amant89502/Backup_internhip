import random
snake = {32:10,36:6,48:26,62:18,88:24,95:56,97:78}
ladder = {1:38,4:14,8:30,21:42,28:76,50:67,71:92,80:99}
score = 0
ch = 'y'
while score <= 94 or ch != 'y':
    ch = input("Press y for continue").lower()
    b = random.randint(1, 6)
    score = score + b
    for i, j in ladder.items():
        if score == i:
            score = j
    for i, j in snake.items():
        if score == i:
            score = j

    print(score)
if score >= 94 and score >= 100:
    b = random.randint(1, 6)
    if score + b > 100:
        score = score
    else:
        score = score + b
        for i, j in ladder.items():
            if score == i:
                score = j
        for i, j in snake.items():
            if score == i:
                score = j








