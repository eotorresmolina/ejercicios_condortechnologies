'''
Test Lista de Mails [Python]
---------------------------
Autor: Torres Molina, Emmanuel O.
Version: 1.1
Descripción:
Programa que sólo sirve para testear y 
verificar el correcto funcionamiento de 
la función: "ordenar_mails" del archivo
"lista_mails".

Para realizar el test copiar la siguiente
línea de código:

from lista_mails import ordenar_mails
'''

from lista_mails import ordenar_mails


if __name__ == "__main__":    
    # Pongo a prueba la función "ordenar_mails".

    # Creo la lista con los mails y el string con el formato de orden.
    mails = ['MailA Flags: A B Fecha de Recepción: 01/02/15',
            'MailB Flags: A Fecha de Recepción: 05/03/15',
            'MailC Flags: B Fecha de Recepción: 06/04/15',
            'MailD Flags: A B Fecha de Recepción: 08/09/15',
            'MailE Flags: C Fecha de Recepción: 07/11/15',
            'MailF Flags: A C Fecha de Recepción: 03/12/15']

    string_orden = 'B-LIFO|!C-FIFO|C-LIFO'

    mails_ordenados = ordenar_mails(mails, string_orden)

    print(mails_ordenados)