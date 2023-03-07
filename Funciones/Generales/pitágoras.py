## Comentario

def input_pit():
    x = int(input("Ingrese los lados a.\n"))
    y = int(input("Ingrese los lados b.\n"))
    return [x, y]

def pitagoras(a, b):
    c = (a**2 + b**2)**0.5
    return c