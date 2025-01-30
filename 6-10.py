people_favorite_numbers = {
    'jose' : [7, 13, 21, 37],
    'pedro': [11, 87, 99],
    'juan' : [5, 12, 1, 66],
    'marlon': [23,90, 100],
    'estrella': [17, 77, 99],
}

for k, v in people_favorite_numbers.items():
    print(f"Los numero favoritos de {k.title()} son: ")
    for numero in v:
        print(f"\t- {numero}")
