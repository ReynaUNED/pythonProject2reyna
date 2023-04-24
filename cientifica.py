import tkinter as tk # importamos las librerias necesarias
import csv #Una vez que el usuario haya seleccionado el archivo, puedes utilizar el módulo csv de Python
# para leer los datos del archivo de texto en una lista de vectores.

from tkinter import filedialog #para abrir un cuadro de diálogo de selección de
# archivo que permita al usuario seleccionar un archivo de texto.

root = tk.Tk()

def open_file(): # funcion para el boton de archivo  y seleccionar archivo
    file_path = filedialog.askopenfilename(filetypes=[('Archivo de texto', '*.txt')])
    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        vectors = [] #para leer datos del archivo
        for row in reader:
            vectors.append([float(x) for x in row])
        print(vectors)# imprime el vector

button = tk.Button(root, text='Seleccionar archivo', command=open_file)#boton para seleccionar
#archivo
button.pack()
def save_file(): #se utiliza un campo de texto (Text) de Tkinter para que el usuario
    # ingrese el contenido del archivo de texto que desea guardar.
    file_path = filedialog.asksaveasfilename(filetypes=[('Archivo de texto', '*.txt')])
    #Después de que el usuario ingrese el contenido y haga clic en el botón "Guardar archivo",
    # el código utiliza la funciónasksaveasfilenamedetkFileDialogpara abrir el cuadro de diálogo
    # de selección de archivo y permitir que el usuario especifique la ubicación y el nombre del
    # archivo.
    with open(file_path, 'w') as f:
        content = text_input.get('1.0', 'end') #Luego, el contenido del campo de texto se lee
        # utilizando el métodoget y se escribe en el archivo de texto utilizando el método write
        # de Python.
        f.write(content)

label = tk.Label(root, text='Ingrese el contenido del archivo:')
label.pack()

text_input = tk.Text(root)
text_input.pack()

button = tk.Button(root, text='Guardar archivo', command=save_file)

button.pack()

root.mainloop()



