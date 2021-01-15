'''
Billetes [Python]
---------------------------
Autor: Torres Molina, Emmanuel O.
Version: 1.1
Descripción:
Programa que dado una suma en pesos se desea
determinar cuál es la mejor manera de pagar
dicha suma dependiendo la cantidad de billetes
que se tengan en cierta "caja" o "cajero".

Se realizó dicho programa usando mayormente 
métodos pertenecientes a la clase "list" y "dict".

En este caso consideré que los billetes y su cantidad
están contenidos en un diccionario.
'''

__author__ = "Torres Molina, Emmanuel O."
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"


def dinero_caja (caja):
    '''
    Función que analiza el dinero que hay disponible
    en la caja.
    Recibe como parámetro, en este caso, un objeto
    de la clase "dict" que contiene los billetes y
    su cantidad.
    Retorna una lista con los billetes disponibles, la
    cantidad de cada uno y una variable 
    entera con el dinero total que hay.
    '''

    # Lista que Genera aquellos billetes que hay disponible en la caja.
    # Esto es cuya cantidad sea distinta de 0.
    billetes_disponibles = [[int(valor[0]), valor[1]] for valor in caja.items() if valor[1] != 0]
    
    # Lista que obtiene la cantidad de plata por billete para obtener el dinero total
    # que hay en la caja.
    dinero_disponible = [int(valor[0])*valor[1] for valor in caja.items() if valor[1] != 0]
    dinero_total = sum(dinero_disponible) 

    return billetes_disponibles, dinero_total


def pagar_suma (cant_pagar=0, billetes_disponibles=0, dinero_total=0):
    '''
    Función que según la cantidad de dinero a pagar
    recibida como parámetro, se determina que billetes
    y cuantos se deben entregar.
    Retorna una lista con los billetes entregados y su 
    cantidad.
    '''

    # Lista que va a contener los billetes que se entregan.
    billetes_entregados = [] 

    if cant_pagar != 0:

        # Si el monto a pagar es mayor al dinero total que hay en la caja
        # entonces pago con lo que hay disponible.
        if cant_pagar > dinero_total:
            cant_pagar = dinero_total

        # Me quedo con aquellos billetes menores y/o igual al monto a pagar.
        filtro_billetes = [billete for billete in billetes_disponibles if billete[0] <= cant_pagar]

        for billete in filtro_billetes:

            cantidad = 0    # Indica que cantidad de billetes se está entregando.

            # Al monto a pagar le resto el billete siempre y cuando
            # sea menor y haya disponibilidad del mismo. 
            while (cant_pagar >= billete[0] and billete[1] != 0):
                cant_pagar -= billete[0]
                cantidad += 1

            if cantidad != 0: 
                billetes_entregados.append([billete[0], cantidad]) # Cargo los billetes y su cantidad.

            # Entra si el monto fue pagado
            if cant_pagar == 0:
                break

    return billetes_entregados


# def actualizar_caja (caja, billetes):
#     '''
#     Función que actualiza la caja con los billetes
#     que quedaron luego de haber pagado el monto.
#     '''

#     for billete in billetes:

#         # Realizo la diferencia entre lo que había y lo que se entregó.
#         # Actualizo la caja.
#         diferencia = caja[str(billete[0])] - billete[1]      
#         caja[str(billete[0])] = diferencia  


if __name__ == "__main__":
    # Realizo el testeo del correcto funcionamiento del programa.

    caja = {"100": 2, "50": 1, "20": 0, "10": 3, "5": 0, "1": 0}
    monto_pagar = 70

    billetes_disponibles, dinero_total = dinero_caja(caja)
    billetes_entregados = pagar_suma(monto_pagar, billetes_disponibles, dinero_total)

    print(billetes_entregados)
