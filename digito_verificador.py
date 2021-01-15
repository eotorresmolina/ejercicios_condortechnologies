'''
Dígito Verificador [Python]
---------------------------
Autor: Torres Molina, Emmanuel O.
Version: 1.1
Descripción:
Programa que buscar calcular un dígito verificador.
En este caso, para la resolución se hizo uso de la 
librería Numpy aprovechando sus ventajas.
'''

__author__ = "Torres Molina, Emmanuel O."
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"


import numpy as np


def inv_dgts(number):
    '''
    Función que Invierte el orden de los dígitos
    contenidos en el entero "number" recibida como parametro.
    Devuelve un array con los digitos invertidos.
    '''

    # Convierto el número entero en una lista de string cuyos elementos son los dígitos
    digits = list(str(number))

    # Recorro la lista en sentido inverso y la convierto en un numpy array.
    dgts_inv = np.asanyarray(digits[::-1], dtype=np.int64)
    
    return dgts_inv 


def mult_digbysec(digits):
    '''
    Función que recibe un array y realiza 
    una multiplicación con la siguiente 
    secuencia de enteros [2, 3, 4, 5, 6, 7].
    Retorna un número entero igual a la suma de 
    los elementos multiplicados.
    '''

    # Creo un array vacío para contener la secuencia
    # de números.
    sec = np.array([], dtype=np.int64)

    diff = len(digits) - len(sec)

    # Concateno la secuencia con ella misma
    # solo si ---> cant_digitos > nro_digitos_secuencia
    # Repito el proceso hasta que ambos array tenga la misma cant. de elementos.
    while (diff != 0):

        if diff >= len(range(2, 8)):
            sec = np.concatenate((sec, np.arange(2, 8))) # Concateno la secuencia con ella misma!

        else: # Entra en el caso de que la cant de dígitos no sea múltiplo de la longitud de la secuencia.
            sec = np.concatenate((sec, np.arange(2, 2+diff))) 

        diff = len(digits) - len(sec)

    # Realizo la suma del producto de ambos array.
    suma = np.sum(digits * sec)

    return suma


def verificar(value):
    '''
    Función que verifica si el valor ingresado
    por parámetro es 11 o 10.
    Si es 11 se intercambia por 0, si es 10 por 1.
    Retorna el valor intercambiado.
    '''
    value %= 11 # Obtengo el Resto de la división entre el valor y 11.
    result = 11 - value # Le resto de 11 al resultado anterior.

    # Intercambio de valores.
    if result == 11:
        result = 0
    elif result == 10:
        result = 1

    return result 


def digito_verificador(numero):
    '''
    Función principal que toma un número entero
    y mediante ciertos procesos
    calcula el dígito verificador.
    Retorna el valor del dígito verificador.
    '''

    dgts_inv = inv_dgts(numero)
    value = mult_digbysec(dgts_inv)
    result = verificar(value)

    return result


if __name__ == "__main__":

    # Realizo el testeo del correcto funcionamiento del programa.

    numero = int(input('\nPor favor Ingresar un Número "Entero": '))
    
    dgt = digito_verificador(numero)

    print('Resultado de la Verificación: {}\n\n'.format(dgt))

