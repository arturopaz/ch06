# Lugares favoritos
favorite_places = {
    'arturo' : ['roma','new york','francia'],
    'susana' : ['osaka', 'italia'],
    'jose'   : ['new york', 'colombia','rusia'],
}

for persona, lugares in favorite_places.items():
    print(f"\nLos lugares favoritos de {persona.title()} son:")
    for lugar in lugares:
        print(f"\t-{lugar.title()}")

