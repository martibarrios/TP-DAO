class Usuario():
    def __init__(self, nombre, apellido, direccion, telefono):
        self.id = None
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Usuario(id={self.id}, nombre='{self.nombre}', apellido='{self.apellido}', direccion='{self.direccion}', telefono='{self.telefono}')"


class Estudiante(Usuario):
    def __init__(self, nombre, apellido, direccion, telefono):
        super().__init__(nombre, apellido, direccion, telefono)

    def __str__(self):
        return f"Estudiante({super().__str__()})"

class Profesor(Usuario):
    def __init__(self, nombre, apellido, direccion, telefono):
        super().__init__(nombre, apellido, direccion, telefono)

    def __str__(self):
        return f"Profesor({super().__str__()})"