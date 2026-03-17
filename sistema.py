import requests
from Profesor import Profesor
from Horario import Horario
from Bloque_horario import Bloque_horario
from Materia import Materia
from Seccion import Seccion

class Sistema:
    def __init__(self):
        self.codigos_materias = []  
        self.lista_materias_t1 = []
        self.lista_materias_t2 = []
        self.lista_materias_t3 = []

    def cargar_materias(self,lista_apis):
        lista_materias = [self.lista_materias_t1, self.lista_materias_t2, self.lista_materias_t3]

        opciones = ["Primer trimestre", "Segundo trimestre", "Tercer trimestre","Todas"]
       
        for opcion in opciones:
            print(f"{opcion}")
        elegida = input("Escriba el nombre del trimestre o 'Todas' para cargar todos): ")
        
        if elegida == "Todas":
            for i in range(len(lista_apis)):
                url = lista_apis[i]
                lista_para_guardar = lista_materias[i]
                respuesta = requests.get(url)
                datos = []
                if respuesta.status_code == 200:
                    datos = respuesta.json() 
                    # Cargar materias
                    if len(datos) != 0:
                        for materia in datos:
                            codigo = materia['Código']
                            if codigo not in self.codigos_materias:
                                self.codigos_materias.append(codigo)
                            nombre = materia['Nombre']
                            cant_secciones = materia['Secciones']
                            lista_secciones = []
                            for i in range(cant_secciones):
                                id_seccion = f"{codigo}-{i+1}"
                                materia_nombre = materia['Nombre']
                                nueva_seccion = Seccion(id_seccion, materia_nombre, "No asignado.")
                                lista_secciones.append(nueva_seccion)
                            
                            nueva_materia = Materia(codigo, nombre, cant_secciones, lista_secciones)
                            
                            lista_para_guardar.append(nueva_materia)
                            
                else:
                    print("Error al acceder a la API") 
        
        
        elif elegida == "Primer trimestre": #Lo pueden manejar asi 
            pass
            
    def imprimir_materias(self):
        print("Materias del primer trimestre:")
        for materia in self.lista_materias_t1:
            materia.mostrar_materia()
               
        print("\nMaterias del segundo trimestre:")
        for materia in self.lista_materias_t2:
            materia.mostrar_materia()
        
        print("\nMaterias del tercer trimestre:")
        for materia in self.lista_materias_t3:
            materia.mostrar_materia()

    def cargar_profesores(self, url_profesores):
        """Descarga los datos de los profesores desde la API."""
        respuesta = requests.get(url_profesores)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            for p in datos:
                # creamos el objeto Profesor usando las llaves del JSON
                nuevo_profe = Profesor(
                    p['Cédula'], 
                    p['Email'], 
                    p['Apellido'], 
                    p['Nombre'], 
                    p['Carga máxima'], 
                    p['Materias']
                )
                self.lista_profesores.append(nuevo_profe)
            print(f"\n--- Se cargaron {len(self.lista_profesores)} profesores exitosamente ---")
        else:
            print("Error al acceder a la API de profesores")



    def imprimir_profesores(self):
        print("\n=== LISTADO DE PROFESORES ===")
        for profe in self.lista_profesores:
            profe.mostrar_profesor()
        
        
        
    def generar_horarios(self):
        # 1. configuracion inicial segun la guia
        try:
            # la guia pide solicitar el numero de salones al usuario [cite: 3, 45]
            num_salones = int(input("\ningrese el numero de salones disponibles (ej. 30): "))
        except:
            num_salones = 30 # valor por defecto ante error de entrada [cite: 40, 43]
            
        # 2. creamos los bloques segun la franja de 7:00 am a 7:00 pm [cite: 46]
        bloques_disponibles = [
            Bloque_horario("B1", "Lunes-Miercoles", "07:00", "09:00", []),
            Bloque_horario("B2", "Lunes-Miercoles", "09:00", "11:00", []),
            Bloque_horario("B3", "Martes-Jueves", "07:00", "09:00", []),
            Bloque_horario("B4", "Martes-Jueves", "09:00", "11:00", [])
        ]
        
        # 3. seleccion de trimestre para procesar [cite: 14]
        print("\n1. Primer trimestre\n2. Segundo trimestre\n3. Tercer trimestre")
        opc = input("seleccione el numero del trimestre: ")
        
        materias_a_procesar = []
        if opc == "1": materias_a_procesar = self.lista_materias_t1
        elif opc == "2": materias_a_procesar = self.lista_materias_t2
        elif opc == "3": materias_a_procesar = self.lista_materias_t3
        
        # 4. distribucion de secciones con regla de ubicuidad 
        for materia in materias_a_procesar:
            for seccion in materia.lista_secciones:
                if seccion.estado == "Asignada": # solo secciones con profe
                    asignada_a_bloque = False
                    
                    for bloque in bloques_disponibles:
                        # chequeo de capacidad de salones 
                        if len(bloque.lista_secciones) < num_salones:
                            
                            # --- AQUI VA LA LOGICA DEL PUNTO 3 ---
                            # verificamos si el profesor ya tiene clase en este bloque (ubicuidad) 
                            profesor_libre = True
                            for s_ocupada in bloque.lista_secciones:
                                if s_ocupada.profesor == seccion.profesor:
                                    profesor_libre = False 
                                    break
                            
                            if profesor_libre:
                                bloque.lista_secciones.append(seccion)
                                seccion.estado = "Programada"
                                asignada_a_bloque = True
                                break # seccion lista, pasamos a la siguiente
                    
                    if not asignada_a_bloque:
                        seccion.estado = "Sin salon o profesor ocupado" 
        
        # 5. mostrar resultados
        print("\n=== REPORTE DE HORARIOS GENERADOS ===")
        for b in bloques_disponibles:
            if len(b.lista_secciones) > 0:
                b.mostrar_bloque()
                
            self.menu_resultados(bloques_disponibles)
    
    
    def iniciar_listas_vacias(self):
        # inicializa el sistema sin datos predefinidos
        self.codigos_materias = []
        self.lista_materias_t1 = []
        self.lista_materias_t2 = []
        self.lista_materias_t3 = []
        self.lista_profesores = []
        print("\n--- sistema iniciado con listas en blanco ---")

    def cargar_desde_csv(self):
        # permite retomar una planificacion guardada
        import os
        archivo = "horario_guardado.csv"
        if not os.path.exists(archivo):
            # si el archivo no existe, informa y redirige segun la guia
            print(f"\n[error] el archivo {archivo} no existe.")
            print("por favor, use la carga inicial (api o blanco) primero.")
            return False
        else:
            print("\n--- cargando datos desde csv... (funcionalidad en desarrollo) ---")
            return True
        
        
    def menu_gestion(self):
        # nivel 2: configuracion de recursos
        while True:
            print("\n--- MENU DE GESTION (NIVEL 2) ---")
            print("1. gestion de profesores (visualizar)")
            print("2. gestion de materias (visualizar)")
            print("3. generar horarios (proceder al nivel 3)")
            print("4. volver al menu principal")
            
            opcion = input("\nseleccione una opcion: ")
            
            if opcion == "1":
                self.imprimir_profesores()
                # aqui se podrian añadir metodos de alta/baja de profes
            elif opcion == "2":
                self.imprimir_materias()
                # aqui se podrian añadir metodos de modificacion de materias
            elif opcion == "3":
                # antes de generar, asignamos los profesores segun la logica previa
                self.asignar_secciones()
                self.generar_horarios() 
                # luego de generar, el programa fluye hacia el nivel 3
            elif opcion == "4":
                break
            else:
                print("opcion no valida.")
                
                
    def exportar_a_csv(self, bloques):
        # guarda el progreso en un archivo csv para visualizar en excel [cite: 29]
        nombre_archivo = "horario_generado.csv"
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as f:
                # cabecera del archivo
                f.write("Bloque,Dias,Hora,Seccion,Materia,Profesor,Estado\n")
                for b in bloques:
                    for s in b.lista_secciones:
                        linea = f"{b.id_bloque},{b.dias},{b.hora_inicio}-{b.hora_fin},"
                        linea += s.obtener_datos_csv()
                        f.write(linea)
            print(f"\n✓ archivo '{nombre_archivo}' generado con exito.")
        except Exception as e:
            print(f"error al exportar: {e}")

    def menu_resultados(self, bloques_generados):
        # nivel 3: menu de resultados y sub-modulos [cite: 23]
        while True:
            print("\n--- MENU DE RESULTADOS (NIVEL 3) ---")
            print("1. visualizar horarios por bloque")
            print("2. exportar horario a csv (excel)")
            print("3. volver al menu de gestion")
            
            opc = input("\nseleccione una opcion: ")
            
            if opc == "1":
                for b in bloques_generados:
                    b.mostrar_bloque()
            elif opc == "2":
                self.exportar_a_csv(bloques_generados)
            elif opc == "3":
                break
            else:
                print("opcion no valida.")
                
                