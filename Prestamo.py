class Prestamo:
    def __init__(self,alquilador, llibre, fechaFin):
        self.llibre = llibre
        self.alquilador = alquilador
        self.fechaFin = fechaFin
    def __str__(self):
        return f" Nombre del alquilador: {self.alquilador}, Libro: {self.llibre}, Fecha de devolucion: {self.fechaFin}"