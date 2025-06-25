def read_file(file_path):
    f = open(file_path, "r") 
    lines = f.readlines()
    total_sum = 0
    record_count = 0

    for line in lines:
        date, value = line.split(",")
        total_sum += int(value)
        record_count += 1
        
    # Calculo del promedio
    average = total_sum / record_count
    print("El promedio de valores es:", average)

try:
    read_file("data.txt")
except FileNotFoundError:
    print("Error: El archivo no fue encontrado.")
except Exception as e:
    print("Ocurrio un error inesperado:", e)

print("Proceso finalizado.")

'''
#data.txt
15-12-2024 , 5
15-11-2024 ,0
16-10-2024 ,1
13-09-2024 ,
 ,
17-08-2024 ,21
16-08-2024 ,0
17-08-2024 ,   6
2024-10-1, 7
16-08-2024 ,Seis
'''


