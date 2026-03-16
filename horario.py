class Horario:
    """clase que representa un horario de clases, contiene el nombre del horario y la cantidad de salones disponibles"""
    def __init__(self, nombre, num_salones):
        """inicializa los atributos del horario, recibe el nombre y el numero de salones, ademas crea una lista vacia para los bloques"""
        
        self.nombre = nombre
        self.num_salones = num_salones
        self.lista_bloques_horario = []  

    
    def mostrar_horario(self):
        """imprime en consola la informacion general del horario, detallando el nombre, los salones y cada bloque registrado"""
        
        print(f"Horario: {self.nombre}")
        print(f"Número de salones disponibles: {self.num_salones}")
        for bloque in self.lista_bloques_horario:
            bloque.mostrar_bloque()