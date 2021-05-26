import art,game_data
from replit import clear
import random as rnd


#print(game_data.data[0]['name'])
is_guessing = True
score = 0
print(art.logo)
# This is the data_length in order to random between those values
data_len = len(game_data.data)
print(data_len)
while is_guessing:
    random = rnd.randint(0,data_len-1)
    data_point = game_data.data[random]
    print(f"Compare A: {data_point['name']}, a {data_point['description']}, from {data_point['country']}.")
    # rank_a describe the total quantity of followers of guess a
    rank_a = data_point['follower_count']
    print(art.vs)
    random = rnd.randint(0,data_len-1)
    data_point = game_data.data[random]
    print(f"Against B: {data_point['name']}, a {data_point['description']}, from {data_point['country']}.")
    rank_b = data_point['follower_count']
    ans = input("Who has more followers? Type 'A' or 'B': ").lower()
    if ans == 'a':
        if rank_a > rank_b:
            score += 1
            clear()
            print(art.logo)
            print(f"You're right! current score: {score}.")
        elif rank_a < rank_b:
            clear()
            print(art.logo)
            print(f"Sorry, that's worng. Final score: {score}")
            is_guessing = False
    elif ans == 'b':
        if rank_b > rank_a:
            score += 1
            clear()
            print(art.logo)
            print(f"You're right! current score: {score}.")
        elif rank_b < rank_a:
            clear()
            print(art.logo)
            print(f"Sorry, that's worng. Final score: {score}")
            is_guessing = False