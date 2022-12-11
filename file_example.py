
score = input("Enter your score : ")
def game(a):
    return a

s = int(game(score))
with open('score.txt') as f:
    h = f.read()
    

if int(h)<s:
    with open('score.txt', 'w') as f:
        f.write(str(s))
        print(f'Your score is highest : {s}')
elif int(h) == 0:
    with open('score.txt', 'w') as f:
        f.write(str(s))
        print(f'Your score is highest : {s}')
else:
    with open('score.txt') as f:
        f.read()
        print(f'You are reach the highest score : {s}')


