import json
import os

FILENAME="flashcard.json"


def load_flashcards():
  if os.path.exists(FILENAME):
    with open(FILENAME, "r") as file:
      return json.load(file)
  else:
    return {
        "What is the difference between a list and a tuple?": (
            "Lists are mutable (changeable), while tuples are immutable"
            " (unchangeable)."
        ),
        "What does the .strip() method do to a string?": (
            "It removes leading and trailing whitespace (spaces, tabs,"
            " newlines)."
        ),
        "How do you start a function definition in Python?": (
            "Using the def keyword followed by the function name and"
            " parentheses."
        ),
        "What is the purpose of try and except blocks?": (
            "To catch and handle errors gracefully so your program doesn't"
            " crash."
        ),
        "What is the file extension used for Python script files?": ".py",
    }


def save_flashcards(flashcards):
  with open(FILENAME, "w") as file:
    json.dump(flashcards, file, indent=4)
    print("\U0001F4BE Flashcard saved to WeberDeck! \u2705")


def add_flashcards(flashcards):
  print("\n ---ADD NEW FLASHCARD---")
  question = input("Enter a question: ")
  if not question:
    print("question cannot be blank")
    return
  answer = input("Enter answer: ")
  if not answer:
    print("answer cannot be blank")
    return

  flashcards[question] = answer
  save_flashcards(flashcards)


def study_deck(flashcards):
  if not flashcards:
    print("\n your flashcard deck is empty")
    return

  print("\n" + "=" * 30)
  print("---STUDY SESSION\U0001F4DA---")
  print("\n" + "=" * 30)
  score = 0
  total = len(flashcards)
  for question, answer in flashcards.items():
    print(f"\nQ: {question}")
    user_input = (
        input("press Enter to see answer (or type quit to quit): ")
        .strip()
        .lower()
    )
    if user_input == "quit":
      print("YOUR STUDY SESSION ENDED EARLY")
      break
    print(f"A: {answer}")
    learner_input = input("DID YOU GET IT Y/N? ").strip().upper()
    if learner_input == "Y":
      score += 1
  print(f"\nSESSION FINISHED! YOU GOT {score} out of {total} \U0001F389")


def main():
  flashcards = load_flashcards()
  print("---Welcome to WEBER DECK\U0001F680---")
  name = input("what is your name, student? ").strip()
  if name:
    print(f"welcome to WEBER DECK {name}")

  while True:
    print("\n\U0001F4CB Menu")
    print("1. Save Flashcards\U0001F4BE")
    print("2. Add Flashcards\U0001F4DD")
    print("3. Study Deck \U0001F4DA")
    print("4. Exit \U0001F44B")

    try:
      choice = int(input("choose an option: "))
    except ValueError:
      print("only numbers 1,2,3,4 are allowed")
      continue

    if choice == 1:
      save_flashcards(flashcards)
    elif choice == 2:
      add_flashcards(flashcards)
    elif choice == 3:
      study_deck(flashcards)
    elif choice == 4:
      print(
          f"\nCongratulations {name}! You finished the WeberDeck session!"
          " \U0001F389\U0001F3C6"
      )
      print("THANKS FOR USING WEBER DECK, WE HOPE IT HELPED! \U0001F44B")
      break
    else:
      print("Invalid option. Please choose between 1 and 4.")


if __name__ == "__main__":
  main()

    