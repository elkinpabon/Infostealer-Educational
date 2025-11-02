# 🎓 Infostealer Educational - Análisis de Ciberseguridad

## 📝 Descripción General

**Infostealer Educational** es un proyecto educativo en Python que demuestra técnicas de análisis de seguridad y comportamiento de malware infostealer. Diseñado para laboratorios de ciberseguridad, permite estudiar y comprender cómo funcionan herramientas maliciosas reales.

### 📦 Componentes del Proyecto:

1. **Script Python** (`monitor_usb.py`)
   - Código fuente educativo
   - Se ejecuta con intérprete Python
   - Debes editar el archivo para cambiar la carpeta destino: `DESTINO = r"C:\Users\<TU_USUARIO>\..."`
   - Comando: `python monitor_usb.py`

2. **Programa Compilado** (`svchost.exe`)
   - Ejecutable binario independiente
   - No requiere Python instalado
   - La carpeta destino se define antes de compilar
   - Comando: `.\svchost.exe`

### ⚠️ ADVERTENCIA - FINES EDUCATIVOS ÚNICAMENTE
Este proyecto es **ÚNICAMENTE** para:
- Investigación académica en ciberseguridad
- Análisis forense en laboratorios controlados
- Educación en defensa contra malware
- Pruebas autorizadas en sistemas propios

### Características de Análisis:
- ✅ Monitoreo de dispositivos de almacenamiento externo
- ✅ Captura de datos para análisis forense
- ✅ Replicación de técnicas de infostealer
- ✅ Análisis de patrones de exfiltración
- ✅ Generación de reportes de actividad
- ✅ Estudio de evasión de detección
- ✅ Análisis de comportamiento oculto

---

## 🖥️ Requisitos del Sistema

### Requisitos de Laboratorio:
- **Entorno**: Máquina virtual aislada (VirtualBox, VMware, Hyper-V)
- **Red**: Desconectada de internet público
- **Aislamiento**: Sistema dedicado para análisis

### Hardware Mínimo:
- Procesador: Intel Core 2 Duo o equivalente
- RAM: 512 MB mínimo
- Disco duro: 100 MB libres
- Puertos USB 2.0 o superior

### Sistema Operativo:
- Windows 7, 8, 10, 11 (32 o 64 bits) en entorno de laboratorio
- Python 3.6 o superior

### Ambiente Seguro Recomendado:
- Máquina virtual con snapshot/punto de restauración
- Sistema operativo limpio antes de pruebas
- Sin acceso a datos personales reales
- Monitoreo con herramientas forenses (Wireshark, Process Monitor)

---

## 🔧 Instalación Paso a Paso

### Paso 1: Verificar Python Instalado

```powershell
python --version
```

**Resultado esperado**: `Python 3.x.x`

Si no está instalado, descargar desde https://www.python.org/

### Paso 2: Descargar o Crear el Programa

Crear carpeta para el proyecto:

```powershell
mkdir C:\Users\<TU_USUARIO>\Desktop\monitorUSB
cd C:\Users\<TU_USUARIO>\Desktop\monitorUSB
```

**Nota**: Reemplaza `<TU_USUARIO>` con tu nombre de usuario de Windows (ej: `elkin`, `admin`, etc.)

Copiar el archivo `monitor_usb.py` en esa carpeta.

### Paso 3: Instalar Dependencias

Abrir PowerShell y ejecutar:

```powershell
pip install pywin32
pip install pyinstaller
```

**Verificar instalación:**

```powershell
pip list | findstr pywin32
pip list | findstr pyinstaller
```

### Paso 4: Verificar Carpeta Destino

El script Python copia archivos a:
```
C:\Users\<TU_USUARIO>\Desktop\<CARPETA_DESTINO>
```

**Crear la carpeta si no existe:**

```powershell
New-Item -ItemType Directory -Path "C:\Users\<TU_USUARIO>\Desktop\<CARPETA_DESTINO>" -Force
```

**Nota**: Reemplaza:
- `<TU_USUARIO>` con tu nombre de usuario (ej: `elkin`)
- `<CARPETA_DESTINO>` con donde quieras guardar los archivos copiados (ej: `ESPE/test`, `Documentos/USB_Backup`)

---

## 🚀 Uso del Proyecto (Laboratorio Educativo)

### Opción A: Ejecutar el Script Python

