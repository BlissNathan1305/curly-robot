import random
import time

questions = [
    {
        "topic": "Math",
        "question": "What is 2 + 2?",
        "choices": ["3", "4", "5", "6"],
        "correct_answer": "4"
    },
    {
        "topic": "Science",
        "question": "What planet is known as the Red Planet?",
        "choices": ["Earth", "Mars", "Jupiter", "Saturn"],
        "correct_answer": "Mars"
    }
]

def run_quiz(questions, time_limit=10):
    score = 0
    total_questions = len(questions)
    random.shuffle(questions)
    for q in questions:
        print(f"\nTopic: {q['topic']}")
        print(q['question'])
        for i, choice in enumerate(q['choices'], 1):
            print(f"{i}. {choice}")
        start_time = time.time()
        while True:
            user_answer = input(f"\nYour answer (1-{len(q['choices'])}): ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(q['choices']):
                break
            print("Invalid input. Please enter a number.")
        if time.time() - start_time > time_limit:
            print("Time's up!")
        else:
            if q['choices'][int(user_answer)-1] == q['correct_answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Sorry, the correct answer was: {q['correct_answer']}")
        print(f"Time taken: {time.time() - start_time:.2f} seconds")
    print(f"\nQuiz complete! Your score: {score}/{total_questions}")

if __name__ == "__main__":
    run_quiz(questions)

