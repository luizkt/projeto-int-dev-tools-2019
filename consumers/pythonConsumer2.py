# -*- coding: utf-8 -*-

from kafka import KafkaConsumer
from json import loads
from os import system, name

# To consume latest messages and auto-commit offsets

consumer = KafkaConsumer('entrada',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True)

count = 0

texto  = ['', '', '', '', '', '', '', '0.00']
texto2 = ['', '', '', '', '', '', '', '0.00']
texto3 = ['', '', '', '', '', '', '', '0.00']

for message in consumer:

    texto = message.value.replace('"', '').replace(',', '.').split(';')

    if ((texto[2] != 'UF') and (texto2[2] != 'UF')):

        if((float(texto[7]) > float(texto3[7])) and (float(texto[7]) > float(texto2[7]))):
            texto3 = texto

        elif((float(texto[7]) > float(texto3[7])) and (float(texto2[7]) > float(texto3[7]))):
            texto3 = texto2

        _ = system('clear')
        print(texto3[5], texto3[6], texto3[7], texto3[4], texto3[2])

    else:
        if (texto2[2] == 'UF'):
            print(texto[5], texto[6], texto[7], texto[4], texto[2])

    texto2 = texto

    count += 1
