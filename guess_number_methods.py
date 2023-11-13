import os, platform, random

def clear():
  '''Clear IDE based on OS system'''
  return os.system("clear") if platform.system() == "Linux" else os.system("cls") 

def correct_input_value(message, lunch_choice1, lunch_choice2):
  '''Take the message and choices and compare if the input was 
     not equal to the choices ask to enter the correct input'''
  user_input =input(message).lower()
  while user_input not in (lunch_choice1, lunch_choice2):
    user_input =input(f"Wrong input. {message}").lower()
  return user_input

def random_number_creator(lower_bound, upper_bound):
  '''Take lower_bound and upper_bound an return a random number between these ranges'''
  return random.randint(lower_bound,upper_bound)

def set_difficulty(game_levels, selected_level):
  '''Take dictionary of game levels and selected level and return value of key'''
  return game_levels.get(selected_level, "None")

def is_float(string):
  '''detect string is a float number or not and return it in boolean'''
  try:
    float(string)
    return True
  except ValueError:
    return False

def correct_number_input(message):
  '''Take the message of operator and user input and ask user to enter input until the input becomes a number'''
  number = input(message)
  while not(number.isnumeric()):
    number = input(f"Wrong guess, {message}")
  return int(number)

def check_answer(answer, guessed_number, lives, end_of_guess):
  '''Take selected number, guessed number and print the result of guessing'''
  lives -=1
  end_of_guess = False
  if lives == 0: 
    end_of_guess = True
    print("You lose 😭")
  elif guessed_number == answer:
    end_of_guess = True
    print(f"You got it! The answer was {answer}. 😎")
  elif guessed_number < answer or guessed_number > answer:
    print("Too low.") if guessed_number < answer else print("Too high.")
    print("Guess again.")
    print(f"You have {lives} attempts remaining to guess the number.")
  return [lives, end_of_guess]
