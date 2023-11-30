import tkinter as tk
from tkinter import messagebox
import secrets
import time

class LotteryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lottery Program")
        self.root.geometry("400x300")
        self.num_names_var = tk.IntVar()
        self.elimination_var = tk.BooleanVar(value=False)
        tk.Label(self.root, text="Enter the number of names to draw:").pack()
        self.entry_num_names = tk.Entry(self.root, textvariable=self.num_names_var)
        self.entry_num_names.pack()
        tk.Checkbutton(self.root, text="Elimination", variable=self.elimination_var).pack()
        tk.Button(self.root, text="Create Name Input Boxes", command=self.create_name_input_boxes).pack()
        self.name_input_entries = []
        tk.Button(self.root, text="Start Lottery", command=self.start_lottery).pack()

    def create_name_input_boxes(self):
        for entry in self.name_input_entries:
            entry.destroy()
        self.name_input_entries.clear()
        num_names = self.num_names_var.get()
        for i in range(num_names):
            entry = tk.Entry(self.root, width=30)
            entry.pack()
            self.name_input_entries.append(entry)

    def start_lottery(self):
        names_list = [entry.get() for entry in self.name_input_entries]
        if len(names_list) < 2:
            messagebox.showerror("Error", "Please enter at least two names to draw.")
            return
        self.lottery_animation(names_list)

    def lottery_animation(self, names_list):
        secrets.SystemRandom().shuffle(names_list)
        previous_user_input = [entry.get() for entry in self.name_input_entries]
        for _ in range(20):
            if names_list:
                winner = names_list.pop()
                if self.elimination_var.get():
                    for entry in self.name_input_entries:
                        if entry.get() == winner:
                            entry.destroy()
                            self.name_input_entries.remove(entry)
                for entry in self.name_input_entries:
                    entry.delete(0, tk.END)
                    entry.insert(0, winner)
                self.root.update()
                time.sleep(0.1)
        messagebox.showinfo("Winner", f"The winner of the lottery is: {winner}")
        for i, entry in enumerate(self.name_input_entries):
            entry.delete(0, tk.END)
            entry.insert(0, previous_user_input[i])
            
if __name__ == "__main__":
    root = tk.Tk()
    app = LotteryApp(root)
    root.mainloop()