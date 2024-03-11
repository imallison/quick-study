import csv
import random

def load_questions(file_name):
    questions = []
    with open(file_name, "r") as file_handler:
        csv_reader = csv.DictReader(file_handler)
        for row in csv_reader:
            question_answer = (row['Question'], row['Answer'])
            questions.append(question_answer)
    return questions

def quiz(questions):
    score = 0 # Numerator

    # Shuffle
    random.shuffle(questions)

    for question, correct_answer in questions:
        # Tuple from earlier
        print(question)

        user_input = input("Your answer: ").strip()
        if user_input.lower() == correct_answer.lower():
            print(f"Correct! Your score is currently {score}.")
            score += 1
        else:
            print(f"Incorrect! The correct answer was: {correct_answer}.")
        print()

    print(f"You've completed all the questions!\nScore: {score}/{len(questions)}")

if __name__ == "__main__":
    questions = load_questions(r"C:\-AL-\all projects\vs code projects\personal-projects\quick-study\qa.csv")
    quiz(questions)