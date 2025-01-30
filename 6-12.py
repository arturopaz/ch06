videojuegos = []
videojuego_0 = {
    'titulo' : 'resident evil',
    'lanzamiento' : '1996',
    'ventas' : '2,750,000',
}
videojuego_1 = {
    'titulo' : 'parasite evil',
    'lanzamiento' : '1999',
    'ventas' : '1,900,000',
}
videojuego_2 = {
    'titulo' : 'metal gear solid',
    'lanzamiento' : '1998',
    'ventas' : '6,000,000',
}

videojuegos.append(videojuego_0)
videojuegos.append(videojuego_1)
videojuegos.append(videojuego_2)


print("\tLista de Videojuegos")
for videojuego in videojuegos:
    for k,v in videojuego.items():
        print(f"{k.title()} : {v.title()}")
    print("\n")
 
     