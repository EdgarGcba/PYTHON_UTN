class Persona:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre

    def __str__(self):
        return f"Persona con DNI {self.dni} y nombre {self.nombre}"

class Docente(Persona):
    def __init__(self, dni, nombre, legajo, sueldo):
        super().__init__(dni, nombre)
        self.legajo = legajo
        self.sueldo = sueldo

    def __str__(self):
        return   super().__str__() + f"\nLegajo {self.legajo} \nSueldo {self.sueldo}" 

class Alumno(Persona):
    def __init__(self, dni, nombre, legajo, nota1, nota2):
        super().__init__(dni, nombre)
        self.legajo = legajo
        self.nota1 = nota1
        self.nota2 = nota2

    def __str__(self):
        return super().__str__()  + f"legajo {self.legajo}, nota1 {self.nota1} y nota2 {self.nota2}"

    def getPromedio(self):
        return (self.nota1 + self.nota2) / 2
    
class Curso:
    def __init__(self, nombre, docente, alumnos):
        self.nombre = nombre
        self.docente = docente
        self.alumnos = alumnos

    def listado_alumnos(self):
        for alumno in self.alumnos:
            str_alumnos += f'\n{alumno.legajo} - ({alumno.nombre}) '

    def cantidad_regulares(self):
        cantidad = 0
        for alumno in self.alumnos:
            if alumno.nota1 >= 4 and alumno.nota2 >= 4:
                cantidad += 1
        return cantidad

    def promedio_total(self):
        
        if len(self.alumnos == 0 ):
            return 0
        cantidad_alumnos = len(self.alumnos)
        for alumno in self.alumnos:
            suma_notas += alumno.getPromedio()
        return suma_notas / cantidad_alumnos

