import tkinter as tk

class Calculator: #clase que implementa el patrón Singleton utilizando una variable de clase __instance.
    __instance = None #singlenton

    def __init__(self): #El método __init__ es responsable de crear
      # la ventana principal de la calculadora y definir los widgets que se van a utilizar.
        if Calculator.__instance is None:
            Calculator.__instance = self
            self.root = tk.Tk()
            self.root.title("Calculadora")

            self.result_var = tk.StringVar()
            self.result_var.set("0")
            self.result_label = tk.Label(self.root, textvariable=self.result_var, font=("Arial", 18), width=15, anchor="e")
            self.result_label.grid(row=0, column=0, columnspan=4)

            button_list = [
                ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
                ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
                ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
                ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("/", 4, 3)
            ]

            self.buttons = {}

            for button in button_list:
                text, row, col = button
                self.buttons[text] = tk.Button(self.root, text=text, font=("Arial", 16), width=3, height=2, command=lambda text=text: self.button_click(text))
                self.buttons[text].grid(row=row, column=col)

            self.root.mainloop()
        else:
            raise Exception("Cannot create multiple instances of Calculator. Please use Calculator.getInstance() instead.")

    @staticmethod
    def getInstance():#El método getInstance es el que implementa el patrón Singleton
      #Si no hay ninguna instancia de la clase creada, se crea una nueva
      #Si ya existe una instancia, se lanza una excepción indicando que no se pueden crear múltiples instancias.
        if Calculator.__instance is None:
            Calculator()
        return Calculator.__instance

    def button_click(self, text):#El método button_click se ejecuta cuando se hace clic en un botón de la calculadora.
        if text == "C":
            self.result_var.set("0")
        elif text == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except:
                self.result_var.set("Error")
        else:
            if self.result_var.get() == "0":
                self.result_var.set(text)
            else:
                self.result_var.set(self.result_var.get() + text)



if __name__ == "__main__":
    calc = Calculator.getInstance()
