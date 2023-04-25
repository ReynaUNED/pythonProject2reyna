import tkinter as tk #importamos la interfaz grafica
import CuadroDeTexto# importamos la ventana del cuadro de texto



class Calculator:  # clase que implementa el patrón Singleton utilizando una variable de clase __instance.
    __instance = None  # singlenton

    def __init__(self):  # El método __init__ es responsable de crear
        # la ventana principal de la calculadora y definir los widgets que se van a utilizar.
        self.ventanaCalculadora = tk.Tk()
        self.ventanaCalculadora.title("Calculadora")

        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.result_label = tk.Label(self.ventanaCalculadora, textvariable=self.result_var, font=("Arial", 18),
                                     width=15, anchor="e")
        self.result_label.grid(row=0, column=0, columnspan=4)

        button_list = [# lista de botones de la calculadora y sus posiciones
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
            ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("/", 4, 3)
        ]

        self.buttons = {}

        for button in button_list:
            text, row, col = button
            self.buttons[text] = tk.Button(self.ventanaCalculadora, text=text, font=("Arial", 16), width=3, height=2,
                                           command=lambda text=text: self.button_click(text))
            self.buttons[text].grid(row=row, column=col)

        barramenu = tk.Menu(self.ventanaCalculadora) #menu principal
        menu = tk.Menu(barramenu, tearoff=0)
        barramenu.add_cascade(label="Herramientas", menu=menu) #opciones del menu
        menu.add_command(label="Cuadro de texto", command=CuadroDeTexto.CuadroTexto)#abre el cuadro de texto
        menu.add_separator()
        menu.add_command(label="Salir", command=self.ventanaCalculadora.quit)# opcion salir
        self.ventanaCalculadora.config(menu=barramenu)

        self.ventanaCalculadora.mainloop()

    def __new__(cls, *args, **kwargs): # metodo que indica si ya hay una instancia o ventana de la calculadora
        # si ya hubiera una ventana abierta , abre la misma con los datos que ya es ingresaron
        if not isinstance(cls.__instance, cls):
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def button_click(self,
                     text):  # El método button_click se ejecuta cuando se hace clic en un botón de la calculadora.
        if text == "C": #si se preciona el boton C el resultado sera cero ya que elimina los datos ingresados
            self.result_var.set("0")
        elif text == "=": # si preciona el igual arrojara el resultado
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


ventanaPrincipal = Calculator()

