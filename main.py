import sys
from PyQt5.QtWidgets import *
from Llibre import Llibre
from Mobiliario import Mobiliario
from Prestamo import Prestamo

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

    def ver_muebles(self):
        self.ventana_muebles = VerMuebles(self.muebles)
        self.ventana_muebles.show()

    def abrir_ventana_csv(self):
        self.ventana_csv = Menu_CSV()
        self.ventana_csv.show()

class MenuPrestamos(QWidget):
    def __init__(self,libros,prestamos,biblioteca):
        super().__init__()
        self.setWindowTitle("Menú de Préstamos")
        self.setGeometry(800, 300, 400, 400)


        self.prestamos = prestamos
        self.libros = libros
        self.biblioteca = biblioteca

        self.layout = QVBoxLayout()

        self.boton_crear_prestamo = QPushButton("Alquilar un libro")
        self.boton_crear_prestamo.clicked.connect(self.alquilar)


        self.boton_ver_prestamos = QPushButton("Ver Préstamos")
        self.boton_ver_prestamos.clicked.connect(self.ver_prestamos)

        self.boton_devolver_libro = QPushButton("Devolver Libro")
        self.boton_devolver_libro.clicked.connect(self.devolver_libro)

        self.layout.addWidget(self.boton_devolver_libro)
        self.layout.addWidget(self.boton_crear_prestamo)
        self.layout.addWidget(self.boton_ver_prestamos)
        self.setLayout(self.layout)

    def alquilar(self):
        self.ventana_prestamos = FormularioPrestamo(self, self.libros, self.prestamos)  # Cambia aquí
        self.ventana_prestamos.show()
        self.biblioteca.prestamos = self.prestamos


    def ver_prestamos(self):
        self.ventana_ver_prestamos = VerPrestamos(self.prestamos,self)
        self.ventana_ver_prestamos.show()
        self.biblioteca.prestamos = self.prestamos


    def devolver_libro(self):
        print("Función para devolver un libro")
        # Aquí puedes implementar la lógica para registrar la devolución de un libro
        self.biblioteca.prestamos = self.prestamos


class VerPrestamos(QWidget):
    def __init__(self, prestamos, menu_prestamos): #añadimos menu_prestamos para poder actualizar la lista
        super().__init__()

        self.prestamos = prestamos
        self.setWindowTitle("Lista de Préstamos")
        self.setGeometry(400, 100, 600, 400)
        self.menu_prestamos = menu_prestamos

        self.layout = QVBoxLayout()

        self.lista_prestamos = QListWidget()
        self.lista_prestamos.addItems([str(prestamo) for prestamo in prestamos])
        self.lista_prestamos.itemClicked.connect(self.editar_prestamo) #conectar evento

        self.layout.addWidget(self.lista_prestamos)
        self.setLayout(self.layout)

    def editar_prestamo(self, item):
        prestamo_seleccionado = next((prestamo for prestamo in self.prestamos if str(prestamo) == item.text()), None)

        if prestamo_seleccionado:
            self.formulario_editar = FormularioEditarPrestamo(prestamo_seleccionado, self)
            self.formulario_editar.show()

