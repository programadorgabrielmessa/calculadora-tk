import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        self.current_number = ""
        self.stored_number = None
        self.operation = None
        self.memory = 0

        # Criar o display
        display = tk.Label(master, textvariable=self.display_var, font=("Arial", 24), anchor="e", bg="white", relief="sunken", width=20)
        display.grid(row=0, column=0, columnspan=5, sticky="ew")

        # Criar frame para os botões
        button_frame = tk.Frame(master)
        button_frame.grid(row=1, column=0, columnspan=5)

        # Definir os textos dos botões
        button_texts = [
            ["MC", "MR", "M+", "M-", "C"],
            ["7", "8", "9", "÷", "√"],
            ["4", "5", "6", "×", "%"],
            ["1", "2", "3", "-", "CE"],
            ["0", ".", "+", "="]
        ]

        # Criar os botões
        for i in range(5):
            for j in range(5):
                if i == 4 and j == 0:
                    btn = tk.Button(button_frame, text="0", font=("Arial", 18), width=10, height=2, command=lambda: self.button_press("0"))
                    btn.grid(row=i, column=j, columnspan=2, sticky="ew")
                elif i == 4 and j == 1:
                    continue
                else:
                    text = button_texts[i][j] if i < 4 else button_texts[i][j-1 if j > 0 else 0]
                    btn = tk.Button(button_frame, text=text, font=("Arial", 18), width=5, height=2, command=lambda t=text: self.button_press(t))
                    btn.grid(row=i, column=j)

    def button_press(self, text):
        if text in "0123456789.":
            self.append_digit(text)
        elif text in "+-×÷":
            self.set_operation(text)
        elif text == "=":
            self.calculate()
        elif text == "C":
            self.clear_all()
        elif text == "CE":
            self.clear_entry()
        elif text == "√":
            self.square_root()
        elif text == "%":
            self.percentage()
        elif text in "M+ M- MR MC".split():
            self.memory_operation(text)

    def append_digit(self, digit):
        if digit == "." and "." in self.current_number:
            return
        if self.current_number == "0" and digit != ".":
            self.current_number = digit
        else:
            self.current_number += digit
        self.display_var.set(self.current_number)

    def set_operation(self, op):
        if self.current_number:
            self.stored_number = float(self.current_number)
            self.current_number = ""
        self.operation = op

    def calculate(self):
        if self.stored_number is not None and self.current_number:
            try:
                if self.operation == "+":
                    result = self.stored_number + float(self.current_number)
                elif self.operation == "-":
                    result = self.stored_number - float(self.current_number)
                elif self.operation == "×":
                    result = self.stored_number * float(self.current_number)
                elif self.operation == "÷":
                    result = self.stored_number / float(self.current_number)
                self.display_var.set(str(result))
                self.current_number = str(result)
                self.stored_number = None
                self.operation = None
            except ZeroDivisionError:
                self.display_var.set("Erro")
                self.current_number = ""
                self.stored_number = None
                self.operation = None

    def clear_all(self):
        self.current_number = ""
        self.stored_number = None
        self.operation = None
        self.display_var.set("0")

    def clear_entry(self):
        self.current_number = ""
        self.display_var.set("0")

    def square_root(self):
        if self.current_number:
            try:
                result = float(self.current_number) ** 0.5
                self.display_var.set(str(result))
                self.current_number = str(result)
            except ValueError:
                self.display_var.set("Erro")
                self.current_number = ""

    def percentage(self):
        if self.operation and self.stored_number is not None:
            percent = float(self.current_number) / 100 * self.stored_number
            self.current_number = str(percent)
            self.display_var.set(self.current_number)

    def memory_operation(self, op):
        if op == "M+" and self.current_number:
            self.memory += float(self.current_number)
        elif op == "M-" and self.current_number:
            self.memory -= float(self.current_number)
        elif op == "MR":
            self.current_number = str(self.memory)
            self.display_var.set(self.current_number)
        elif op == "MC":
            self.memory = 0

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculadora")
    calc = Calculadora(root)
    root.mainloop()