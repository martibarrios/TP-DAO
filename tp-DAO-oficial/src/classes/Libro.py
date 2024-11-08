class Libro():
    def __init__(self, code_isbn, titulo, genero, anio_publicacion, autor, cant_disponible):
        self.code_isbn = code_isbn
        self.titulo = titulo
        self.genero = genero
        self.anio_publicacion = anio_publicacion
        self.autor = autor
        self.cant_disponible = cant_disponible

    def __str__(self):
        return f"Libro(isbn={self.code_isbn}, titulo='{self.titulo}', genero='{self.genero}', año_publicacion={self.anio_publicacion}, autor={self.autor}, cantidad_disponible={self.cant_disponible})"