class FormularioEditarPrestamo(QWidget):
    def __init__(self, prestamo, ventana_prestamos):
        super().__init__()

        self.prestamo = prestamo
        self.ventana_prestamos = ventana_prestamos
        self.setWindowTitle(f"Editar Préstamo de {prestamo.llibre}")
        self.setGeometry(400, 100, 400, 400)

        self.layout = QVBoxLayout()

        self.usuario_input = QLineEdit(prestamo.alquilador)
        self.libro_input = QLineEdit(prestamo.llibre)
        self.fecha_devolucion_input = QLineEdit(prestamo.fechaFin)

        self.layout.addWidget(QLabel("Usuario:"))
        self.layout.addWidget(self.usuario_input)
        self.layout.addWidget(QLabel("Libro:"))
        self.layout.addWidget(self.libro_input)
        self.layout.addWidget(QLabel("Fecha de Devolución:"))
        self.layout.addWidget(self.fecha_devolucion_input)

        self.boton_guardar = QPushButton("Guardar Cambios")
        self.boton_guardar.clicked.connect(self.guardar_cambios)

        self.boton_borrar = QPushButton("Borrar Préstamo")
        self.boton_borrar.clicked.connect(self.borrar_prestamo)

        self.layout.addWidget(self.boton_borrar)
        self.layout.addWidget(self.boton_guardar)

        self.setLayout(self.layout)

    def borrar_prestamo(self):
        self.ventana_prestamos.menu_prestamos.prestamos.remove(self.prestamo)
        self.ventana_prestamos.lista_prestamos.clear()
        self.ventana_prestamos.lista_prestamos.addItems(
            [str(prestamo) for prestamo in self.ventana_prestamos.menu_prestamos.prestamos])
        for libro in self.ventana_prestamos.menu_prestamos.libros:
            if libro.nom == self.prestamo.llibre:
                libro.enPrestec = "No"
                break
        self.close()
        self.ventana_prestamos.menu_prestamos.biblioteca.prestamos = self.ventana_prestamos.menu_prestamos.prestamos

    def guardar_cambios(self):
        self.prestamo.alquilador = self.usuario_input.text()
        self.prestamo.llibre = self.libro_input.text()
        self.prestamo.fechaFin = self.fecha_devolucion_input.text()

        self.ventana_prestamos.lista_prestamos.clear()
        self.ventana_prestamos.lista_prestamos.addItems([str(prestamo) for prestamo in self.ventana_prestamos.menu_prestamos.prestamos])
        self.close()
        self.ventana_prestamos.menu_prestamos.biblioteca.prestamos = self.ventana_prestamos.menu_prestamos.prestamos

class FormularioPrestamo(QWidget):
    def __init__(self, gestion_prestamos, libros, prestamos):
        super().__init__()
        self.setWindowTitle("Afegir Préstec")
        self.setGeometry(800, 300, 400, 400)

        self.gestion_prestamos = gestion_prestamos
        self.libros = libros
        self.prestamos = prestamos

        self.layout = QVBoxLayout()

        self.libro_combo = QComboBox()
        self.libro_combo.addItems([libro.nom for libro in libros])

        self.usuario_input = QLineEdit()
        self.fecha_devolucion_input = QLineEdit()

        self.layout.addWidget(QLabel("Llibre:"))
        self.layout.addWidget(self.libro_combo)
        self.layout.addWidget(QLabel("Usuari:"))
        self.layout.addWidget(self.usuario_input)
        self.layout.addWidget(QLabel("Data de Devolució:"))
        self.layout.addWidget(self.fecha_devolucion_input)

        self.boton_guardar = QPushButton("Guardar Préstec")
        self.boton_guardar.clicked.connect(self.guardar_prestamo)

        self.layout.addWidget(self.boton_guardar)

        self.setLayout(self.layout)

    def guardar_prestamo(self):
        libro_seleccionado = self.libro_combo.currentText()
        usuario = self.usuario_input.text()
        fecha_devolucion = self.fecha_devolucion_input.text()
        prestamo = Prestamo(usuario, libro_seleccionado, fecha_devolucion)
        self.prestamos.append(prestamo)
        for libro in self.libros:
            if libro.nom == libro_seleccionado:
                libro.enPrestec = "En prestec"
                break
        self.close()
        self.gestion_prestamos.biblioteca.prestamos = self.prestamos

# Ventana para gestionar libros (Añadir y Ver)
class Biblioteca(QWidget):
    def __init__(self):
        super().__init__()

        self.libros = []
        self.prestamos = []
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

        self.boton_prestamos = QPushButton("Prestamos")
        self.boton_prestamos.clicked.connect(self.menu_prestamos)



        # Añadir botones al layout
        self.layout.addWidget(self.boton_anadir)
        self.layout.addWidget(self.boton_ver)
        self.layout.addWidget(self.boton_prestamos)
        self.setLayout(self.layout)

    def menu_prestamos(self):
        self.prestamos = MenuPrestamos(self.libros,self.prestamos, self)
        self.prestamos.show()


    def anadir_libro(self):
        self.formulario = FormularioLibro(self)
        self.formulario.show()

    def ver_libros(self):
        self.ventana_libros = VerLibros(self.libros)
        self.ventana_libros.show()

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
        self.libro.estanteria = self.estanteria_input.text()
        self.libro.fila = self.fila_input.text()
        self.libro.columna = self.columna_input.text()

        # Actualizar la lista de libros
        self.ventana_libros.lista_libros.clear()
        self.ventana_libros.lista_libros.addItems([str(libro) for libro in self.ventana_libros.libros])

        # Cerrar el formulario
        self.close()

