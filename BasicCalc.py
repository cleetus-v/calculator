import tkinter as tk
from tkinter import messagebox
from tkmacosx import Button # Ensure you ran: pip install tkmacosx

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("450x550") # Bigger window to fit Mac buttons
        self.root.configure(bg="#1e1e1e") # Dark background
        self.root.resizable(False, False)

        self.equation = ""

        # 1. THE DISPLAY BOX (Row 0)
        self.display = tk.Entry(root, font=("Arial", 32), bg="#252526", 
                                fg="#ffffff", borderwidth=0, justify='right',
                                highlightthickness=0)
        self.display.grid(row=0, column=0, columnspan=4, padx=15, pady=30, sticky="nsew")

        # 2. BUTTON LIST
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        # 3. CREATE BUTTONS
        row_val = 1
        col_val = 0

        for button in buttons:
            # Logic to define b_color (fixes your error)
            if button == '=':
                b_color = "#007acc" # VS Code Blue
            elif button == 'C':
                b_color = "#d14836" # Red-ish for Clear
            else:
                b_color = "#333333" # Dark Grey for numbers

            action = lambda x=button: self.on_button_click(x)
            
            # Using tkmacosx Button with pixel-based width/height
            Button(root, text=button, width=75, height=75, borderless=1,
                   bg=b_color, fg="#ffffff", activebackground="#444444",
                   font=("Arial", 18, "bold"),
                   command=action).grid(row=row_val, column=col_val, padx=5, pady=5)
            
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.equation))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.equation = result
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.clear_screen()
        elif char == 'C':
            self.clear_screen()
        else:
            self.equation += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.equation)

    def clear_screen(self):
        self.equation = ""
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
