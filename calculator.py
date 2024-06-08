import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.expression = ""

        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.total_expression = tk.StringVar()
        self.label = self.create_display_label()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), ".": (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def create_display_frame(self):
        frame = tk.Frame(self.root, height=100, bg="lightgrey")
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_label(self):
        label = tk.Label(
            self.display_frame, textvariable=self.total_expression, anchor=tk.E, bg="lightgrey", fg="black", padx=24, font=("Arial", 24)
        )
        label.pack(expand=True, fill="both")
        return label

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(
                self.buttons_frame, text=str(digit), bg="white", fg="black", font=("Arial", 18), borderwidth=0, command=lambda x=digit: self.add_to_expression(x)
            )
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(
                self.buttons_frame, text=symbol, bg="lightblue", fg="black", font=("Arial", 18), borderwidth=0, command=lambda x=operator: self.append_operator(x)
            )
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_special_buttons(self):
        self.clear_button = tk.Button(
            self.buttons_frame, text="C", bg="lightgreen", fg="black", font=("Arial", 18), borderwidth=0, command=self.clear
        )
        self.clear_button.grid(row=0, column=1, sticky=tk.NSEW, columnspan=2)

        self.equals_button = tk.Button(
            self.buttons_frame, text="=", bg="orange", fg="black", font=("Arial", 18), borderwidth=0, command=self.evaluate
        )
        self.equals_button.grid(row=4, column=3, sticky=tk.NSEW, columnspan=2)

    def add_to_expression(self, value):
        self.expression += str(value)
        self.total_expression.set(self.expression)

    def append_operator(self, operator):
        self.expression += operator
        self.total_expression.set(self.expression)

    def clear(self):
        self.expression = ""
        self.total_expression.set(self.expression)

    def evaluate(self):
        try:
            self.expression = str(eval(self.expression))
            self.total_expression.set(self.expression)
        except Exception as e:
            self.total_expression.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    for i in range(1, 5):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)
    root.mainloop()
