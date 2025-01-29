# Mascotas

mascotas = []

gato = {
    'tipo': 'felino',
    'dueño': 'arturo',
    'nombre': 'tom',
    'peso': 6
}

perro = {
    'tipo' : 'mamifero',
    'dueño': 'pancho',
    'nombre': 'yogy',
    'peso' : 15
}

mascotas.append(gato)
mascotas.append(perro)

for mascota in mascotas:
    print(f"\nLos datos de {mascota['nombre'].title()}")
    for k,v in mascota.items():
        print(f" {k.title()} : {v}")

    # print(f"\nTipo: {mascota['tipo'].title()}")
    # print(f"Dueño: {mascota['dueño'].title()}")