class FormularioEditarMueble(QWidget):
    def __init__(self, mueble, ventana_muebles):
        super().__init__()

        self.mueble = mueble
        self.ventana_muebles = ventana_muebles  # Para actualizar la lista después de editar
        self.setWindowTitle(f"Editar {mueble.nom}")
        self.setGeometry(400, 100, 400, 400)

        # Crear layout
        self.layout = QVBoxLayout()

        # Campos de formulario prellenados con los valores actuales del libro
        self.nom_input = QLineEdit(mueble.nom)
        self.cuantitat_input = QLineEdit(mueble.cuantitat)
        self.tamany_input = QLineEdit(mueble.tamany)
        self.pes_input = QLineEdit(mueble.pes)

        # Añadir los campos al formulario
        self.layout.addWidget(QLabel("Nombre:"))
        self.layout.addWidget(self.nom_input)
        self.layout.addWidget(QLabel("Cantidad:"))
        self.layout.addWidget(self.cuantitat_input)
        self.layout.addWidget(QLabel("Tamaño:"))
        self.layout.addWidget(self.tamany_input)
        self.layout.addWidget(QLabel("Peso:"))
        self.layout.addWidget(self.pes_input)

        # Botón para guardar cambios
        self.boton_guardar = QPushButton("Guardar Cambios")
        self.boton_guardar.clicked.connect(self.guardar_cambios)

        self.boton_borrar = QPushButton("Borrar Mueble")
        self.boton_borrar.clicked.connect(self.borrar_mueble)

        self.layout.addWidget(self.boton_borrar)
        self.layout.addWidget(self.boton_guardar)

        self.setLayout(self.layout)

    def borrar_mueble(self):
        self.ventana_muebles.libros.remove(self.mueble)
        self.ventana_muebles.lista_muebles.clear()
        self.ventana_muebles.lista_muebles.addItems([str(mueble) for mueble in self.ventana_muebles.muebles])
        self.close()

    def guardar_cambios(self):
        # Actualizamos los campos del mueble con los nuevos valores
        self.mueble.nom = self.nom_input.text()
        self.mueble.cuantitat = self.cuantitat_input.text()
        self.mueble.tamany = self.tamany_input.text()
        self.mueble.pes = self.pes_input.text()

        # Actualizar la lista de muebles
        self.ventana_muebles.lista_muebles.clear()
        self.ventana_muebles.lista_muebles.addItems([str(mueble) for mueble in self.ventana_muebles.muebles])

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
        enPrestec = "No"
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

class VerMuebles(QWidget):
    def __init__(self, muebles):
        super().__init__()

        self.muebles = muebles  # Guardamos la lista de muebles
        self.setWindowTitle("Lista de Muebles")
        self.setGeometry(400, 100, 1400, 800)

        # Crear layout
        self.layout = QVBoxLayout()

        # Crear un QListWidget para mostrar los libros
        self.lista_muebles = QListWidget()
        self.lista_muebles.addItems([str(mueble) for mueble in muebles])  # Mostrar muebles usando el __str__

        # Conectar el evento de clic en un libro
        self.lista_muebles.itemClicked.connect(self.editar_muebles)

        # Añadir la lista al layout
        self.layout.addWidget(self.lista_muebles)
        self.setLayout(self.layout)

    def editar_muebles(self, item):
        # Buscar el mueble que corresponde al item seleccionado
        mueble_seleccionado = next((mueble for mueble in self.muebles if str(mueble) == item.text()), None)

        if mueble_seleccionado:
            # Mostrar el formulario de edición
            self.formulario_editar = FormularioEditarMueble(mueble_seleccionado, self)
            self.formulario_editar.show()


# Bloque para ejecutar la aplicación correctamente
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Asegurarse de que no se cierre la aplicación automáticamente
    ventana = MenuPrincipal()
    ventana.show()
    sys.exit(app.exec_())
