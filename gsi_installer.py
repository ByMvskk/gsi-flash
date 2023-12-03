import os
import threading
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


def instalar_gsi():
    platform_path = os.path.join(script_dir, "platform")
    comandos_path = os.path.join(platform_path, "cmds.txt")

    try:
        with open(comandos_path, 'r') as file:
            comandos = file.readlines()

        def ejecutar_comandos():

            for comando in comandos:
                comando = comando.strip()

                subprocess.run(["cmd", "/c", comando], cwd=platform_path)

        thread = threading.Thread(target=ejecutar_comandos)
        thread.start()

    except Exception as e:
        print(f"Error al leer los comandos de fastboot: {str(e)}")
        messagebox.showerror("Error", f"Error al leer los comandos de fastboot. Verifica el archivo 'cmds.txt'.")


def mostrar_ayuda():
    mensaje = "¡Bienvenido al GSI Flasher!\n\n" \
              "Este programa te permite instalar una GSI (Generic System Image) en tu dispositivo " \
              "utilizando comandos de fastboot.\n\n" \
              "Instrucciones:\n" \
              "1. Conecta tu dispositivo al modo fastboot.\n" \
              "2. Presiona el botón 'Instalar GSI' para iniciar el proceso de instalación.\n" \
              "3. Espera a que se complete la instalación y tu dispositivo se reinicie.\n\n" \
              "¡Nota: Utiliza este programa con precaución! La instalación de GSI puede " \
              "borrar datos y afectar el funcionamiento de tu dispositivo."

    messagebox.showinfo("Ayuda", mensaje)

ventana = tk.Tk()
ventana.title("GSI Flasher")

script_dir = os.path.dirname(os.path.abspath(__file__))

icono_path = os.path.join(script_dir, "src", "icono.ico")
if os.path.exists(icono_path):
    ventana.iconbitmap(default=icono_path)

imagen_path = os.path.join(script_dir, "src", "android14.png")
imagen = Image.open(imagen_path)
ancho_ventana = 1200
alto_ventana = 700
ancho_imagen = ancho_ventana - 40
alto_imagen = int(ancho_imagen / imagen.width * imagen.height)
imagen = imagen.resize((ancho_imagen, alto_imagen), Image.LANCZOS)
imagen = ImageTk.PhotoImage(imagen)

etiqueta = ttk.Label(ventana, text="Bienvenido al GSI Flasher!", font=("Helvetica", 24), borderwidth=5, relief="flat", anchor="center")
etiqueta_imagen = ttk.Label(ventana, image=imagen, borderwidth=5, relief="flat")
boton_instalar = ttk.Button(ventana, text="Instalar GSI", command=instalar_gsi, style="TButton", cursor="hand2")
etiqueta_desarrollado = ttk.Label(ventana, text="Developed by OnlyMysk", font=("Helvetica", 12), borderwidth=5, relief="flat")

etiqueta.pack(pady=20)
etiqueta_imagen.pack(pady=20, padx=20)
boton_instalar.pack(pady=20, padx=20)
etiqueta_desarrollado.pack(pady=20)

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 16), foreground="black", background="#3498db", width=20)

boton_instalar.bind("<Enter>", lambda e: style.configure("TButton", background="#2980b9"))
boton_instalar.bind("<Leave>", lambda e: style.configure("TButton", background="#3498db"))

menu_ayuda = tk.Menu(ventana)
ventana.config(menu=menu_ayuda)
menu_ayuda.add_command(label="Ayuda", command=mostrar_ayuda)

def cerrar_ventana():
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)
ventana.mainloop()