```powershell
cd C:\Users\<TU_USUARIO>\Desktop\monitorUSB
python monitor_usb.py
```

**Ventajas:**
- Código fuente visible
- Modificable para aprender
- Requiere Python 3.6+

**Nota**: Reemplaza `<TU_USUARIO>` con tu nombre de usuario de Windows

### Opción B: Ejecutar el Programa Compilado

```powershell
cd C:\Users\<TU_USUARIO>\Desktop\monitorUSB
python monitor_usb.py --compile
# Luego ejecutar:
.\svchost.exe
```

**Ventajas:**
- Ejecutable independiente
- No requiere Python
- Simula malware real compilado

**Nota**: Reemplaza `<TU_USUARIO>` con tu nombre de usuario de Windows

### ⚠️ REQUISITOS LEGALES
Antes de usar este proyecto, debes:
1. ✅ Contar con autorización escrita del propietario del sistema
2. ✅ Estar en un ambiente de laboratorio controlado
3. ✅ Cumplir con leyes de ciberseguridad locales
4. ✅ Reportar hallazgos responsablemente
5. ✅ No usar para fines maliciosos

### Ejecución del Script Python

```powershell
cd C:\Users\<TU_USUARIO>\Desktop\monitorUSB
python monitor_usb.py
```

**Objetivo educativo:**
- Observar código fuente en ejecución
- Monitorear comportamiento del programa
- Capturar actividad de red/disco
- Analizar patrones de exfiltración

### Ejecución del Programa Compilado

```powershell
.\svchost.exe
```

**Objetivo de análisis:**
- Estudiar técnicas de ofuscación
- Analizar ejecutable compilado
- Comparar con malware real
- Entender evasión de detección

Los reportes generados (`reporte_usb.md`) son **estudios de caso** que muestran:
- Patrones de movimiento de archivos
- Tipos de datos exfiltrados
- Velocidad de transferencia
- Evasión de detección

---

## 🛠️ Herramientas y Características Detalladas

### 📚 CONTEXTO EDUCATIVO
Cada característica demuestra técnicas reales de malware:

### 1. **Monitoreo de Dispositivos USB**

**Técnica maliciosa replicada:**
- Detección pasiva de dispositivos conectados
- Identificación de letras de unidad dinámicamente
- **Defensa**: Monitoreo de eventos de conexión USB en Windows

### 2. **Copia Silenciosa de Archivos**

**Técnicas estudiadas:**
- Preservación de estructura (exfiltración inteligente)
- Orden de priorización (archivos críticos primero)
- Manejo de errores (robustez del programa)
- **Defensa**: Monitoreo de I/O de disco, DLP

### 3. **Análisis de Archivos**

**Recolección de información:**
- Catalogación de tipos de archivo
- Cálculo de tamaño y metadatos
- **Defensa**: Auditoría de acceso a archivos

### 4. **Generación de Reportes Ocultos**

**Técnicas de persistencia:**
- Logs en formato Markdown (difícil de detectar)
- Registros detallados de actividad
- **Defensa**: Monitoreo de creación de archivos

### 5. **Logging Silencioso**

**Métodos de evasión:**
- Registro sin interfaz visible
- Datos históricos para análisis
- **Defensa**: Monitoreo de integridad de archivos

### 6. **Manejo Robusto de Excepciones**

**Técnicas de resiliencia:**
- Continúa ante errores de permisos
- Adaptación a entornos variados
- **Defensa**: Sandboxing, aislamiento

### 7. **Formateo de Datos**

**Técnicas de ofuscación:**
- Conversión de tamaños (confusión)
- Estrutura legible para humanos
- **Defensa**: Análisis de datos exfiltrados

---

## 📊 Generación de Reporte

### Ubicación del Reporte

```
C:\Users\<TU_USUARIO>\Desktop\<CARPETA_DESTINO>\reporte_usb.md
```

**Ejemplos:**
```
C:\Users\elkin\Desktop\monitorUSB\archivos\reporte_usb.md
C:\Users\Maria\Documents\Copias\reporte_usb.md
D:\Backups\USB_Archivos\reporte_usb.md
```

**Nota**: El reporte se crea automáticamente con el mismo destino que configuraste

### Ejemplo de Contenido del Reporte

