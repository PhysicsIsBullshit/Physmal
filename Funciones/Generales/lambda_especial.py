### Este script contiene el factor de lorentz ###

from Constantes.constantes_generales import constantes_generales

c_0 = constantes_generales["c_0"]

def lambda_especial(velocidad):
    resultado = 1./(1. - (velocidad/c_0)**2)**0.5
    return resultado