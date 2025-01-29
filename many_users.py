usuarios = {
    'apaz' : {
        'nombre':'arturo',
        'apellido':'paz',
        'edad': 37,
    },

    'syuruki' : {
        'nombre': 'susana',
        'apellido': 'yuruki',
        'edad' : 62,
    }
}

for username, user_info in usuarios.items():
    print(f"\nUsername: {username}")
    nombres = f"{user_info['nombre']} {user_info['apellido']}"
    edad = user_info['edad']

    print(f"\tNombres: {nombres.title()}")
    print(f"\tEdad: {edad}")
    