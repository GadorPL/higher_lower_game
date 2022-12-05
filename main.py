from game_data import data
import random

score = 0
account_a = random.choice(data)
game_over = False

while not game_over:
    account_b = random.choice(data)
    print(f"Compare A: {account_a['name']}, {account_a['description']}, from {account_a['country']}.")
    print(f"Compare B: {account_b['name']}, {account_b['description']}, from {account_b['country']}.")

    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    account_a_follower_count = account_a['follower_count']
    account_b_follower_count = account_b['follower_count']

    if account_a_follower_count > account_b_follower_count:
        correct_answer = 'A'
    else:
        correct_answer = 'B'

    if correct_answer == user_answer:
        score += 1
        print(f"You're right! Current score: {score}")
        account_a = account_b
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True


# TODO: Add logos
# TODO: Make sure there can never be compared 2 accounts with the same number of followers