```markdown
# Reporte de Copia USB - 2025-11-02_14-30-45

## Información General
- **Unidad USB**: D:\
- **Directorio Destino**: C:\Users\Elkin Andres\Desktop\ESPE\test
- **Fecha y Hora**: 02/11/2025 14:30:45

## Estadísticas de Copia
- **Total de Archivos**: 1250
- **Total de Carpetas**: 45
- **Archivos Copiados**: 1248
- **Errores**: 2
- **Tamaño Total**: 2.50 GB

## Distribución por Tipo de Archivo
| Tipo | Cantidad | Tamaño |
|------|----------|--------|
| .pdf | 45 | 125.30 MB |
| .docx | 230 | 450.25 MB |
| .jpg | 512 | 1.20 GB |
| .mp4 | 15 | 650.50 MB |
| .xlsx | 89 | 120.75 MB |

## Estructura del USB
```
Documents/Reportes/2024/Enero/reporte.pdf
Documents/Reportes/2024/Febrero/reporte.pdf
...
```

---

## 💾 Compilación a Ejecutable (Análisis de Evasión)

### 🎓 OBJETIVO EDUCATIVO

Demuestra técnicas reales de evasión que usan los desarrolladores de malware:
- Ofuscación de código fuente
- Disfraz de proceso legítimo
- Evasión de detección por antivirus
- Empaquetamiento de código

### Diferencia Script vs Programa Compilado:

| Aspecto | Script Python | Programa Compilado |
|--------|---------------|-------------------|
| **Código** | Visible y legible | Ofuscado/binario |
| **Ejecución** | Requiere `python.exe` | Directo |
| **Modificación** | Fácil (texto) | Difícil (binario) |
| **Detección** | Claro qué es | Puede parecer legítimo |
| **Tamaño** | Pequeño (~5 KB) | Más grande (~40 MB) |

### Paso 1: Compilar el Script a Programa

```powershell
cd C:\Users\<TU_USUARIO>\Desktop\monitorUSB
python monitor_usb.py --compile
```

**Tiempo estimado**: 2-5 minutos

**Nota**: Reemplaza `<TU_USUARIO>` con tu nombre de usuario de Windows

**Monitorear durante compilación:**
```powershell
# En otra terminal, capturar actividad
Get-Process | Export-Csv -Path "procesos_antes.csv"
# Luego de compilar:
Get-Process | Export-Csv -Path "procesos_despues.csv"
```

### Paso 2: Análisis del Ejecutable Compilado

```powershell
# Obtener propiedades del archivo compilado
Get-Item -Path "svchost.exe" | Select-Object *

# Calcular hash (verificar integridad)
Get-FileHash -Path "svchost.exe" -Algorithm SHA256

# Comparar tamaño
ls -l monitor_usb.py
ls -l svchost.exe
```

### Paso 3: Análisis Forense del Programa

Características observables para análisis:

✅ **Técnicas de Evasión Analizadas**
- Nombre falso: `svchost.exe` (similar a proceso legítimo)
- Icono copiado: De Windows (shell32.dll)
- Sin consola visible
- Sin indicios obvios de Python en el código

✅ **Comparación de Comportamiento**
- Script: `python.exe` visible en Task Manager
- Programa: `svchost.exe` (proceso aparentemente legítimo)

✅ **Análisis Dinámico Recomendado**
- Ejecutar en sandbox (Cuckoo, Any.run)
- Capturar tráfico de red (Wireshark)
- Monitorear sistema de archivos (ProcMon)
- Analizar comportamiento (API Calls)

### Paso 4: Laboratorio de Defensa

**Cómo detectar este programa compilado:**

```powershell
# Buscar procesos sospechosos (Script vs Programa)
Get-Process python    # Script Python
Get-Process svchost   # Programa compilado

# Ver diferencias en línea de comandos
Get-Process | Where-Object {$_.ProcessName -eq "svchost"} | Select-Object *

