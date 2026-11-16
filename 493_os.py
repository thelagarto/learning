import os
import shutil

print("[+] Verifico si el archivo existe con os.path\n")

if os.path.exists("mi_archivo.txt"):
    print("[+] El archivo existe")
else:
    print("[+] El archivo NO existe")


print("\n[+] Creo un directorio con mkdir \n")

if not os.path.exists("mi_directorio1"):
    os.mkdir("mi_directorio1")


print("\n[+] Creo directorios anidados con makedirs \n")

if not os.path.exists("mi_directorio/mi_subdirectorio"):
    os.makedirs("mi_directorio/mi_subdirectorio")

print(f"[+] Listado de recursos en el directorio de trabajo con listdir:\n")
recursos = os.listdir()
for recurso in recursos:
    print(recurso)

print(f"[+] comprueba si file1.txt existe :\n")

if os.path.exists("file1.txt"):
    print("existo")
    os.remove("file1.txt")

    print("borro")
if os.path.exists("file1.txt"):
    print("existo")
else:
    print("no existo")


print("[+] borro directorio con contenido con shutil.rmtree")
if os.path.exists("mi_directorio"):
    shutil.rmtree("mi_directorio")

print("[+] borro directorio vacio con os rmdir")
if os.path.exists("mi_directorio1"):
    os.rmdir("mi_directorio1")

print("[+] Renombrar un file")
if os.path.exists("file2.txt"):
    os.rename("file2.txt", "file_02.txt" )





print("[+] Peso de un file ")
if os.path.exists("/etc/passwd"):
    tamano = os.path.getsize("/etc/passwd")
print(f"[+] El archivo /etc/passwd pesa {tamano} bytes")





print("\n[+] Test join / basename / dir  \n")

ruta = os.path.join("directorio44","archivo.txt")

print(f"[+] Ruta: {ruta}")

archivo = os.path.basename(ruta)
print(f"[+] Nombre de archivo:      {archivo}")
directorio = os.path.dirname(ruta)
print(f"[+] Nombre del directorio:  {directorio}")




print("\n[+] Test split  \n")


print(f"[+] Ruta: {ruta}")

directorio, archivo = os.path.split(ruta)

print(f"[+] Archivo: {archivo}, directorio: {directorio}")

if os.path.exists(directorio):
    print(f"Borro directorio con contenido: {directorio}")
    os.system("rm -r directorio44")
