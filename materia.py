from Seccion import Seccion

class Materia:
    """clase que define una asignatura del plan de estudios, agrupa la informacion basica como el codigo, el nombre y la gestion de sus secciones correspondientes"""
    
    def __init__(self, codigo, nombre, cant_secciones,lista_secciones):
        self.codigo = codigo
        self.nombre = nombre
        self.cant_secciones = cant_secciones
        self.lista_secciones = lista_secciones
        
    def mostrar_materia(self):
        """metodo para visualizar los datos de la materia, muestra por pantalla el codigo y nombre seguidos del detalle individual de cada una de sus secciones"""
        
        print(f"Código: {self.codigo}, Materia: {self.nombre}, Secciones: {self.cant_secciones}")
        for seccion in self.lista_secciones:
            seccion.mostrar_seccion()