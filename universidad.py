class Universidad:
    def __init__(self, nombre, ciudad=None):
        self.nombre = nombre
        self.ciudad = ciudad
        self.estudiantes = []

    def registrar_estudiante(self, nombre_estudiante):
        if nombre_estudiante and nombre_estudiante not in self.estudiantes:
            self.estudiantes.append(nombre_estudiante)

    def total_estudiantes(self):
        return len(self.estudiantes)
