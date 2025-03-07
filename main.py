import sys
from PyQt5.QtWidgets import *
from Llibre import Llibre
from Mobiliario import Mobiliario

class MenuPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Biblioteca")
        self.setGeometry(800, 300, 400, 400)
        self.layout = QVBoxLayout()

        self.boton_libros = QPushButton("Libros")
        self.boton_libros.clicked.connect(self.abrir_ventana_libros)

        self.boton_muebles = QPushButton("Muebles")
        self.boton_muebles.clicked.connect(self.abrir_ventana_muebles)

        self.layout.addWidget(self.boton_muebles)
        self.layout.addWidget(self.boton_libros)
        self.setLayout(self.layout)

    def abrir_ventana_libros(self):
        self.ventana_libros = Biblioteca()
        self.ventana_libros.show()

    def abrir_ventana_muebles(self):
        self.ventana_muebles = Muebles()
        self.ventana_muebles.show()

class Muebles(QWidget):
    def __init__(self):
        super().__init__()

        self.muebles = []
        self.setWindowTitle("Muebles")
        self.setGeometry(800, 300, 400, 400)
        self.layout = QVBoxLayout()

        self.boton_anadir_mueble = QPushButton("Añadir Mueble")
        self.boton_anadir_mueble.clicked.connect(self.anadir_mueble)

        self.boton_ver_muebles = QPushButton("Ver Muebles")
        self.boton_ver_muebles.clicked.connect(self.ver_muebles)

        self.layout.addWidget(self.boton_anadir_mueble)
        self.layout.addWidget(self.boton_ver_muebles)
        self.setLayout(self.layout)

    def anadir_mueble(self):
        #QMessageBox.information(self, "Añadir muebles", "Se ha pulsado el boton de añadir muebles")
        self.formulario = FormularioMobiliario(self)
        self.formulario.show()

    def abrir_ventana_csv(self):
        self.ventana_csv = Menu_CSV()
        self.ventana_csv.show()

    def ver_muebles(self):
        QMessageBox.information(self,"Ver muebles", "Se ha pulsado el boton de ver muebles")

# Ventana para gestionar libros (Añadir y Ver)
class Biblioteca(QWidget):
    def __init__(self):
        super().__init__()

        self.libros = []
        self.setWindowTitle("Gestión de Libros")
        self.setGeometry(800, 300, 400, 400)

        # Crear layout
        self.layout = QVBoxLayout()

        # Botón para añadir libros (cambiamos 'añadir' por 'anadir' para evitar caracteres especiales)
        self.boton_anadir = QPushButton("Añadir Libro")
        self.boton_anadir.clicked.connect(self.anadir_libro)  # Conectar acción

        # Botón para ver libros
        self.boton_ver = QPushButton("Ver Libros")
        self.boton_ver.clicked.connect(self.ver_libros)  # Conectar acción

        self.boton_csv = QPushButton("CSV")
        self.boton_csv.clicked.connect(self.abrir_ventana_csv)

        self.boton_graficos = QPushButton("Graficos")
        self.boton_graficos.clicked.connect(self.abrir_graficos)

        # Añadir botones al layout
        self.layout.addWidget(self.boton_anadir)
        self.layout.addWidget(self.boton_ver)
        self.layout.addWidget(self.boton_graficos)
        self.layout.addWidget(self.boton_csv)
        self.setLayout(self.layout)

    def anadir_libro(self):
        self.formulario = FormularioLibro(self)
        self.formulario.show()

    def ver_libros(self):
        self.ventana_libros = VerLibros(self.libros)
        self.ventana_libros.show()

    def abrir_ventana_csv(self):
        self.ventana_csv = Menu_CSV()
        self.ventana_csv.show()

    def abrir_graficos(self):
        QMessageBox.information(self,"Graficos", "Se ha pulsado el boton para ver los graficos")

class VerLibros(QWidget):
    def __init__(self, libros):
        super().__init__()

        self.libros = libros  # Guardamos la lista de libros
        self.setWindowTitle("Lista de Libros")
        self.setGeometry(400, 100, 1400, 800)

        # Crear layout
        self.layout = QVBoxLayout()

        # Crear un QListWidget para mostrar los libros
        self.lista_libros = QListWidget()
        self.lista_libros.addItems([str(libro) for libro in libros])  # Mostrar libros usando el __str__

        # Conectar el evento de clic en un libro
        self.lista_libros.itemClicked.connect(self.editar_libro)

        # Añadir la lista al layout
        self.layout.addWidget(self.lista_libros)
        self.setLayout(self.layout)

    def editar_libro(self, item):
        # Buscar el libro que corresponde al item seleccionado
        libro_seleccionado = next((libro for libro in self.libros if str(libro) == item.text()), None)

        if libro_seleccionado:
            # Mostrar el formulario de edición
            self.formulario_editar = FormularioEditarLibro(libro_seleccionado, self)
            self.formulario_editar.show()

