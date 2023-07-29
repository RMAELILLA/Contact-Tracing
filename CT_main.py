import tkinter as tk
from tkinter import messagebox
from contact_info import ContactInfoFrame
from questions import QuestionsFrame
from questions2 import AdditionalQuestionsFrame

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("COVID Contact Tracing App")
        self.contact_info_frame = ContactInfoFrame(self, self.show_questions_frame)
        self.questions_frame = QuestionsFrame(self, self.show_contact_info_frame)
        self.additional_questions_frame = None

        self.contact_info_frame.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        self.questions_frame.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        self.questions_frame.grid_forget()
        
    def show_contact_info_frame(self):
        self.questions_frame.grid_forget()
        self.contact_info_frame.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

    def show_questions_frame(self):
        contact_info = self.contact_info_frame.get_contact_info()
        if contact_info:
            self.questions_frame.contact_info = contact_info
            self.contact_info_frame.grid_forget()
            self.show_next_question()
        else:
            tk.messagebox.showerror("Error", "Please fill in all contact details.")

    def show_next_question(self):
        if self.questions_frame.current_question < len(self.questions_frame.questions):
            self.questions_frame.grid()
            self.questions_frame.show_regular_question()
        else:
            self.display_contact_details()

    def show_additional_questions(self):
        answers = self.questions_frame.answers
        if len(answers) >= 3 and answers[2] == "Yes":
            if answers[3] == "Yes - Positive" or answers[4] == "Yes - Pending":
                self.additional_questions_frame = AdditionalQuestionsFrame(self, self.show_next_question)
                self.additional_questions_frame.set_contact_info(self.questions_frame.contact_info)
                self.additional_questions_frame.geometry("400x200")
                self.additional_questions_frame.title("Additional Questions")
            else:
                self.show_next_question()
        else:
            self.show_next_question()

    def display_contact_details(self):
        contact_info_message = "Contact Details:\n"
        for key, value in self.questions_frame.contact_info.items():
            contact_info_message += f"{key}: {value}\n"

        message = contact_info_message + "\nAnswers to Questions:\n"
        for i in range(len(self.questions_frame.questions)):
            message += f"{i + 1}. {self.questions_frame.questions[i]}\nAnswer: {self.questions_frame.answers[i]}\n"

        messagebox.showinfo("Contact Tracing Information", message)
        self.questions_frame.grid_forget()
        self.contact_info_frame.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        self.additional_questions_frame = None

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()