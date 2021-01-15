'''
Lista de Mails [Python]
---------------------------
Autor: Torres Molina, Emmanuel O.
Version: 1.1
Descripción:
Funciones que ordenan una lista de mails obtenidos
de un mail server IMAP.
Un string es el encargado de indicar de qué manera
se desea ordenar dicha lista.
Dicho orden va a ser respecto de su fecha de recepción.

Se utilizaron los métodos de la clase "dict", "list"
y "str" para el desarrollo.

Considerar para el desarrollo de la función principal
lo siguiente: 
- Cada mail llega con el siguiente formato
  en forma de string, por ej:
  "MailD Flags: A B Fecha de Recepción: 08/09/15"
- La lista original de mails está ordenada
  de la más antigua a la más actual según
  la fecha de recepción.

NOTA: Sólo se debe llamar a la función 
"ordenar_lista" <--- función principal
Las demás funciones sólo sirven para el procesamiento
y desarrollo de la función principal.
'''

__author__ = "Torres Molina, Emmanuel O."
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"


def obtener_flags_mail (mail):
    '''
    Función que recibe el mail en formato
    string y extrae los flags del mismo.
    Retorna los flags del mail.
    '''

    # Creo una lista con la fecha y los flags.
    mail_split = mail.split('Flags:')

    # Genero la lista "flags" de un único elemento
    flags_fecha = mail_split[1].split('Fecha de Recepción')
    flags = flags_fecha[0].split(':')   # Obtengo los FLAGS.

    return flags[0]  # Retorno el elemento de la lista


def ordenar_mails(mails, string_orden):
    '''
    Función principal que permite ordenar
    la lista "mails".
    - Cada mail dentro de la lista es un string 
    que tiene el siguiente formato: 
    "MailD Flags: A B Fecha de Recepción: 08/09/15"
    - El string_orden tiene el formato: 
    [!]<FLAG>-(FIFO|LIFO), por ej:
    "B-LIFO|!C-FIFO|C-LIFO"

    La forma en la que se ordena es respecto
    a su fecha de recepción

    Retorna la lista de mails ordenada.
    '''

    d_ordenado = {}     # Diccionario que va a contener los mails ordenados. 
    contador = 1

    # Separo el string para obtener una lista con el formato del orden.
    formato_orden = string_orden.split('|')

    # Recorro la lista para determinar como voy a ordenar los mails.
    for orden in formato_orden:
        lista_ord = []

        tipo_lista = orden.split('-')
        contenedor_flag = tipo_lista[0]     # Elemento que contiene el FLAG para ordenar.
        
        # Obtengo el tipo de lista: LIFO o FIFO
        tipo_lista = tipo_lista[1]

        # Obtengo los datos(fecha y flags) de los mails. 
        flags = [obtener_flags_mail(mail) for mail in mails]

        if tipo_lista == 'LIFO': # En este caso ordeno de mayor a menor

            if '!' in contenedor_flag:
                # Filtro aquellos mails cuyo flag no tengan el flag de orden
                mails_filtrados = [mail for (mail, flag) in zip(mails, flags) 
                                    if not(contenedor_flag[1] in flag)]
            else:
                # Filtro aquellos mails cuyo flag tengan el flag de orden
                mails_filtrados = [mail for (mail, flag) in zip(mails, flags)
                                    if (contenedor_flag in flag)]

            lista_ord = [mail for mail in mails_filtrados[::-1] if not (mail in d_ordenado.values())]
   
        elif tipo_lista == 'FIFO': # En este caso ordeno de menor a mayor

            if '!' in contenedor_flag:
                # Filtro aquellos mails cuyo flag no tengan el flag de orden
                 mails_filtrados = [mail for (mail, flag) in zip(mails, flags) 
                                    if not(contenedor_flag[1] in flag)]
            else:
                # Filtro aquellos mails cuyo flag tengan el flag de orden
                mails_filtrados = [mail for (mail, flag) in zip(mails, flags)
                                    if (contenedor_flag in flag)]
   
            lista_ord = [mail for mail in mails_filtrados if not (mail in d_ordenado.values())]

        # Almaceno los mails en forma ordenada en el diccionario --> {1: 'MailX', {2: 'MailY}, ...}
        for valor, mail in zip(range(contador, contador + len(lista_ord)), lista_ord):
            d_ordenado[valor] = mail

        contador += len(lista_ord)

    # Obtengo la lista de mails ordenados.
    mails_ordenados = [mail for mail in d_ordenado.values()]

    return mails_ordenados