class Cuenta:
    def __init__(self, titular, monto):
        self.titular = titular
        self.monto = monto

    def __str__(self):
        return f'Titular: {self.titular}, Monto: {self.monto}'

    def depositar(self, monto):
        self.monto += monto

    def extraer(self, monto):
        if self.monto >= monto:
            self.monto -= monto
        else:
            print('Saldo insuficiente')

    def calcular_interes(self):
        pass

    def acreditar_interes(self):
        pass

class PlazoFijo(Cuenta):
    def __init__(self, titular, monto, interes_anual, plazo):
        super().__init__(titular, monto)
        self.interes_anual = interes_anual
        self.plazo = plazo

    def __str__(self):
        return f'Titular: {self.titular}, Monto: {self.monto}, Interés anual: {self.interes_anual}, Plazo: {self.plazo}'

    def calcular_interes(self):
        interes_ganado = self.monto * (self.interes_anual / 100) * (self.plazo / 365)
        return interes_ganado

    def acreditar_interes(self):
        interes_ganado = self.calcular_interes()
        self.monto += interes_ganado
        return 'Interés acreditado exitosamente.'
    
class CajaDeAhorro(Cuenta):
    def __init__(self, titular, monto):
        super().__init__(titular, monto)

    def __str__(self):
        return f'Titular: {self.titular}, Monto: {self.monto}'
    
class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    def listar_cuentas(self):
        datos_cuentas = []
        for cuenta in self.cuentas:
            datos_cuentas.append(str(cuenta))
        return datos_cuentas

    def mostrar_total_depositos(self):
        total_depositos = 0
        for cuenta in self.cuentas:
            total_depositos += cuenta.monto
        return total_depositos