class FormularioEditarLibro(QWidget):
    def __init__(self, libro, ventana_libros):
        super().__init__()

        self.libro = libro
        self.ventana_libros = ventana_libros  # Para actualizar la lista después de editar
        self.setWindowTitle(f"Editar {libro.nom}")
        self.setGeometry(400, 100, 400, 400)

        # Crear layout
        self.layout = QVBoxLayout()

        # Campos de formulario prellenados con los valores actuales del libro
        self.nom_input = QLineEdit(libro.nom)
        self.autor_input = QLineEdit(libro.autor)
        self.pagines_input = QLineEdit(libro.pagines)
        self.genere_input = QLineEdit(libro.genere)
        self.sinopsis_input = QLineEdit(libro.sinopsis)
        self.dataPublicacio_input = QLineEdit(libro.dataPublicacio)
        self.edicio_input = QLineEdit(libro.edicio)
        self.enPrestec_input = QLineEdit(libro.enPrestec)
        self.estanteria_input = QLineEdit(libro.estanteria)
        self.fila_input = QLineEdit(libro.fila)
        self.columna_input = QLineEdit(libro.columna)

        # Añadir los campos al formulario
        self.layout.addWidget(QLabel("Nombre:"))
        self.layout.addWidget(self.nom_input)
        self.layout.addWidget(QLabel("Autor:"))
        self.layout.addWidget(self.autor_input)
        self.layout.addWidget(QLabel("Paginas:"))
        self.layout.addWidget(self.pagines_input)
        self.layout.addWidget(QLabel("Genero:"))
        self.layout.addWidget(self.genere_input)
        self.layout.addWidget(QLabel("Sinopsis:"))
        self.layout.addWidget(self.sinopsis_input)
        self.layout.addWidget(QLabel("Fecha de Publicacion:"))
        self.layout.addWidget(self.dataPublicacio_input)
        self.layout.addWidget(QLabel("Edicion:"))
        self.layout.addWidget(self.edicio_input)
        self.layout.addWidget(QLabel("En Prestamo:"))
        self.layout.addWidget(self.enPrestec_input)
        self.layout.addWidget(QLabel("Estantería:"))
        self.layout.addWidget(self.estanteria_input)
        self.layout.addWidget(QLabel("Fila:"))
        self.layout.addWidget(self.fila_input)
        self.layout.addWidget(QLabel("Columna:"))
        self.layout.addWidget(self.columna_input)

        # Botón para guardar cambios
        self.boton_guardar = QPushButton("Guardar Cambios")
        self.boton_guardar.clicked.connect(self.guardar_cambios)

        self.boton_borrar = QPushButton("Borrar Libro")
        self.boton_borrar.clicked.connect(self.borrar_libro)

        self.layout.addWidget(self.boton_borrar)
        self.layout.addWidget(self.boton_guardar)

        self.setLayout(self.layout)

    def borrar_libro(self):
        self.ventana_libros.libros.remove(self.libro)
        self.ventana_libros.lista_libros.clear()
        self.ventana_libros.lista_libros.addItems([str(libro) for libro in self.ventana_libros.libros])
        self.close()

    def guardar_cambios(self):
        # Actualizamos los campos del libro con los nuevos valores
        self.libro.nom = self.nom_input.text()
        self.libro.autor = self.autor_input.text()
        self.libro.pagines = self.pagines_input.text()
        self.libro.genere = self.genere_input.text()
        self.libro.sinopsis = self.sinopsis_input.text()
        self.libro.dataPublicacio = self.dataPublicacio_input.text()
        self.libro.edicio = self.edicio_input.text()
        self.libro.enPrestec = self.enPrestec_input.text()
        self.libro.estanteria = self.estanteria_input.text()
        self.libro.fila = self.fila_input.text()
        self.libro.columna = self.columna_input.text()

        # Actualizar la lista de libros
        self.ventana_libros.lista_libros.clear()
        self.ventana_libros.lista_libros.addItems([str(libro) for libro in self.ventana_libros.libros])

        # Cerrar el formulario
        self.close()

