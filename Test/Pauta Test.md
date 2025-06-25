# 🧪 Pauta de Evaluación Técnica – Python: Lectura y Promedio de Archivo

## ✅ Objetivo

Evaluar la capacidad de un desarrollador para procesar archivos de texto, validar datos, manejar errores, y escribir código limpio y robusto. El archivo contiene líneas con datos de fecha y valor separado por coma. El objetivo es calcular el promedio de los valores válidos.

---

## 📝 Criterios de Evaluación (Total: 110 puntos)

| Nº | Criterio | Descripción | Puntaje Máx. | Puntaje Obtenido |
|----|----------|-------------|---------------|------------------|
| 1 | **Manejo de archivos** | Uso correcto de apertura y cierre del archivo (idealmente `with open`). | 10 pts |         |
| 2 | **Lectura robusta de líneas** | Considera espacios, líneas vacías o mal formateadas. Usa `.strip()` o validaciones. | 15 pts |         |
| 3 | **Manejo de errores individuales por línea** | Maneja valores vacíos, incorrectos o no convertibles (`try/except` por línea). | 15 pts |         |
| 4 | **Validación de formato** | Verifica si la línea contiene una coma y dos partes válidas. | 10 pts |         |
| 5 | **Conversión segura a entero** | Usa `try/except` o validación antes de convertir a `int`. | 10 pts |         |
| 6 | **Cálculo del promedio solo con datos válidos** | No incluye líneas erróneas en el promedio. | 10 pts |         |
| 7 | **Muestra del resultado claro** | El resultado se imprime correctamente al final, con buen formato. | 5 pts  |         |
| 8 | **Buen uso de excepciones globales** | Manejo de `FileNotFoundError` y errores generales (`Exception`). | 10 pts |         |
| 9 | **Estilo y legibilidad** | Código limpio, indentado, con nombres descriptivos. | 10 pts |         |
| 10 | **Modularización de la lógica** | Separa claramente funciones como `leer_datos()` y `calcular_promedio()` para mejorar la mantenibilidad. | 5 pts |         |
| 11 | **Extras (Bonus)** | Mejora opcional: log de errores, contador de líneas descartadas, validación de fecha. | 5 pts  |         |
| 12 | **Uso de `pandas` (Bonus)** | Se usó `pandas` para cargar, limpiar y operar sobre el archivo de manera eficiente. | 5 pts |         |
|    | **TOTAL** | | **110 pts** | **____/110** |

---

## 🎯 Rango de Desempeño

- **90–110 puntos** → 🟢 *Excelente*: Código robusto, limpio y bien estructurado.
- **70–89 puntos** → 🟡 *Bueno*: Funciona correctamente pero con detalles que mejorar.
- **50–69 puntos** → 🟠 *Regular*: Faltan validaciones importantes o tiene errores de lógica.
- **0–49 puntos** → 🔴 *Insuficiente*: Código incompleto, frágil o con errores graves.

---

## 💡 Ejemplo de solución con `pandas` (bonus)

```python
def read_file(file_path):
    total_sum = 0
    record_count = 0
    skipped = 0

    try:
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    skipped += 1
                    continue

                parts = line.split(",")
                if len(parts) != 2:
                    skipped += 1
                    continue

                date, value = parts[0].strip(), parts[1].strip()

                try:
                    num = int(value)
                    total_sum += num
                    record_count += 1
                except ValueError:
                    skipped += 1
                    continue

        if record_count > 0:
            average = total_sum / record_count
            print("El promedio de valores es:", average)
        else:
            print("No hay registros válidos para calcular el promedio.")

        print(f"{skipped} líneas fueron descartadas.")

    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")
    except Exception as e:
        print("Ocurrió un error inesperado:", e)

    print("Proceso finalizado.")




#===============================================================================


import pandas as pd

def calcular_promedio_con_pandas(file_path):
    try:
        df = pd.read_csv(file_path, header=None, names=["fecha", "valor"])
        df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
        promedio = df["valor"].dropna().mean()
        print("El promedio de valores es:", promedio)
        print(f"{df['valor'].isna().sum()} líneas fueron descartadas.")
    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")
    except Exception as e:
        print("Ocurrió un error inesperado:", e)

    print("Proceso finalizado.")
