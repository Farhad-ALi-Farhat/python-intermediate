import json

def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)

def run_quiz():
    questions = load_questions()
    score = 0

    for q in questions:
        answer = input(q["question"] + " ").lower()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print(f"\nYour score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
