def ordenar_mails(mails, string_orden):

    d_ordenado = {}
    contador = 1

    # Separo el string para obtener una lista con el formato del orden.
    formato_orden = string_orden.split('|')

    # Recorro la lista para determinar como voy a ordenar los mails.
    for orden in formato_orden:
        fecha_ant = None
        lista_ord = []

        tipo_lista = orden.split('-')

        contenedor_flag = tipo_lista[0]     # Elemento que contiene el string relacionado con el FLAG 
        
        # Obtengo el tipo de lista: LIFO o FIFO
        tipo_lista = tipo_lista[1]

        if tipo_lista == 'LIFO':
            
            # Pregunto por el caracter '!'
            if '!' in contenedor_flag:
                for mail in mails:

                    mail_split = mail.split('Flags:')

                    # Obtengo el FLAG del mail actual.
                    flags_fecha = mail_split[1].split('Fecha de Recepción')
                    flags = flags_fecha[0].split(':')

                    # Obtengo la fecha del mail actual separando en dd-mm-aa
                    # Invierto la fecha y concateno: dd-mm-aa --> aa-mm-dd
                    # Convierto el string en entero.
                    fecha_act = flags_fecha[1].split(': ')
                    fecha_act = fecha_act[1].split('/')
                    fecha_act = fecha_act[2] + fecha_act[1] + fecha_act[0]
                    fecha_act = int(fecha_act)

                    # Entra si el mail no está en la lista ordenada
                    if  not (mail in d_ordenado.values()):  
                        if not(contenedor_flag[1] in flags[0]): 
                            if lista_ord == []:
                                lista_ord.append(mail)
                            else:
                                if fecha_ant <= fecha_act:
                                    lista_ord.append(mail)  

                            fecha_ant = fecha_act       
                
                for valor, mail in zip(range(contador, contador + len(lista_ord)), lista_ord[::-1]):
                    d_ordenado[valor] = mail

                contador += len(lista_ord)
            
            else:
                for mail in mails:

                    mail_split = mail.split('Flags:')

                    # Obtengo el FLAG del mail actual.
                    flags_fecha = mail_split[1].split('Fecha de Recepción')
                    flags = flags_fecha[0].split(':')

                    # Obtengo la fecha del mail actual separando en dd-mm-aa
                    # Invierto la fecha y concateno: dd-mm-aa --> aa-mm-dd
                    # Convierto el string en entero.
                    fecha_act = flags_fecha[1].split(': ')
                    fecha_act = fecha_act[1].split('/')
                    fecha_act = fecha_act[2] + fecha_act[1] + fecha_act[0]
                    fecha_act = int(fecha_act)

                    # Entra si el mail no está en la lista ordenada
                    if  not (mail in d_ordenado.values()):  
                        if contenedor_flag in flags[0]: 
                            if lista_ord == []:
                                lista_ord.append(mail)
                            else:
                                if fecha_ant <= fecha_act:
                                    lista_ord.append(mail)  

                            fecha_ant = fecha_act       
                
                for valor, mail in zip(range(contador, contador + len(lista_ord)), lista_ord[::-1]):
                    d_ordenado[valor] = mail

                contador += len(lista_ord)
        
        elif tipo_lista == 'FIFO':
            
            # Pregunto por el caracter '!'
            if '!' in contenedor_flag:
                for mail in mails:

                    mail_split = mail.split('Flags:')

                    # Obtengo el FLAG del mail actual.
                    flags_fecha = mail_split[1].split('Fecha de Recepción')
                    flags = flags_fecha[0].split(':')

                    # Obtengo la fecha del mail actual separando en dd-mm-aa
                    # Invierto la fecha y concateno: dd-mm-aa --> aa-mm-dd
                    # Convierto el string en entero.
                    fecha_act = flags_fecha[1].split(': ')
                    fecha_act = fecha_act[1].split('/')
                    fecha_act = fecha_act[2] + fecha_act[1] + fecha_act[0]
                    fecha_act = int(fecha_act)

                    # Entra si el mail no está en la lista ordenada
                    if  not (mail in d_ordenado.values()):  
                        if not(contenedor_flag[1] in flags[0]): 
                            if lista_ord == []:
                                lista_ord.append(mail)
                            else:
                                if fecha_ant >= fecha_act:
                                    lista_ord.append(mail)  

                            fecha_ant = fecha_act       
                
                for valor, mail in zip(range(contador, contador + len(lista_ord)), lista_ord[::-1]):
                    d_ordenado[valor] = mail

                contador += len(lista_ord)
            
            else:
                for mail in mails:

                    mail_split = mail.split('Flags:')

                    # Obtengo el FLAG del mail actual.
                    flags_fecha = mail_split[1].split('Fecha de Recepción')
                    flags = flags_fecha[0].split(':')

                    # Obtengo la fecha del mail actual separando en dd-mm-aa
                    # Invierto la fecha y concateno: dd-mm-aa --> aa-mm-dd
                    # Convierto el string en entero.
                    fecha_act = flags_fecha[1].split(': ')
                    fecha_act = fecha_act[1].split('/')
                    fecha_act = fecha_act[2] + fecha_act[1] + fecha_act[0]
                    fecha_act = int(fecha_act)

                    # Entra si el mail no está en la lista ordenada
                    if  not (mail in d_ordenado.values()):  
                        if contenedor_flag in flags[0]: 
                            if lista_ord == []:
                                lista_ord.append(mail)
                            else:
                                if fecha_ant >= fecha_act:
                                    lista_ord.append(mail)  

                            fecha_ant = fecha_act       
                
                for valor, mail in zip(range(contador, contador + len(lista_ord)), lista_ord[::-1]):
                    d_ordenado[valor] = mail

                contador += len(lista_ord)

    mails_ordenados = [mail for mail in d_ordenado.values()]

    return mails_ordenados


if __name__ == "__main__":
    
    mails = ['MailA Flags: A B Fecha de Recepción: 01/02/15',
            'MailB Flags: A Fecha de Recepción: 05/03/15',
            'MailC Flags: B Fecha de Recepción: 06/04/15',
            'MailD Flags: A B Fecha de Recepción: 08/09/15',
            'MailE Flags: C Fecha de Recepción: 07/11/15',
            'MailF Flags: A C Fecha de Recepción: 03/12/15']

    string_orden = 'B-LIFO|!C-FIFO|C-LIFO'

    d = ordenar_mails(mails, string_orden)

    print(d)