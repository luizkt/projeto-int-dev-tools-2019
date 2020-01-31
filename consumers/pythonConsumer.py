# -*- coding: utf-8 -*-

from kafka import KafkaConsumer
import json
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

consumer = KafkaConsumer('entrada',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')))

lista = [[0 for i in range(3)] for j in range(27)]

#initialize table
for data in Estado:
    lista[data.value][0] = data.name
    lista[data.value][1] = 0.0
    lista[data.value][2] = 0

for message in consumer:

    row = message.value

    #clear terminal para linux
    _ = system('clear')

    lista[Estado[row["uf"]].value][1] = lista[Estado[row["uf"]].value][1] + row["valorParcela"]
    lista[Estado[row["uf"]].value][2] = lista[Estado[row["uf"]].value][2] + 1

    for i in range(27):
        if(lista[i][2] != 0):
            print('%s, R$ %14.2f, %8d' % (lista[i][0], lista[i][1], lista[i][2]))
