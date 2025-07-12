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
            if nota_final > 0 and nota_final < 100:
                estudiante = Estudiante(nombre, carne, carrera, nota_final)
            else:
                print("La nota es invalida")
            lista.append(estudiante)
        case 2:
            if len(lista) > 0:
                print("---Lista de Estudiantes---")
                for i in lista:
                    print(f"- Nombre: {i.nombre}, Carnet: {i.carne}, Carrera: {i.carrera}, Nota final: {i.nota_final}")
            else:
                print("No hay estudiantes registrados")
        case 3:
            print("3")
        case 4:
            print("---Promedio---")
        case 5:
            print("Gracias por usar el sistema")
        case _:
            print("Opcion invalida")