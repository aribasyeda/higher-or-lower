from random import choice
from game_data import data
from art import logo, vs
from replit import clear

def get_random_account(data):
  """Returns randomly chosen accounts from the given data."""
  return choice(data)

def format_data(account):
  """Format account data into printable format: name, description and country."""
  return f"{account['name']}, a {account['description']}, from {account['country']}"
  
def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "A"
  else:
    return guess == "B"

def gameplay():
  print("Welcome to...")
  score = 0
  game_over = False
  account_b = get_random_account(data)
  
  while not game_over:    
    account_a = account_b
    account_b = get_random_account(data)
    
    while account_a == account_b:
      account_b = get_random_account(data)
    
    print(f"""
    Compare A: {format_data(account_a)}.
    {vs}
    Against B: {format_data(account_b)}.
    """)
    
    guess = input("👉 Who has more followers? Type 'A' or 'B': \n").upper()
    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']
    is_correct = check_answer(guess, a_followers, b_followers)

    clear()
    print(logo)
  
    if is_correct:
      score += 1
      print(f"Correct 🥳 Your current score is {score}")
    else:
      game_over = True
      print(f"Wrong ❌ Your final score is {score}")

gameplay()
