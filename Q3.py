import json
def load_questions_from_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['questions']
def evaluate_quiz(questions):
    score = 0
    for question_info in questions:
        question_text = question_info['question']
        correct_answer = question_info['answer']
        user_response = input(f"{question_text} ")
        if user_response.strip().lower() == correct_answer.strip().lower():
            score += 1
    return score
def prompt_username():
    return input("Enter your name: ")
def record_user_score(username, score, file_path):
    with open(file_path, 'a') as file:
        file.write(f"{username},{score}\n")
def execute_quiz_program():
    quiz_file = 'Q.json'
    results_file = 'results.csv'
    questions = load_questions_from_file(quiz_file)
    score = evaluate_quiz(questions)
    username = prompt_username()
    record_user_score(username, score, results_file)
if __name__ == "__main__":
    execute_quiz_program()


