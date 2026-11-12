#!/usr/bin/env python3
import datetime

print(f"\n\t[+] Estudio: fechas y horas")

print(f"\n[+] Fecha y hora actual:\n")
ahora = datetime.datetime.now()
print(ahora)

print(f"\n[+] Hora esplicita:\n")
hora_e = datetime.time(14, 25, 18)
print(hora_e)



print(f"\n[+] Fecha esplicita:\n")
fecha_e = datetime.date(2023, 6, 14)
print(fecha_e)


print(f"\n[+] Fecha y hora esplicita:\n")
fechahora_e = datetime.datetime(2023, 6, 14, 13 ,59 ,25)
print(fechahora_e)


print(f"\n[+] Fecha y hora actual:\n")
tempo = datetime.datetime.now()
print(tempo)

anno = tempo.year
mese = tempo.month
giorno = tempo.day
ora = tempo.hour
minuti = tempo.minute
secondi = tempo.second
print(f"\nANo: {anno}, mes: {mese}, dia: {giorno}, hora: {ora}, minutos: {minuti}, segundos: {secondi}\n")
