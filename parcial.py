def verificar_multiplos(num1, num2):
  # profe, coloco en comentarios la funcionalidades de cada estructura de control
    if num2 != 0 and num1 % num2 == 0:             # este "if " verifica si num1 es múltiplo de num2
        print(f"{num1} es múltiplo de {num2}")
    #aquí, uso que el modulo o residuo de una division, ya que si el residuo es 0, significa que el primer número es divisible por el segundo, en pocas palabras es multiplo
    elif num1 != 0 and num2 % num1 == 0:
        print(f"{num2} es múltiplo de {num1}")      # el elif verifica si num2 es múltiplo de num1, tal cual como lo pide en el
                                                    # documento
    else:
        print(f"No hay múltiplos entre {num1} y {num2}")  


pares_de_numeros = [
    (7919, 2),
    (840, 210),
    (678223072849, 23),
    (1299827, 104729),
    (104728, 13)
]


for par in pares_de_numeros:
    verificar_multiplos(par[0], par[1])
#aqui el for recorre el array para sacar los pares y operarlos
