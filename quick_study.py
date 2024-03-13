import csv
import random

def load_questions(file_name):
    questions = []
    with open(file_name, "r") as file_handler:
        csv_reader = csv.DictReader(file_handler)
        for row in csv_reader:
            question_answer = (row['Question'], row['Option A'], row['Option B'], row['Option C'], row['Option D'], row['Answer'])
            questions.append(question_answer)
    return questions

def quiz(questions):
    score = 0 # Numerator

    # Shuffle
    random.shuffle(questions)

    for question, optionA, optionB, optionC, optionD, correct_answer in questions:
        # Tuple from earlier
        print(question)
        print(f"A. {optionA}")
        print(f"B. {optionB}")
        print(f"C. {optionC}")
        print(f"D. {optionD}\n")

        user_input = input("Your answer (input the letter only): ").strip()
        if user_input.lower() == correct_answer.lower():
            score += 1
            print(f"Correct! Your score is currently {score}.")
        else:
            print(f"Incorrect! Your score is currently {score}.\nThe correct answer was: {correct_answer}.")
        print()

    print(f"You've completed all the questions!\nScore: {score}/{len(questions)}")

if __name__ == "__main__":
    questions = load_questions(r"C:\-AL-\all projects\vs code projects\personal-projects\quick-study\questions.csv")
    quiz(questions)