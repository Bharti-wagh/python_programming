import json

# Step 1: Load questions from JSON file
def load_questions(filename="quiz.json"):
    with open(filename, "r") as file:
        data = json.load(file)
    return data["questions"]

# Step 2: Run the Quiz
def run_quiz(questions):
    score = 0
    for idx, q in enumerate(questions, start=1):
        print(f"\nQ{idx}: {q['question']}")
        
        # Show options
        for i, option in enumerate(q['options'], start=1):
            print(f"{i}. {option}")
        
        # Take user input
        choice = int(input("Enter option number: "))
        
        # Check Answer
        if q['options'][choice-1] == q['answer']:
            print(" Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")
    
    # Final Score
    print(f"\n Your Final Score: {score}/{len(questions)}")

# Step 3: Main Program
if __name__ == "__main__":
    questions = load_questions("quiz.json")
    run_quiz(questions)
