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
    op = int(input("Elija una opcion: "))
    match   op:
        case 1:
            nombre = input("Ingrese el nombre del estudiante: ")
            carne = int(input("Ingrese el carnet: "))
            carrera = input("Ingrese la carrera: ")
        case 2:
        case 3:
        case 4: