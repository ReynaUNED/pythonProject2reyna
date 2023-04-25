import tkinter as tk # importamos las librerias necesarias
import csv #Una vez que el usuario haya seleccionado el archivo, puedes utilizar el módulo csv de Python
# para leer los datos del archivo de texto en una lista de vectores.

from tkinter import filedialog #para abrir un cuadro de diálogo de selección de
# archivo que permita al usuario seleccionar un archivo de texto.


class CuadroTexto(): #clase para el cuadro de texto
    def __init__(self):

        self.ventanaTexto = tk.Tk()
        self.button = tk.Button(self.ventanaTexto, text='Seleccionar archivo', command=self.open_file)#boton para seleccionar

        #archivo
        self.button.pack()

        self.label = tk.Label(self.ventanaTexto, text='Ingrese el contenido del archivo:')#se ingresa el texto
        self.label.pack()

        self.text_input = tk.Text(self.ventanaTexto)
        self.text_input.pack()

        self.button = tk.Button(self.ventanaTexto, text='Guardar archivo', command=self.save_file)#boton para guardar

        self.button.pack()

        self.ventanaTexto.mainloop()


    def open_file(self): # funcion para el boton de archivo  y seleccionar archivo
        file_path = filedialog.askopenfilename(filetypes=[('Archivo de texto', '*.txt')])
        with open(file_path, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            vectors = [] #para leer datos del archivo
            for row in reader:
                vectors.append([x for x in row])
            self.text_input.delete('1.0', tk.END)
            self.text_input.insert(tk.END, vectors) # imprime el vector


    def save_file(self): #se utiliza un campo de texto (Text) de Tkinter para que el usuario
        # ingrese el contenido del archivo de texto que desea guardar.
        file_path = filedialog.asksaveasfilename(filetypes=[('Archivo de texto', '*.txt')])
        #Después de que el usuario ingrese el contenido y haga clic en el botón "Guardar archivo",
        # el código utiliza la funciónasksaveasfilenamedetkFileDialogpara abrir el cuadro de diálogo
        # de selección de archivo y permitir que el usuario especifique la ubicación y el nombre del
        # archivo.
        with open(file_path, 'w') as f:
            content = self.text_input.get('1.0', 'end') #Luego, el contenido del campo de texto se lee
            # utilizando el métodoget y se escribe en el archivo de texto utilizando el método write
            # de Python.
            f.write(content)





