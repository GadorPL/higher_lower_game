from game_data import data
from art import logo, vs
import random


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"


print(logo)
score = 0
account_a = random.choice(data)
game_over = False

while not game_over:
    account_b = random.choice(data)
    while account_a['follower_count'] == account_b['follower_count']:
        account_b = random.choice(data)

    print(f"Compare A: {account_a['name']}, {account_a['description']}, from {account_a['country']}.")
    print(vs)
    print(f"Compare B: {account_b['name']}, {account_b['description']}, from {account_b['country']}.")

    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    account_a_follower_count = account_a['follower_count']
    account_b_follower_count = account_b['follower_count']

    if check_answer(user_answer, account_a_follower_count, account_b_follower_count):
        score += 1
        print(f"\n\n\nYou're right! Current score: {score}\n\n")
        account_a = account_b
    else:
        print(f"\n\n\nSorry, that's wrong. Final score: {score}")
        game_over = True

