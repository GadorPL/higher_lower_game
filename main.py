from game_data import data
import random

account_a = random.choice(data)
account_b = random.choice(data)
print(f"Compare A: {account_a['name']}, {account_a['description']}, from {account_a['country']}.")
print(f"Compare B: {account_b['name']}, {account_b['description']}, from {account_b['country']}.")

# TODO: 2 Compare logic
# TODO: 3 Place account B in place of account A and then take random new account as a choice B
# TODO: Add logos


