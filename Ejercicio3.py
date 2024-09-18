texto = input("ingrese una cadena de texto: ")

texto_mayus = texto.upper()
long = len(texto)
contiene_python = "python" in texto

print(f" Texto en mayusculas: {texto_mayus}")
print(f" Numero de caracteres: {long}")
print(f" Contiene la palabra ´python´ : {contiene_python}")