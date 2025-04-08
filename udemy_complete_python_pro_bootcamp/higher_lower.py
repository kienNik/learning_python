from random import choice

instagram_follower = {
    'C.Ronaldo': 100,
    'L.Messi': 90,
    'Neymar Jr': 85,
    'L.Suarez': 80,
    'K.Mbappe': 83,
    'M.Salah': 81,
}

game_over = False
score = 0

while not game_over:
    if len(instagram_follower) == 0:
        print(f'Your score: {score}')
        break

    person1 = choice(list(instagram_follower.keys()))
    p1_follower = instagram_follower[person1]
    instagram_follower.pop(person1)
    person2 = choice(list(instagram_follower.keys()))
    p2_follower = instagram_follower[person2]
    instagram_follower.pop(person2)
    
    print(f'{person1} vs {person2}')
    answer = input('Higher or lower? h/l: ')
    if (answer == 'h' and p1_follower > p2_follower) or (answer == 'l' and p1_follower < p2_follower):
        score += 1
    else:
        print('Lose')
        print(f'Your score: {score}')
        game_over = True