class Menu_CSV(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Csv")
        self.setGeometry(800, 300, 400, 400)

class FormularioLibro(QWidget):
    def __init__(self, biblioteca):
        super().__init__()

        self.setWindowTitle("Añadir Libro")
        self.setGeometry(800, 300, 400, 400)

        # Referencia a la clase Biblioteca para agregar libros
        self.biblioteca = biblioteca

        # Crear layout
        self.layout = QVBoxLayout()

        # Campos para el formulario
        self.nom_input = QLineEdit()
        self.autor_input = QLineEdit()
        self.pagines_input = QLineEdit()
        self.genere_input = QLineEdit()
        self.sinopsis_input = QLineEdit()
        self.dataPublicacio_input = QLineEdit()
        self.edicio_input = QLineEdit()
        self.enPrestec_input = QLineEdit()
        self.estanteria_input = QLineEdit()
        self.fila_input = QLineEdit()
        self.columna_input = QLineEdit()

        # Añadir campos al formulario
        self.layout.addWidget(QLabel("Nombre:"))
        self.layout.addWidget(self.nom_input)

        self.layout.addWidget(QLabel("Autor:"))
        self.layout.addWidget(self.autor_input)

        self.layout.addWidget(QLabel("Paginas:"))
        self.layout.addWidget(self.pagines_input)

        self.layout.addWidget(QLabel("Genero:"))
        self.layout.addWidget(self.genere_input)

        self.layout.addWidget(QLabel("Sinopsis:"))
        self.layout.addWidget(self.sinopsis_input)

        self.layout.addWidget(QLabel("Fecha de Publicacion:"))
        self.layout.addWidget(self.dataPublicacio_input)

        self.layout.addWidget(QLabel("Edicion:"))
        self.layout.addWidget(self.edicio_input)

        self.layout.addWidget(QLabel("En Prestamo:"))
        self.layout.addWidget(self.enPrestec_input)

        self.layout.addWidget(QLabel("Estantería:"))
        self.layout.addWidget(self.estanteria_input)

        self.layout.addWidget(QLabel("Fila:"))
        self.layout.addWidget(self.fila_input)

        self.layout.addWidget(QLabel("Columna:"))
        self.layout.addWidget(self.columna_input)

        # Botón para guardar el libro
        self.boton_guardar = QPushButton("Guardar Libro")
        self.boton_guardar.clicked.connect(self.guardar_libro)

        self.layout.addWidget(self.boton_guardar)

        self.setLayout(self.layout)

    def guardar_libro(self):
        nom = self.nom_input.text()
        autor = self.autor_input.text()
        pagines = self.pagines_input.text()
        genere = self.genere_input.text()
        sinopsis = self.sinopsis_input.text()
        dataPublicacio = self.dataPublicacio_input.text()
        edicio = self.edicio_input.text()
        enPrestec = self.enPrestec_input.text()
        estanteria = self.estanteria_input.text()
        fila = self.fila_input.text()
        columna = self.columna_input.text()

        libro = Llibre(nom, autor, pagines, genere, sinopsis, dataPublicacio, edicio, enPrestec, estanteria, fila,columna)
        self.biblioteca.libros.append(libro)

        QMessageBox.information(self, "Libro Guardado", f"Se guardó {libro.nom}")

        # Al enviar el formulario con el clear los campos se vacian por si quieres añadir un nuevo libro.
        self.nom_input.clear()
        self.autor_input.clear()
        self.pagines_input.clear()
        self.genere_input.clear()
        self.sinopsis_input.clear()
        self.dataPublicacio_input.clear()
        self.edicio_input.clear()
        self.enPrestec_input.clear()
        self.estanteria_input.clear()
        self.fila_input.clear()
        self.columna_input.clear()

class FormularioMobiliario(QWidget):
    def __init__(self, muebles):
        super().__init__()

        self.setWindowTitle("Añadir Muebles")
        self.setGeometry(800, 300, 400, 400)

        # Referencia a la clase mueble para agregar muebles
        self.muebles = muebles

        # Crear layout
        self.layout = QVBoxLayout()

        # Campos para el formulario
        self.nom_input = QLineEdit()
        self.cuantitat_input = QLineEdit()
        self.tamany_input = QLineEdit()
        self.pes_input = QLineEdit()

        # Añadir campos al formulario
        self.layout.addWidget(QLabel("Nombre:"))
        self.layout.addWidget(self.nom_input)

        self.layout.addWidget(QLabel("Cantidad:"))
        self.layout.addWidget(self.cuantitat_input)

        self.layout.addWidget(QLabel("Tamaño:"))
        self.layout.addWidget(self.tamany_input)

        self.layout.addWidget(QLabel("Peso:"))
        self.layout.addWidget(self.pes_input)


        # Botón para guardar el mueble
        self.boton_guardar = QPushButton("Guardar Mueble")
        self.boton_guardar.clicked.connect(self.guardar_mueble)

        self.layout.addWidget(self.boton_guardar)

        self.setLayout(self.layout)

    def guardar_mueble(self):
        nom = self.nom_input.text()
        cuantitat = self.cuantitat_input.text()
        tamany = self.tamany_input.text()
        pes = self.pes_input.text()

        mueble = Mobiliario(nom, cuantitat, tamany, pes)
        self.muebles.muebles.append(mueble)

        QMessageBox.information(self, "Mueble Guardado", f"Se guardó {mueble.nom}")

        # Al enviar el formulario con el clear los campos se vacian por si quieres añadir un nuevo libro.
        self.nom_input.clear()
        self.cuantitat_input.clear()
        self.tamany_input.clear()
        self.pes_input.clear()


# Bloque para ejecutar la aplicación correctamente
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Asegurarse de que no se cierre la aplicación automáticamente
    ventana = MenuPrincipal()
    ventana.show()
    sys.exit(app.exec_())
