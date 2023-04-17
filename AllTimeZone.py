import tkinter as tk
import pytz
from datetime import datetime
from tkinter import filedialog

# Obtener la hora de todos los países
def obtener_hora_mundial():
    lista_paises.delete(1.0, tk.END)  # Borrar contenido anterior
    for pais in pytz.all_timezones:
        tz = pytz.timezone(pais)
        hora_local = datetime.now(tz)
        hora = hora_local.strftime('%Y-%m-%d %H:%M:%S %Z')
        lista_paises.insert(tk.END, f'{pais}: {hora}\n')

# Exportar la lista de países y horas a un archivo de texto
def exportar():
    contenido = lista_paises.get(1.0, tk.END)
    archivo = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[('Archivo de texto', '*.txt')],
                                      title='Guardar como')
    if archivo is not None:
        archivo.write(contenido)
        archivo.close()

# Configurar la ventana principal
ventana = tk.Tk()
ventana.title('Hora Mundial')
ventana.geometry('400x400')

# Lista de países
lista_paises = tk.Text(ventana, height=20, width=50)
lista_paises.pack(pady=10)

#Añadimos una barra de desplazamiento deslizable horizontal y vertical a la lista de países
scrollbar = tk.Scrollbar(ventana, orient=tk.VERTICAL, command=lista_paises.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
lista_paises.config(yscrollcommand=scrollbar.set)


# Botón de actualización
boton_actualizar = tk.Button(ventana, text='GO', command=obtener_hora_mundial)
boton_actualizar.pack()

# Botón de exportación
boton_exportar = tk.Button(ventana, text='Exportar', command=exportar)
boton_exportar.pack()

ventana.mainloop()