# Analizar cambios en sistema de archivos
Compare-Object (ls "C:\test" -Force) (ls "C:\test" -Force -ErrorAction SilentlyContinue)
```

---

## 🔍 Solución de Problemas

### Problema 1: "ModuleNotFoundError: No module named 'win32api'"

**Solución:**
```powershell
pip install --upgrade pywin32
python -m pip install pywin32
```

### Problema 2: "El USB no se detecta"

**Verificar:**
1. USB está completamente conectado
2. USB es reconocido por Windows (En Mi PC aparece)
3. Script está en ejecución

**Solución:**
```powershell
# Ver unidades conectadas
Get-Volume
```

### Problema 3: "Permiso denegado al crear carpeta destino"

**Solución:**
```powershell
# Ejecutar como administrador
# O cambiar ruta destino a carpeta accesible
```

### Problema 4: "PyInstaller no compila correctamente"

**Solución:**
```powershell
pip install --upgrade pyinstaller
pip install --upgrade wheel
```

### Problema 5: "El reporte no se genera"

**Verificar:**
1. Carpeta destino existe y tiene permisos de escritura
2. Al menos se copió un archivo
3. Disco no está lleno

---

## ❓ Preguntas Frecuentes

### P: ¿Qué sucede si el USB se desconecta durante la copia?

R: El script continúa monitoreando. Cuando reconectes el mismo USB, reanudará la copia de los archivos que falten.

### P: ¿Se pueden cambiar las carpetas?

R: Sí, edita `monitor_usb.py` y modifica:
```python
DESTINO = r"C:\Users\<TU_USUARIO>\Desktop\<CARPETA_DESTINO>"
```

**Ejemplos:**
```python
DESTINO = r"C:\Users\elkin\Desktop\monitorUSB\archivos"
DESTINO = r"D:\Backups\USB_Archivos"
DESTINO = r"C:\Users\Maria\Documents\Copias"
```

**Nota**: Reemplaza `<TU_USUARIO>` y `<CARPETA_DESTINO>` según corresponda

### P: ¿Es seguro para el USB?

R: Sí, solo lee los archivos. No modifica ni elimina nada del USB.

### P: ¿Cuánto espacio necesita?

R: El script copia exactamente el tamaño del USB. Si el USB tiene 1 GB, necesitará 1 GB libre en destino.

### P: ¿Puedo copiar a una unidad de red?

R: Sí, usa rutas de red:
```python
DESTINO = r"\\servidor\compartido\carpeta"
```

### P: ¿El reporte incluye todo?

R: El reporte muestra los primeros 100 archivos en detalle. Si hay más, indica cuántos adicionales hay.

### P: ¿Necesito permisos de administrador?

R: No. Funciona con permisos de usuario normal.

### P: ¿Funcionará en USB externos y tarjetas SD?

R: Sí, cualquier dispositivo que Windows reconozca como unidad.

### P: ¿Puedo programar para ejecutar automáticamente?

R: Sí, usando Task Scheduler de Windows.

---

## 📞 Información Técnica

### Archivos del Proyecto

```
monitor_usb.py          ← Script Python (código fuente)
README.md               ← Esta guía educativa
reporte_usb.md          ← Reportes generados
svchost.exe             ← Programa compilado (si existe)
build/                  ← Archivos temporales de compilación
```

### Variables Configurables

Edita `monitor_usb.py` para cambiar:

```python
DESTINO = r"C:\ruta\destino"  # Carpeta donde copiar archivos
```

### Funciones Principales

- `ocultar_consola()` - Oculta ventana
- `procesar_usb_silencioso()` - Procesa USB
- `generar_reporte_markdown()` - Crea reporte
- `monitorear_dispositivos_usb()` - Loop principal
- `compilar_ejecutable()` - Genera EXE

---

---

## 📜 Contexto Educativo

Este programa es una **herramienta de aprendizaje** para estudiantes de ciberseguridad que desean comprender:

- Cómo funcionan los infostealers reales
- Técnicas de evasión de detección
- Patrones de análisis forense
- Estrategias defensivas
- Desarrollo de sistemas de detección

### ⚠️ RESTRICCIONES CRÍTICAS:

```
✅ PERMITIDO SOLO PARA:
- Estudiantes de ciberseguridad autorizados
- Laboratorios académicos aislados
- Análisis forense autorizado
- Investigación bajo supervisión

❌ ESTRICTAMENTE PROHIBIDO:
- Usar sin autorización
- En sistemas de producción
- Para robo de datos
- Distribución no autorizada
- Violación de privacidad
```

### Responsabilidad Legal:

El usuario acepta:
- Cumplir con todas las leyes aplicables
- Usar solo en entorno autorizado
- No causar daño a sistemas terceros
- Reportar vulnerabilidades responsablemente

---
