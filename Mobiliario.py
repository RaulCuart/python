class Llibre:
    def __init__(self,nom, cuantitat, tamany, pes):
        self.nom = nom
        self.cuantitat = cuantitat
        self.tamany = tamany
        self.pes = pes
    def __str__(self):
        return f" Nombre: {self.nom}, cuantitat: {self.cuantitat}, tamany: {self.tamany}, pes: {self.pes} "