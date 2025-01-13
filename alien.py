alien_0 = {'x_position':0, 'y_position': 25, 'speed':'medium'}

print(f"la posicion en el eje x actual del alien {alien_0['x_position']}")

if alien_0['speed'] == 'low':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"la nueva posicion en el eje x  del alien {alien_0['x_position']}")
print(f"El diccionario tiene el siguiente valor: {alien_0}")
print("eliminando el parametro de velocidad...")
del alien_0['speed']
print(f"El diccionario quedo así: {alien_0}")
