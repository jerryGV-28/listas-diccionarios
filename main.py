import os
os.system("cls")
flag = True
postulantes = []
vacantes_totales= 20
vacantes = 20
aceptados = 0
rechazados = 0
promedio_acumulador = 0
try:
    while flag:
        print("=== SISTEMA DE POSTULACIÓN MAGÍSTER ===")
        print("1. Registrar postulante")
        print("2. Ver postulantes registrados")
        print("3. Buscar postulante por correo")
        print("4. Ver postulantes aceptados")
        print("5. Ver estadísticas")
        print("6. Mostrar vacantes disponibles")
        print("7. Salir")
        try:
            x = int(input("ingrese la accion a realizar:\n"))
            if x == 1:
                while True:
                    nombre = input("ingresa nombre del postulante:\n")
                    if nombre.isalpha() and len(nombre) >0:
                            break
                    else:
                        print("nombre invalido debe de tener solo letras")
                while True:
                    apellido = input("ingresa apellido del postulante:\n")
                    if apellido.isalpha() and len(apellido) > 0:
                            break
                    else:
                        print("apellido invalido debe de tener solo letras")
                while True:
                    try:
                        edad = int(input("ingrese la edad:\n"))
                        if edad >= 17 or edad <=60:
                            break
                        else:
                            print("edad debe de estar entre 17 y 60")
                            
                    except:
                        print("esta mal")
                while True:
                    correo = input("ingrese correo:\n")
                    if "@" in correo and "." in correo and len(correo) >=6:
                        break
                    else:
                        print("ingresa tu correo bien")
                while True:
                    carrera = input("ingrese su carrera:\n")
                    if len(carrera) >=4:
                        break
                    else:
                        print("esta mal")
                while True:
                    try:
                        promedio = float(input("ingrese tu promedio:\n"))
                        if promedio >= 1.0 and promedio <= 7.0:
                            break
                        else:
                            print("no esta en la escala adecuada de notas")
                    except:
                        print("esta mal")
                if edad >=20 and promedio >=5.5 and vacantes >0:
                    postulacion = "aceptada"
                    vacantes-=1
                    aceptados +=1
                else:
                    postulacion = "rechazada"
                    rechazados += 1
                postulante = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "edad": edad,
                    "correo": correo,
                    "carrera": carrera,
                    "promedio": promedio,
                    "estado": postulacion
                }
                postulantes.append(postulante)
                print("te has postulado con exito")
            elif x == 2:
                print("Ver postulantes")
                if len(postulantes) > 0: 
                    for p in postulantes:
                        print(f"Nombre completo: {p["nombre"]} {p["apellido"]}")
                        print(f"Edad: {p["edad"]}")
                        print(f"Correo: {p["correo"]}")
                        print(f"Carrera: {p["carrera"]}")
                        print(f"Promedio: {p["promedio"]}")
                        print(f"Estado: {p["estado"]}")
                        print("******************")
                
                else: 
                    print("No existen postulantes registrados")

            elif x == 3:
                if len(postulantes) > 0:
                    busqueda = input("ingrese el correo de postulante por consultar:\n")
                    for y in postulantes:
                        if busqueda == y["correo"]:
                            print("DATOS DEL POSTULANTE")
                            print(f"Nombre completo: {y["nombre"]} {y["apellido"]}")
                            print(f"Edad: {y["edad"]}")
                            print(f"Correo: {y["correo"]}")
                            print(f"Carrera: {y["carrera"]}")
                            print(f"Promedio: {y["promedio"]}")
                            print(f"Estado: {y["estado"]}")
                else:
                    print("no existen postulantes")
                
            elif x == 4:
                if len(postulantes) > 0:
                    for z in postulantes:
                        if  "aceptada" == z["estado"]:
                            print("DATOS DE POSTULANTES ACEPTADOS")
                            print(f"Nombre completo: {z["nombre"]} {z["apellido"]}")
                            print(f"Edad: {z["edad"]}")
                            print(f"Correo: {z["correo"]}")
                            print(f"Carrera: {z["carrera"]}")
                            print(f"Promedio: {z["promedio"]}")
                            print(f"Estado: {z["estado"]}")
                else:
                    print("no existen postulantes")
                
            elif x == 5:
                print("DATOS GENERALES")
                print("TOTAL POSTULANTES")
                print(len(postulantes))
                print("PROMEDIO GENERAL")
                for w in postulantes:
                    promedio_acumulador+= w["promedio"]
                    promedio_general = promedio_acumulador/len(postulantes)
                print(promedio_general)
                print("CANTIDAD ACEPTADOS")
                print(aceptados)
                print("CANTIDAD RECHAZADOS")
                print(rechazados)
                print("ESTUDIANTE CON MAYOR PROMEDIO")
                campeon = postulantes[0]
                for estudiante in postulantes:
                    if estudiante["promedio"] > campeon["promedio"]:
                        campeon = estudiante
                print(f"el estudiante con el mayor promedio es: {campeon["nombre"]} con un promedio de {campeon["promedio"]}")
                
            elif x == 6:
                print(f"vacantes totales {vacantes_totales}")
                print(f"vacantes disponibles {vacantes_totales-aceptados}")

            elif x == 7:
                print("muchas gracias")
                flag = False
            else:
                print("esta mal")

        except:
            print("esta mal")
except:
    print("esta mal")
