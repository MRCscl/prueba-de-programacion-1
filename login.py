import tkinter as tk
from Main import consulta

ventana = tk.Tk()
ventana.title("Datos")
ventana.geometry("1000x600")

panel = tk.Frame(
    ventana,
    bg="blue",
    padx=0,
        pady=0,
        width=1000,
        height=600,)
panel.pack()

entrada = tk.Entry(panel, bg="red",width=40)
entrada.pack(pady=5)

texto_resultado = tk.Text(panel,bg="yellow",height=15, width=60)
texto_resultado.pack()

def consultar():
    filtro = entrada.get()
    consulta_sql = f"SELECT * FROM alumnos WHERE Nombre = '{filtro}'"
    resultados = consulta(consulta_sql)

    texto_resultado.delete("1.0", tk.END)

    for fila in resultados:
        texto_resultado.insert(tk.END, str(fila) + "\n")

boton = tk.Button(panel, text="Consultar", command=consultar)
boton.pack(pady=5)

ventana.mainloop()