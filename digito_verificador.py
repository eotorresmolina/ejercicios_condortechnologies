import numpy as np


def inv_dgts(digits):
    '''
    Función que Invierte el orden de los digitos
    contenidos en la lista "digits" recibida como parametro 
    en sentido inverso
    Devuelve un array con los digitos invertidos.
    '''

    # Recorro la lista en sentido inverso y la convierto en un numpy array.
    dgts_inv = np.asanyarray(digits[::-1], dtype=np.int64)
    
    return dgts_inv 


def mult_digbysec(digits):
    '''
    Función que recibe un array y realiza 
    una multiplicación con la siguiente 
    secuencia de enteros [2, 3, 4, 5, 6, 7].
    Retorna la suma de los elementos multiplicados.
    '''

    # Creo un array vacío para contener la secuencia
    # de números.
    sec = np.array([], dtype=np.int64)

    # Realizo la diferencia entre el número de digitos y la
    # longitud de la secuencia.
    diff = len(digits) - len(sec)

    # Realizo un concatenado de la secuencia en caso de que
    # de que la misma haya acabado ---> cant_digitos > nro_digitos_secuencia
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


if __name__ == "__main__":

    digitos = list(str(input('\nPor favor Ingrese Dígitos "Enteros" que desee: ')))
    
    dgts_inv = inv_dgts(digitos)
    value = mult_digbysec(dgts_inv)
    result = verificar(value)

    print('Resultado de la Verificación: {}\n\n'.format(result))

