import tkinter as tk
from tkinter import messagebox

class AdditionalQuestionsFrame(tk.Frame):
    def __init__(self, master, contact_info, next_callback, back_callback):
        super().__init__(master)
        self.master = master
        self.contact_info = contact_info
        self.next_callback = next_callback
        self.back_callback = back_callback

        self.questions = [
            "When was your most recent visit to this location?",
            "Since then until today, what places have you been? (besides home)"
        ]

        self.answers = []
        self.current_question = 0

        self.question_label = tk.Label(self, text=self.questions[self.current_question])
        self.question_label.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        self.answer_entry = tk.Entry(self)
        self.answer_entry.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

        self.next_button = tk.Button(self, text="Next", command=self.save_answer)
        self.next_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def save_answer(self):
        answer = self.answer_entry.get()
        if answer:
            self.answers.append(answer)
            self.answer_entry.delete(0, tk.END)
            self.show_next_question()
        else:
            messagebox.showerror("Error", "Please enter an answer for the current question.")

    def show_next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.question_label.config(text=self.questions[self.current_question])
        else:
            self.display_contact_details()

    def display_contact_details(self):
        contact_info_message = "Contact Details:\n"
        for key, value in self.contact_info.items():
            contact_info_message += f"{key}: {value}\n"

        message = contact_info_message + "\nAnswers to Questions:\n"
        num_questions = len(self.questions)
        for i in range(num_questions):
            if i < len(self.answers):
                message += f"{i + 1}. {self.questions[i]}\nAnswer: {self.answers[i]}\n"

        messagebox.showinfo("Contact Tracing Information", message)
        self.back_callback()

        self.contact_info_completed = False
        self.contact_info = {}