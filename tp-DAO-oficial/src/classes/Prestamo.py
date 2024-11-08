class Prestamo():
    def __init__(self, usuario, libro, fecha_prestamo, fecha_devolucion):
        self.id = None
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def registrar_pretamo(self):
        pass

    def __str__(self):
        return f"Prestamo(id={self.id}, usuario={self.usuario}, libro={self.libro}, fecha_prestamo={self.fecha_prestamo}, fecha_devolucion={self.fecha_devolucion})"