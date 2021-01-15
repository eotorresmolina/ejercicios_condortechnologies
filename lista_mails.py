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


def obtener_datos_mail (mail):
    '''
    Función que recibe el mail en formato
    string y extrae los datos característicos
    del mismo.
    Dichos datos son:
    - fecha
    - flags

    Retorna la fecha y los flags del mail.
    '''

    # Creo una lista con la fecha y los flags.
    mail_split = mail.split('Flags:')

    flags_fecha = mail_split[1].split('Fecha de Recepción')
    flags = flags_fecha[0].split(':')   # Obtengo los FLAGS.

    # Obtengo la fecha separando en dd-mm-aa
    # Invierto la fecha y concateno: dd-mm-aa --> aa-mm-dd --> aammdd
    fecha = flags_fecha[1].split(': ')
    fecha = fecha[1].split('/')
    fecha = fecha[2] + fecha[1] + fecha[0]
    fecha = int(fecha)

    return fecha, flags





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

    Retorna la lista de mails ordenada.
    '''

    d_ordenado = {}     # Diccionario que va a contener los mails ordenados. 
    contador = 1

    # Separo el string para obtener una lista con el formato del orden.
    formato_orden = string_orden.split('|')

    # Recorro la lista para determinar como voy a ordenar los mails.
    for orden in formato_orden:
        fecha_ant = None
        lista_ord = []

        tipo_lista = orden.split('-')
        contenedor_flag = tipo_lista[0]     # Elemento que contiene el FLAG para ordenar.
        
        # Obtengo el tipo de lista: LIFO o FIFO
        tipo_lista = tipo_lista[1]

        if tipo_lista == 'LIFO':

            if '!' in contenedor_flag:
                for mail in mails:
                    fecha_act, flags = obtener_datos_mail(mail)

                    # Entra si el mail no está en la lista ordenada
                    if  not (mail in d_ordenado.values()):  
                        if not(contenedor_flag[1] in flags[0]): 
                            if fecha_ant is None or fecha_ant <= fecha_act:
                                lista_ord.append(mail)  

                            fecha_ant = fecha_act       
            else:
                for mail in mails:
                    fecha_act, flags = obtener_datos_mail(mail)

                    # Entra si el mail no está en la lista ordenada
                    if  not (mail in d_ordenado.values()):  
                        if contenedor_flag in flags[0]: 
                            if fecha_ant is None or fecha_ant <= fecha_act:
                                lista_ord.append(mail)  

                            fecha_ant = fecha_act      
        elif tipo_lista == 'FIFO':
            
            if '!' in contenedor_flag:
                for mail in mails:
                    fecha_act, flags = obtener_datos_mail(mail)

                    # Entra si el mail no está en la lista ordenada
                    if  not (mail in d_ordenado.values()):  
                        if not(contenedor_flag[1] in flags[0]): 
                            if fecha_ant is None or fecha_ant <= fecha_act:
                                lista_ord.append(mail)   

                            fecha_ant = fecha_act       
            else:
                for mail in mails:
                    fecha_act, flags = obtener_datos_mail(mail)

                    # Entra si el mail no está en la lista ordenada
                    if  not (mail in d_ordenado.values()):  
                        if contenedor_flag in flags[0]: 
                            if fecha_ant is None or fecha_ant <= fecha_act:
                                lista_ord.append(mail) 

                            fecha_ant = fecha_act       
                
        for valor, mail in zip(range(contador, contador + len(lista_ord)), lista_ord[::-1]):
            d_ordenado[valor] = mail

            contador += len(lista_ord)

    # Obtengo la lista de mails ordenados.
    mails_ordenados = [mail for mail in d_ordenado.values()]

    return mails_ordenados