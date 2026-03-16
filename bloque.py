class Bloque_horario():
    
    """
    clase que representa un segmento de tiempo especifico en la planificacion.
    contiene la informacion de los dias, horas y las secciones que ocupan salones en ese bloque.
    """
    def __init__(self, id_bloque, dias, hora_inicio, hora_fin):
        
        """
        inicializa un bloque horario con su identificador y el rango de tiempo asignado
        """
        self.id_bloque = id_bloque
        self.dias = dias
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.lista_secciones = [] # inicializamos la lista vacia para llenarla luego
        
    def mostrar_bloque(self):
        """
        imprime en consola el resumen del bloque y el detalle de cada seccion que tiene asignada.
        """
        print(f"\n>>> Bloque: {self.id_bloque} ({self.dias}) | {self.hora_inicio} - {self.hora_fin}")
        print(f"    Capacidad: {len(self.lista_secciones)} secciones asignadas.")
        for seccion in self.lista_secciones:
            # llamamos al metodo de la clase seccion
            seccion.mostrar_seccion()