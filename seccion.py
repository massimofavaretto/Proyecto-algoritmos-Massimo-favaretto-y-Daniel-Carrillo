class Seccion():
    """clase que representa una secci9n especifica de una materia, gestiona el estado de la inscripcion y el profe que la da """
    
    def __init__(self, id_seccion, materia, profesor= "No asignado.", estado = "Por manejar en la distribucion."):
        """inicializa los datos de la seccion, recibe el identificador y la materia, estableciendo valores predeterminados para el profesor y el estado actual"""
        
        self.id_seccion = id_seccion
        self.materia = materia
        self.profesor = profesor
        self.estado = estado
        
    def asignar_profesor(self, profesor):
        """actualiza el atributo del docente encargado de la seccion con el objeto o nombre proporcionado"""
        self.profesor = profesor
        
    def mostrar_seccion(self):
        """imprime de forma formateada los detalles de la seccion, incluyendo su identificador, la materia asociada y el nombre del profesor asignado"""
        print(f"""          Sección: {self.id_seccion}, Materia: {self.materia}, Profesor: {self.profesor}""")
        
    def asignar_profesor(self, nombre_profesor):
        """establece el nombre del profe en la seccion y actualiza automaticamente el estado a asignada para mostrar el cambio en el sistema"""
        self.profesor = nombre_profesor
        self.estado = "Asignada" # cambia el estado al asignar un docente
        
    def asignar_secciones(self):
        """ejecuta el algoritmo de distribucion, recorre todas las materias de los tres trimestres buscando docentes con cupo y autorizacion para asignar cada seccion o cerrarla si no hay personal"""
        # unificamos todas las materias de los tres trimestres en una sola lista para procesar
        todas_las_materias = self.lista_materias_t1 + self.lista_materias_t2 + self.lista_materias_t3
        
        print("\n--- Iniciando proceso de asignacion de profesores ---")
        
        for materia in todas_las_materias:
            for seccion in materia.lista_secciones:
                # buscamos un profesor que pueda dar esta materia y tenga cupo
                profesor_encontrado = None
                
                for profe in self.lista_profesores:
                    # verificamos si el codigo de la materia esta en su lista y si tiene cupo
                    if materia.codigo in profe.materias and profe.tiene_cupo():
                        profesor_encontrado = profe
                        break # salimos del bucle de profesores al hallar uno
                
                if profesor_encontrado:
                    # vinculamos la seccion al profesor y viceversa
                    nombre_completo = f"{profesor_encontrado.nombre} {profesor_encontrado.apellido}"
                    seccion.asignar_profesor(nombre_completo)
                    profesor_encontrado.secciones_asignadas.append(seccion)
                else:
                    seccion.estado = "Cerrada"
                    seccion.profesor = "Sin profesor (no hay personal disponible)"
        
        print("Proceso de asignacion finalizado.")
    
    """genera una cadena de texto formateada con los atributos de la seccion separados por comas, hace q sea mas facil pasarlo a excel """    
    def obtener_datos_csv(self):
        return f"{self.id_seccion},{self.materia},{self.profesor},{self.estado}\n"