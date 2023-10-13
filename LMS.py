import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
        self.borrowed_books = {}

    def displayAvailableBooks(self):
        return "\n".join(self.books)

    def borrowBook(self, bookname, student_name):
        if bookname in self.books:
            due_date = datetime.now() + timedelta(days=15)
            self.books.remove(bookname)
            self.borrowed_books[bookname] = {'student': student_name, 'due_date': due_date}
            return f"You have been issued {bookname}. Please return it by {due_date.strftime('%Y-%m-%d %H:%M:%S')}."
        else:
            return "Sorry, this book is either not available or already been issued to someone else."

    def returnBook(self, bookname, student_name):
        if bookname in self.borrowed_books and self.borrowed_books[bookname]['student'] == student_name:
            self.books.append(bookname)
            del self.borrowed_books[bookname]
            return "Thanks for returning this book."
        else:
            return "This book was not borrowed by you or does not exist in our records."

    def displayBorrowedBooks(self):
        return "\n".join([f"Book: {book}, Borrower: {info['student']}, Due Date: {info['due_date'].strftime('%Y-%m-%d %H:%M:%S')}" for book, info in self.borrowed_books.items()])

    def checkOverdueBooks(self):
        current_date = datetime.now()
        overdue_books = {book: info for book, info in self.borrowed_books.items() if info['due_date'] < current_date}
        return "\n".join([f"Book: {book}, Borrower: {info['student']}, Due Date: {info['due_date'].strftime('%Y-%m-%d %H:%M:%S')}" for book, info in overdue_books.items()])

    def addBook(self, bookname):
        self.books.append(bookname)
        return f"'{bookname}' has been added to the library."

class LibraryManagementApp:
    def __init__(self, root):
        self.centralLibrary = Library(["Science", "Python", "C Language"])
        self.root = root
        self.root.title("Library Management System")

        self.create_gui()

    def create_gui(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.label = tk.Label(self.main_frame, text="Central Library", font=("Helvetica", 20))
        self.label.pack()

        self.action_menu = tk.StringVar()
        self.action_menu.set("Select Action")

        self.action_dropdown = tk.OptionMenu(self.main_frame, self.action_menu, "Select Action", "Display available books", "Request a book", "Return a book", "Display borrowed books", "Check for overdue books", "Add a book to the library", "Exit the library")
        self.action_dropdown.pack()

        self.student_name_label = tk.Label(self.main_frame, text="Enter your name:")
        self.student_name_label.pack()
        self.student_name_entry = tk.Entry(self.main_frame)
        self.student_name_entry.pack()

        self.book_name_label = tk.Label(self.main_frame, text="Enter the name of the book:")
        self.book_name_label.pack()
        self.book_name_entry = tk.Entry(self.main_frame)
        self.book_name_entry.pack()

        self.result_text = tk.Text(self.main_frame, height=10, width=40)
        self.result_text.pack()

        self.action_button = tk.Button(self.main_frame, text="Perform Action", command=self.perform_action)
        self.action_button.pack()

    def perform_action(self):
        action = self.action_menu.get()
        student_name = self.student_name_entry.get()
        book_name = self.book_name_entry.get()

        if action == "Display available books":
            available_books = self.centralLibrary.displayAvailableBooks()
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, available_books)
        elif action == "Request a book":
            result = self.centralLibrary.borrowBook(book_name, student_name)
            messagebox.showinfo("Borrow Book", result)
        elif action == "Return a book":
            result = self.centralLibrary.returnBook(book_name, student_name)
            messagebox.showinfo("Return Book", result)
        elif action == "Display borrowed books":
            borrowed_books = self.centralLibrary.displayBorrowedBooks()
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, borrowed_books)
        elif action == "Check for overdue books":
            overdue_books = self.centralLibrary.checkOverdueBooks()
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, overdue_books)
        elif action == "Add a book to the library":
            result = self.centralLibrary.addBook(book_name)
            messagebox.showinfo("Add Book", result)
        elif action == "Exit the library":
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementApp(root)
    root.mainloop()
