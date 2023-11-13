from guess_number_arts import developer, logo
from guess_number_methods import clear, check_answer, correct_input_value, correct_number_input, set_difficulty, random_number_creator 

end_of_game = False

while not end_of_game:
  clear()
  print(logo)
  game_levels_container = {"easy" : 10 , "hard" : 5}
  lower_bound = 1
  upper_bound = 100
  selected_number = random_number_creator(1, 100)
  print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between {lower_bound} and {upper_bound}.\nPssst, the correct answer is {selected_number}")
  difficulty = correct_input_value("Choose a difficulty. Type 'easy' or 'hard': ", "easy","hard")
  lives = set_difficulty(game_levels_container, difficulty)
  print(f"You have {lives} attempts remaining to guess the number.")
  end_of_guess = False

  while not end_of_guess:
    guess = correct_number_input("Make a guess: ")
    [lives, end_of_guess] = check_answer(selected_number, guess, lives, end_of_guess)
  reply_game = correct_input_value("Do you want to try it again? Type 'y' or 'n' ", "y", "n")
  if reply_game == 'n':
    end_of_game = True
    clear()
    print(logo + developer) 





