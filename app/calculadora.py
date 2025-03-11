import tkinter as tk
from functools import partial

class Calculadora:
    def __init__(self, master):
        self.master = master
        self.master.title('Calculadora Tk')
        self.master.geometry('300x400')
        self.master.resizable(FALSE, FALSE)

        # Dark theme colors
        self.bg_color = '#212121'
        self.btn_color = '#333333'
        self.text_color = '#FFFFFF'
        self.highlight_color = '#FF5722'

        # Configuring the layout
        self.master.configure(bg=self.bg_color)

        # Input display (large, right-aligned)
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.display = tk.Entry(self.master, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, 
                                bg=self.bg_color, fg=self.text_color, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10)

        # Button layout
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('C', 1, 0), ('(', 1, 1), (')', 1, 2), ('<', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('.', 5, 0), ('0', 5, 1), ('=', 5, 2), ('/', 5, 3),
            ('^', 6, 2), ('√', 6, 3)
        ]

        for (text, row, col) in buttons:
            action = partial(self.on_button_click, text)
            tk.Button(self.master, text=text, command=action, height=3, width=6, 
                      bg=self.btn_color, fg=self.text_color, font=('Arial', 18)).grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set("0")
        elif char == '=':
            try:
                expression = self.result_var.get()
                result = eval(expression)
                self.result_var.set(str(result))
            except:
                self.result_var.set("Error")
        elif char == '<':
            current_text = self.result_var.get()
            self.result_var.set(current_text[:-1])
        else:
            current_text = self.result_var.get()
            if current_text == '0':
                self.result_var.set(char)
            else:
                self.result_var.set(current_text + char)

if __name__ == '__main__':
    root = tk.Tk()
    app = Calculadora(master=root)
    root.mainloop()
