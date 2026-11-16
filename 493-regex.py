#!/ustr/bin/env python3

import re

print("\n[+] Caracteres normales")
text = " Mi gato esta en el tejado, es el mejor gato de todos los gatos"

# buscamos la palabra gato

matches = re.findall("gato", text)
print(text)
print(matches)



print("\n[+] Caracteres especiales")
text1 = " Hoy es 15/12/2025 manana sera 16/12/2025"

# buscamos la palabra gato

matches1 = re.findall("\d{2}\/\d{2}\/\d{4}", text1)

# \d{2} son 2 digitos
# para poder identificar la barra "/" sin errores hay que escaparla \/
print(text1)
print(matches1)


print("\n[+] Caracteres delimitadores")
text3 = "Puedes contactarme a estos e-mail: soporte@thelagarto.com o info@thelagarto.io"

# \w contempla caracteres alfanumericos
# \w+ con + selecciona secuencia de varios elementos del mismo tipo
# separa en tuplas lo que tiene delimitador @

# matches3 = re.findall("(\w+)@(\w+).(\w+)", text3)
# alternativa porque hay que escapar el punto \.
# el {2,} significa desde 2 en aldelante
print(text3)
matches3 = re.findall("(\w+)@(\w+\.\w{2,})", text3)


print(matches3)


print("\n[+] Aplicar substituciones")

texto4 = "Mi gato esta en el tejado y mi perro en el jardin"
nuevo_texto = re.sub ("gato", "perro", texto4)
print(texto4)
print(nuevo_texto)



print("\n[+] Split")

campo = "Campo1,Campo2,Campo3,Campo4,Campo5"

nuevo_campo = re.split(",", campo)
print(campo)
print(nuevo_campo)


print("\n[+] Muestra elemento 2 de la lista ")

print(nuevo_campo[2])




print("\n[+] Validador de correo")

import re

def validar_correo(correo):
    print(f"Correo ingresado: {correo}")
    patron = "[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]{2,}"

    if re.findall(patron, correo):        
        return True
    else:      
        return False

print(validar_correo("soporte@.io"))
print(validar_correo("so/porte@parrot.io"))
print(validar_correo("soporte@.clan.com"))
print(validar_correo("$oporte@aaaa.io"))
print(validar_correo("Soporte@kali.hacker"))




print("[+] Patrones y match")

texto5 = "Hoy es 15/12/2025 manana sera 16/12/2025"
patron5 = r"\b(\d{2}\/\d{2}\/\d{4})\b"   

for match in re.finditer(patron5, texto5):
    print(f"La fecha es: {match.group(0)}, la cual comienza en la posicion {match.start()} y termina en la posicion {match.end()}")
