from datetime import date

class Banco_University:
    def __init__(self, numero_cuenta: str, nombre_cliente: str, fecha_apertura: date, balance_inicial: float = 0.0) -> None:
        self.numero_cuenta: str = numero_cuenta
        self.nombre_cliente: str = nombre_cliente
        self.fecha_apertura: date = fecha_apertura
        self.balance: float = balance_inicial

    def mostrar_info(self) -> None:
        print("\n=== Información de la cuenta ===")
        print(f"Cliente: {self.nombre_cliente}")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Fecha de apertura: {self.fecha_apertura}")
        print(f"Balance actual: Bs{self.balance:.2f}")

    def pago(self, monto: float) -> None:
        if monto > 0:
            self.balance += monto
            print(f"Pago realizado: +Bs{monto:.2f}")
        else:
            print("El monto debe ser positivo.")

    def retiro(self, monto: float) -> None:
        if monto <= 0:
            print("El monto debe ser positivo.")
        elif monto > self.balance:
            print("Fondos insuficientes.")
        else:
            self.balance -= monto
            print(f"Retiro realizado: -Bs{monto:.2f}")

    def mostrar_balance(self) -> None:
        print(f"Balance actualizado: Bs{self.balance:.2f}")


print("=== Crear nueva cuenta bancaria ===")
numero_cuenta = input("Ingrese número de cuenta: ")
nombre_cliente = input("Ingrese nombre del cliente: ")
balance_inicial = float(input("Ingrese balance inicial: "))

cuenta1 = Banco_University(numero_cuenta, nombre_cliente, date.today(), balance_inicial)

cuenta1.mostrar_info()

while True:
    print("\n--- Menú ---")
    print("1. Pago (depositar dinero)")
    print("2. Retiro (sacar dinero)")
    print("3. Mostrar balance")
    print("4. Mostrar información completa")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        monto = float(input("Ingrese monto a depositar: "))
        cuenta1.pago(monto)
    elif opcion == "2":
        monto = float(input("Ingrese monto a retirar: "))
        cuenta1.retiro(monto)
    elif opcion == "3":
        cuenta1.mostrar_balance()
    elif opcion == "4":
        cuenta1.mostrar_info()
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida.")