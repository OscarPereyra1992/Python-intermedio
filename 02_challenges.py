##Challenges

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz(number):
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

##fizzbuzz(100)

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def anagrama(first_string: str,second_string: str):
    
    if len(first_string) == len(second_string):
        for i in first_string:
            if i not in second_string:
                return False
            else:
                return True
    else:
       return False 
print(anagrama("españa","apañes"))