# friend = {
#     'first_name': 'jose',
#     'last_name': 'paz',
#     'age': 37,
#     'city': 'chimbote'
# }

people = [
    {
        'first_name': 'arturo',
        'last_name': 'paz',
        'age': 37,
        'city': 'chimbote'
    },
    {
        'first_name': 'susana',
        'last_name': 'yuruki',
        'age': 62,
        'city': 'lima'
    }    
]

print("Datos de las personas")
for person in people :
    print(f"\n{person}")
    print(f"\tNombre: {person['first_name'].title()}")
    print(f"\tApellido: {person['last_name'].title()}")
    print(f"\tEdad: {person['age']}")
    print(f"\tCiudad: {person['city'].title()}")



# print(f"First Name: {friend['first_name'].title()}")
# print(f"Second Name: {friend['last_name'].title()}")
# print(f"Age: {friend['age']}")
# print(f"City: {friend['city'].title()}")