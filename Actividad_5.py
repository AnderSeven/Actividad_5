from multiprocessing.queues import JoinableQueue
lista = []
class Estudiante:
    def __init__(self, nombre, carne, carrera, nota_final):
        self.nombre = nombre
        self.carne = carne
        self.carrera = carrera
        self.nota_final = nota_final

a = True
while True:
    print("---Menu---")
    print("1. Registrar estudiante")
    print("2. Mostrar la lista de estudiantes")
    print("3. Buscar estudiante")
    print("4. Calcular el promedio de todos los estudiantes")
    print("5. Salir")
    op = int(input("Elija una opcion: "))
    match   op:
        case 1:
            print("---Registro de estudiantes---")
            nombre = input("Ingrese el nombre del estudiante: ")
            carne = int(input("Ingrese el carnet: "))
            carrera = input("Ingrese la carrera: ")
            nota_final = float(input("Ingrese la nota final: "))
            estudiante = Estudiante(nombre, carne, carrera, nota_final)
            lista.append(estudiante)
        case 2:
            if len(lista) > 0:
                print("---Lista de Estudiantes---")
                for i in lista:
                    print(f"- Nombre: {i.nombre}, Carnet: {i.carne}, Carrera: {i.carrera}, Nota final: {i.nota_final}")
            else:
                print("No hay estudiantes registrados")
        case 3:
            if len(lista) > 0:
                carnet_buscar = int(input("Ingrese el carnet: "))
                encontrado = False
                for i in lista:
                    if i.carne == carnet_buscar:
                        print(f"Nombre: {i.nombre}, Carnet: {i.carne}, Carrera: {i.carrera}, Nota final: {i.nota_final}")
                        encontrado = True
                        break
                if encontrado == False:
                    print("No se encontro al estudiante")
            else:
                print("No hay estudiantes registrados")
        case 4:
            print("---Promedio---")
        case 5:
            print("Gracias por usar el sistema")
        case _:
            print("Opcion invalida")