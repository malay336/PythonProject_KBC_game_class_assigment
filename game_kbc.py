import random
from questions import questions 
def kbc_game_no_lifelines():

  money_tree = [0, 1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 7000000, 10000000]
  current_money = 0

  def display_question(question):
      print(f"\nQuestion: {question['question']}")
      print("Options:")
      for i, option in enumerate(question['options']):
          print(f"{i+1}. {option}")

  def get_user_answer():
      while True:
          try:
              user_choice = int(input("Enter your answer (1-4): "))
              if 1 <= user_choice <= 4:
                  return user_choice
              else:
                  print("Invalid input. Please enter a number between 1 and 4.")
          except ValueError:
              print("Invalid input. Please enter a number.")

  def check_answer(user_choice, question):
      if question['options'][user_choice - 1] == question['answer']:
          print("Correct!")
          return True
      else:
          print("Incorrect!")
          return False

  # Shuffle the questions
  random.shuffle(questions)
  for i, question in enumerate(questions):
      display_question(question)

      user_answer = get_user_answer()
      if check_answer(user_answer, question):
          current_money = money_tree[i]
          print(f"Your current winnings: ₹{current_money}")
      else:
          print(f"You lose! Your final winnings: ₹{current_money}")
          break

  print("Game Over!")

if __name__ == "__main__":
  kbc_game_no_lifelines()