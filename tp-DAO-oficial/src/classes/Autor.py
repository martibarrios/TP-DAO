class Autor():
    def __init__(self, nombre, apellido, nacionalidad) -> None:
        self.id = None
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        

    def __str__(self):
        return f"Autor(id={self.id}, nombre='{self.nombre}', apellido='{self.apellido}', nacionalidad='{self.nacionalidad}')"