import tkinter as tk
from tkinter import messagebox

questions = [
    {
        'question': "What does CPU stand for?",
        'options': ['Central Process Unit', 'Central Processing Unit', 'Computer Personal Unit', 'Control Program Unit'],
        'answer': 'Central Processing Unit'
    },
    {
        'question': "Which language is primarily used for Android development?",
        'options': ['Java', 'Swift', 'Kotlin', 'Python'],
        'answer': 'Kotlin'
    },
    {
        'question': "Which protocol is used to transfer web pages on the Internet?",
        'options': ['HTTP', 'FTP', 'SMTP', 'SSH'],
        'answer': 'HTTP'
    },
]

current_question_index = 0
user_answers = [None] * len(questions)
selected_option = None

root = tk.Tk()
root.title("Online quiz")
root.geometry("600x500")
root.configure(bg="white")

home_frame = tk.Frame(root, bg="white")
quiz_frame = tk.Frame(root, bg="white")
flashcard_frame = tk.Frame(root, bg="white")
review_frame = tk.Frame(root, bg="white")

def show_home():
    quiz_frame.pack_forget()
    flashcard_frame.pack_forget()
    review_frame.pack_forget()
    home_frame.pack(fill="both", expand=True)

home_label = tk.Label(home_frame, text="Choose quiz type", font=("Arial", 20), bg="white")
home_label.pack(pady=30)

tk.Button(home_frame, text="Manual Exam", width=25, command=lambda: start_quiz()).pack(pady=10)
tk.Button(home_frame, text="Flashcards Exam", width=25, command=lambda: start_flashcards()).pack(pady=10)

def start_quiz():
    global current_question_index
    current_question_index = 0
    home_frame.pack_forget()
    show_question()
    quiz_frame.pack(fill="both", expand=True)

def show_question():
    global selected_option
    for widget in quiz_frame.winfo_children():
        widget.destroy()

    q = questions[current_question_index]
    selected_option = tk.StringVar(value=user_answers[current_question_index])

    tk.Label(quiz_frame, text=f"Q{current_question_index+1}: {q['question']}", wraplength=500,
             font=("Arial", 14), bg="white").pack(pady=20)

    for option in q['options']:
        tk.Radiobutton(
            quiz_frame, text=option, variable=selected_option, value=option,
            font=("Arial", 12), bg="white", selectcolor='lightblue', indicatoron=0,
            width=30, pady=5
        ).pack(pady=2)

    nav_frame = tk.Frame(quiz_frame, bg="white")
    nav_frame.pack(pady=20)

    if current_question_index > 0:
        tk.Button(nav_frame, text="Previous", command=go_previous).pack(side="left", padx=10)
    if current_question_index < len(questions) - 1:
        tk.Button(nav_frame, text="Next", command=go_next).pack(side="left", padx=10)
    else:
        tk.Button(nav_frame, text="Submit", command=submit_quiz).pack(side="left", padx=10)

def go_next():
    global current_question_index
    user_answers[current_question_index] = selected_option.get()
    current_question_index += 1
    show_question()

def go_previous():
    global current_question_index
    user_answers[current_question_index] = selected_option.get()
    current_question_index -= 1
    show_question()

def submit_quiz():
    user_answers[current_question_index] = selected_option.get()
    quiz_frame.pack_forget()
    show_review()

def show_review():
    review_frame.pack(fill="both", expand=True)
    for widget in review_frame.winfo_children():
        widget.destroy()

    tk.Label(review_frame, text="Review Answers", font=("Arial", 18), bg="white").pack(pady=20)

    for idx, q in enumerate(questions):
        frame = tk.Frame(review_frame, bg="white", pady=5)
        frame.pack(fill="x", padx=20)

        tk.Label(frame, text=f"Q{idx+1}: {q['question']}", font=("Arial", 12), wraplength=500, bg="white").pack(anchor="w")

        for option in q['options']:
            color = "white"
            if option == q['answer']:
                color = "#d4edda"
            if user_answers[idx] == option and option != q['answer']:
                color = "#f8d7da"
            tk.Label(frame, text=option, font=("Arial", 11), bg=color, anchor="w", width=50, padx=10).pack(anchor="w")

    tk.Button(review_frame, text="Back to Home", command=show_home).pack(pady=20)

def start_flashcards():
    global current_question_index
    current_question_index = 0
    home_frame.pack_forget()
    show_flashcard()
    flashcard_frame.pack(fill="both", expand=True)

def show_flashcard():
    for widget in flashcard_frame.winfo_children():
        widget.destroy()

    q = questions[current_question_index]
    selected = tk.StringVar()

    tk.Label(flashcard_frame, text=f"Flashcard {current_question_index+1}", font=("Arial", 16), bg="white").pack(pady=10)
    tk.Label(flashcard_frame, text=q['question'], wraplength=500, font=("Arial", 14), bg="white").pack(pady=10)

    for option in q['options']:
        tk.Radiobutton(flashcard_frame, text=option, variable=selected, value=option,
                       font=("Arial", 12), bg='white', selectcolor='lightblue', indicatoron=0,
                       width=30, pady=5).pack(pady=2)

    feedback_label = tk.Label(flashcard_frame, text="", font=("Arial", 14), bg='white')
    feedback_label.pack(pady=10)

    def flip_card():
        answer = questions[current_question_index]['answer']
        feedback_label.config(text=f"✅ Correct Answer: {answer}", fg='green')

    tk.Button(flashcard_frame, text="Flip Card", command=flip_card).pack(pady=10)

    nav_frame = tk.Frame(flashcard_frame, bg='white')
    nav_frame.pack(pady=20)

    if current_question_index > 0:
        tk.Button(nav_frame, text="Previous", command=flash_prev).pack(side="left", padx=10)
    if current_question_index < len(questions) - 1:
        tk.Button(nav_frame, text="Next", command=flash_next).pack(side="left", padx=10)
    else:
        tk.Button(nav_frame, text="Back to Home", command=show_home).pack(side="left", padx=10)

def flash_next():
    global current_question_index
    current_question_index += 1
    show_flashcard()

def flash_prev():
    global current_question_index
    current_question_index -= 1
    show_flashcard()

show_home()
root.mainloop()
