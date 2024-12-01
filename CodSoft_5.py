# Phase-2
# Project Title: Quiz Game

# Printed the title of the quiz game
print("-----------------------------------------------------------------------------------------------------------------------")
print("************ Welcome To The 10-10 Quiz Game **************")

# List of dictionaries, each containing a question and its correct answer
question_bank = [
    {"text": "1.The national animal of India is", "answer": "A"},
    {"text": "2.The national bird of India is", "answer": "C"},
    {"text": "3.The national fruit of India is", "answer": "C"},
    {"text": "4.The national tree of India is", "answer": "A"},
    {"text": "5.The national flower of India is", "answer": "B"},
    {"text": "6.Jana-Gana-Mana was originally composed in", "answer": "C"},
    {"text": "7.National River of India is", "answer": "C"},
    {"text": "8.National Currency of India is", "answer": "B"},
    {"text": "9.National Vegetable of India is", "answer": "A"},
    {"text": "10.What is the ratio of width of our national flag to its length?", "answer": "D"}
]

# List of possible answer options for each question
options = [
    ["A.Tiger", "B.Elephant", "C.Cow", "D.Lion"],  # Options for question 1
    ["A.Parrot", "B.Pigeon", "C.Peacock", "D.Sparrow"],  # Options for question 2
    ["A.Guava", "B.Apple", "C.Mango", "D.Pineapple"],  # Options for question 3
    ["A.Banyan", "B.Ashoka", "C.Eucalyptus", "D.Neem"],  # Options for question 4
    ["A.Rose", "B.Lotus", "C.Lily", "D.Jasmine"],  # Options for question 5
    ["A.Gujarati", "B.Hindi", "C.Bengali", "D.Marathi"],  # Options for question 6
    ["A.Yamuna", "B.Chenab", "C.Ganga", "D.Narmada"],  # Options for question 7
    ["A.Dollar", "B.Rupee", "C.Euro", "D.Yen"],  # Options for question 8
    ["A.Pumpkin", "B.Potato", "C.Tomato", "D.Carrot"],  # Options for question 9
    ["A.3:4", "B.1:4", "C.1:2", "D.2:3"]  # Options for question 10
]

# Initialized the user's score to 0
score = 0

# Defined a Function to check if the user's answer is correct


def check_answer(user_guess, correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False


# Ran a Loop through each question in the question bank
for question_num in range(len(question_bank)):
    # Printed a separator for clarity between questions
    print("\n--------------------------------------------------------------------------------------------------------------------------------")

    # Printed the current question text
    print(question_bank[question_num]["text"])

    # Printed the answer options for the current question
    for i in options[question_num]:
        print(i)

    # Prompted the user to input their guess (answer choice: A, B, C, or D)
    guess = input(
        "\nEnter your answer(A/B/C/D)>> ").upper()

    # Checked if the user's guess is correct
    is_correct = check_answer(guess, question_bank[question_num]["answer"])

    # If the guess is correct, increase the score and inform the user
    if is_correct:
        print("Correct Answer")
        score += 1
    else:
        # If the guess is incorrect, inform the user and show the correct answer
        print("Incorrect Answer")
        print(f"The correct answer is {question_bank[question_num]['answer']}")

    # Showed the user's current score after answering each question
    print(f"Your current score is {score}/{question_num+1}")

# After the quiz is over, print the total number of correct answers and the score percentage
print(f"You have given '{score}' correct answers")
print(f"Your score is {(score/len(question_bank))*100}%")
