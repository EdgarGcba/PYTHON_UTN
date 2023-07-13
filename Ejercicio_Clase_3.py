class Lado:
    def __init__(self, longitud):
        self.longitud = longitud


class Figura:
    lado1
    lado2
    lado3
    
    def __init__(self,lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
                        
    def perimetro(self):
        return sum(lado.longitud for lado in self.lados)


class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3):
        super().__init__(lado1, lado2, lado3)


class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__(lado, lado, lado)
        self.lado4 = lado


class Rectangulo(Figura):
    def __init__(self, lado1, lado2, ):
        super().__init__(lado1, lado2, lado1)
        self.lado4 = lado2


# Ejemplo de uso
lado1 = Lado(3)
lado2 = Lado(4)
lado3 = Lado(5)

triangulo = Triangulo(lado1, lado2, lado3)
print("Perímetro del triángulo:", triangulo.perimetro())

lado_cuadrado = Lado(4)
cuadrado = Cuadrado(lado_cuadrado)
print("Perímetro del cuadrado:", cuadrado.perimetro())

lado1_rectangulo = Lado(3)
lado2_rectangulo = Lado(5)
rectangulo = Rectangulo(lado1_rectangulo, lado2_rectangulo)
print("Perímetro del rectángulo:", rectangulo.perimetro())
