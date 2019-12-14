# -*- coding: utf-8 -*-

from kafka import KafkaConsumer
#from json import loads
from os import system, name
from enum import Enum

class Estado(Enum):
    AC=0
    AL=1
    AP=2
    AM=3
    BA=4
    CE=5
    DF=6
    ES=7
    GO=8
    MA=9
    MT=10
    MS=11
    MG=12
    PA=13
    PB=14
    PR=15
    PE=16
    PI=17
    RJ=18
    RN=19
    RS=20
    RO=21
    RR=22
    SC=23
    SP=24
    SE=25
    TO=26

consumer = KafkaConsumer('topicoBolsaFamilia' ,
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True)

texto  = ['', '', '', '', '', '', '', '0.00']

lista = [[0 for i in range(3)] for j in range(27)]

for data in Estado:
    lista[data.value][0] = data.name

for message in consumer:

    texto = message.value.replace('"', '').replace(',', '.').split(';')

    #ignorar primeira linha
    if(texto[2] != 'UF'):      
        
        #clear terminal para linux
        _ = system('clear')
        
        lista[Estado[texto[2]].value][1] = lista[Estado[texto[2]].value][1] + float(texto[7])
        lista[Estado[texto[2]].value][2] = lista[Estado[texto[2]].value][2] + 1

        for i in range(27):
            if(lista[i][2] != 0):
                print('%s, R$ %14.2f, %8d' % (lista[i][0], lista[i][1], lista[i][2]))
