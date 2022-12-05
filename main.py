from game_data import data
import random


account_a = random.choice(data)
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
    print("You're right!")
else:
    print("Sorry, that's wrong")

# TODO: Keep score
# TODO: 3 Place account B in place of account A and then take random new account as a choice B
# TODO: Add logos
# TODO: Make sure there can never be compared 2 accounts with the same number of followers


