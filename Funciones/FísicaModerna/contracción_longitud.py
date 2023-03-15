### Este script calcula la contracción de la longitud causada por la relatividad especial ###

from Funciones.Generales.lambda_especial import lambda_especial

def contracción_longitud(longitud_propia, velocidad):
    resultado = longitud_propia/lambda_especial(velocidad)
    return resultado

def input_contracción_longitud():
    print("\nHay dos sistemas de referencia, A y B. "
        "El sistema B se mueve con velocidad constante v relativo al sistema A (sistema en 'reposo'). "
        "Desde el sistema B se mide una distancia (longitud propia) y se"
        "quiere medir dicha distancia desde el sistema A.\n")

    velocidad = float(input("Escriba la velocidad v (m/s): "))
    longitud_propia = float(input("Escriba la longitud propia (metros): "))

    longitud_prima = contracción_longitud(longitud_propia, velocidad)

    print("La distancia o longitud medida por el sistema en 'resposo' es {:.2f} m.".format(longitud_prima))