from Sistema import Sistema

def menu_principal():
    """funcion principal que gestiona el flujo del programa, permite al usuario elegir entre iniciar listas vacias, descargar datos de github o cargar archivos csv para procesar horarios"""
    sistema = Sistema()
    
    # urls de la api de github
    url_m1 = 'https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-2/refs/heads/main/materias2526-1.json'
    url_m2 = 'https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-2/refs/heads/main/materias2526-2.json' 
    url_m3 = 'https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-2/refs/heads/main/materias2425-3.json'
    url_profes = 'https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-2/refs/heads/main/profesores2526.json'
    lista_apis_materias = [url_m1, url_m2, url_m3]

    while True:
        """bucle infinito que mantiene el menu interactivo desplegado, capturando las opciones del usuario y redirigiendo a los diferentes niveles del sistema segun la seleccion"""
        
        print("\n--- MENU PRINCIPAL (NIVEL 1) ---")
        print("1. crear listas en blanco")
        print("2. descargar datos de la api de github")
        print("3. cargar un horario en csv")
        print("4. salir del programa")
        
        try:
            opcion = input("\nseleccione una opcion: ")
            
            if opcion == "1":
                sistema.iniciar_listas_vacias()
                sistema.menu_gestion() # salta al nivel 2 [cite: 19]
                
            elif opcion == "2":
                sistema.cargar_materias(lista_apis_materias)
                sistema.cargar_profesores(url_profes)
                sistema.menu_gestion() # salta al nivel 2 [cite: 19]
                
            elif opcion == "3":
                if sistema.cargar_desde_csv():
                    # si existe el csv, la guia pide ir directo a resultados (nivel 3) [cite: 41]
                    sistema.generar_horarios() 
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            
            