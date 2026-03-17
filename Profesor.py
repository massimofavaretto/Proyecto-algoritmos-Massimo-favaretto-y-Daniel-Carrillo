class Profesor():
    """clase que representa a un docente del sistema, almacena su informacion personal, capacidad de carga academica y las materias que esta autorizado a dictar"""
    
    def __init__(self, cedula, email, apellido, nombre, max_carga, materias):
        """inicializa los datos del profesor incluyendo identificacion, contacto, limites de secciones y una lista para controlar las asignaciones actuales"""
        
        self.cedula = cedula
        self.email = email
        self.apellido = apellido
        self.nombre = nombre
        self.max_carga = max_carga
        self.materias = materias  # lista de cddigos de materias que puede dar
        self.secciones_asignadas = [] # lista para guardar objetos seccion
        
    def tiene_cupo(self):
        """compara la cantidad de secciones ya asignadas con el limite maximo permitido para determinar si el profesor puede recibir mas trabajo"""
        
        return len(self.secciones_asignadas) < self.max_carga

    def mostrar_profesor(self):
        """presenta un resumen del perfil del docente en consola, mostrando su nombre completo, estado de su carga academica y los codigos de sus materias autorizadas"""
        
        materias_str = ", ".join(self.materias)
        print(f"ID: {self.cedula} | {self.nombre} {self.apellido} | Carga: {len(self.secciones_asignadas)}/{self.max_carga}")
        print(f"   Materias autorizadas: {materias_str}")