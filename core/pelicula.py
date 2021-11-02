class Pelicula:
    # Metodo constructor 
    # Permite crear nuevas instancias de peliculas
    def __init__(self, id,titulo, sinopsis, actores , duracion):
        self.id = id
        self.titulo = titulo
        self.sinopsis = sinopsis
        self.duracion = duracion
