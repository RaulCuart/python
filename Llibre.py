class Llibre:
    def __init__(self,nom,autor,pagines,genere,sinopsis,dataPublicacio,edicio,enPrestec,estanteria,fila,columna):
        self.nom = nom
        self.autor = autor
        self.pagines = pagines
        self.genere = genere
        self.sinopsis = sinopsis
        self.dataPublicacio = dataPublicacio
        self.edicio = edicio
        self.enPrestec = enPrestec
        self.estanteria = estanteria
        self.fila = fila
        self.columna = columna

    def __str__(self):
        return f" Nombre: {self.nom}, Autor: {self.autor}, Numero de paginas: {self.pagines}, Genero: {self.genere}, Sinopsis: {self.sinopsis}, Fecha de publicacion: {self.dataPublicacio}, Edicion: {self.edicio}, En prestamo: {self.enPrestec}, Estanteria: {self.estanteria}, Fila: {self.fila}, Columna: {self.columna} "