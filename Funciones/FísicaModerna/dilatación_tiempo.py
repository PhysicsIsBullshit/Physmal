### Este script calcula la dilatación del tiempo causada por la relatividad especial ###

from Funciones.Generales.lambda_especial import lambda_especial

def dilatación_tiempo(tiempo_propio, velocidad):
    resultado = lambda_especial(velocidad) * tiempo_propio
    return resultado

def input_dilatación_tiempo():
    print("\nHay dos sistemas de referencia, A y B. "
        "El sistema B se mueve con velocidad constante v relativo al sistema A (sistema en 'reposo'). "
        "Desde el sistema B se mide el tiempo de un suceso (tiempo propio) y se"
        "quiere medir dicho tiempo desde el sistema A.\n")

    velocidad = float(input("Escriba la velocidad v (m/s): "))
    tiempo_propio = float(input("Escriba el tiempo propio (segundos): "))

    tiempo_prima = dilatación_tiempo(tiempo_propio, velocidad)

    print("El tiempo medido por el sistema en 'reposo' es {:.2f} s.".format(tiempo_prima))
    