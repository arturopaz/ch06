# Ciudades

ciudades = {
    'Lima': { 'pais': 'peru', 'poblacion': 10_092_000, 'moneda': 'sol' },
    'roma': { 'pais': 'italia', 'poblacion': 2_760_000, 'moneda': 'euro' },
    'bogota': { 'pais': 'colombia', 'poblacion': 7_907_000, 'moneda': 'peso colombiano'},
}


for key, value in ciudades.items():
    print(f"Los datos de {key.title()}")
    for clave, valor in value.items():
        print(f"\t {clave.title()} : {valor}"
)