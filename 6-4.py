glossary = {
    'lista': 'Es un objeto que nos permite guardar valores de diferentes tipos',
    'tupla': 'Es un objeto que permite guardar valores que no cambian',
    'diccionario': 'Nos permite guardar valores en pares clave-valor',
    'loop_for': 'Permite realizar una busqueda iterando el contenido de un objeto',
    'print': 'Una funcion que permite imprimir en pantalla',
    'title()': 'Metodo que permite convertir la primera letra de una cadena en mayuscula',
    'get()': 'Metodo que permite obtener un valor de un diccionario',
    'keys()': 'Metodo que permite obtener las claves de un diccionario',
    'values()': 'Metodo que permite obtener los valores de un diccionario',
    'items()': 'Metodo que permite obtener los pares clave-valor de un diccionario'
}

print("Algunas definiciones del capítulo")
for k, v in glossary.items():
    print(f"{k.title()}:\n\t{v}")

# print(f"Lista:\n\t{glossary['lista']}")
# print(f"Tupla:\n\t{glossary['tupla']}")
# print(f"Diccionario:\n\t{glossary['diccionario']}")
# print(f"Loop For:\n\t{glossary['loop_for']}")
# print(f"Print:\n\t{glossary['print']}")