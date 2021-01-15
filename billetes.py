def inicializar_caja ( ):
    '''
    Función que permite inicializar la 
    cantidad de billetes de cada denominación
    en la caja.
    '''
    caja = {"100": 2, "50": 1, "20": 0, "10": 3, "5": 0, "1": 0}

    return caja


def dinero_caja (caja):
    '''
    Función que analiza el dinero que hay disponible
    en la caja.
    Retorna una lista con los billetes disponibles y la
    cantidad que hay de cada uno y el dinero total que hay 
    en la caja.
    '''

    # Lista que Genera aquellos billetes que hay disponible en la caja.
    # Esto es cuya cantidad sea distinta de 0.
    billetes_disponibles = [[int(valor[0]), valor[1]] for valor in caja.items() if valor[1] != 0]
    
    # Lista que obtiene la cantidad de plata por billete
    dinero_disponible = [int(valor[0])*valor[1] for valor in caja.items() if valor[1] != 0]

    dinero_total = sum(dinero_disponible) # Obtengo la suma total.

    return billetes_disponibles, dinero_total


def pagar_suma (cant_pagar=0, billetes_disponibles=0, dinero_total=0):
    '''
    Función que según la cantidad de dinero a pagar
    recibida como parámetro, se determina que billetes
    y su cantidad se deben entregar.
    Retorna los billetes entregados y su cantidad.
    '''

    billetes_entregados = [] # Lista vacía

    if cant_pagar != 0:

        # Me quedo con aquellos billetes menores y/o igual al monto a pagar.
        filtro_billetes = [billete for billete in billetes_disponibles if billete[0] <= cant_pagar]

        for dinero in filtro_billetes:
            cantidad = 0

            while (cant_pagar >= dinero[0] and dinero[1] != 0):
                cant_pagar -= dinero[0]
                cantidad += 1

            if cantidad != 0: # -- if agregado
                billetes_entregados.append([dinero[0], cantidad])

            if cant_pagar == 0:
                break

    #filtrado_billetes_entregados = [valor for valor in billetes_entregados if valor[1] != 0]

    #return filtrado_billetes_entregados

    return billetes_entregados


def actualizar_caja (caja, billetes):
    '''
    Función que actualiza la caja según
    los billetes entregados.
    '''

    # Recorro la lista de billetes entregados
    for billete in billetes:

        # Realizo la diferencia entre lo que había y lo que se entregó
        diferencia = caja[str(billete[0])] - billete[1] 
        
        caja[str(billete[0])] = diferencia  # Actualizo la cantidad nueva


if __name__ == "__main__":

    caja = inicializar_caja()

    print('\n{}\n'.format(caja))

    billetes_disponibles, dinero_total = dinero_caja(caja)

    billetes_entregados = pagar_suma(70, billetes_disponibles, dinero_total)

    actualizar_caja(caja, billetes_entregados)

    #print('\n{}\n'.format(caja))

    print(billetes_entregados)
