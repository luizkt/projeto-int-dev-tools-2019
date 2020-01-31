# -*- coding: utf-8 -*-

from kafka import KafkaConsumer
import json
from os import system, name

# To consume latest messages and auto-commit offsets

consumer = KafkaConsumer('entrada',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')))

count = 0

row  = json.loads('{"mesReferencia":"","mesCompetencia":"","uf":"","codigoMunicipioSiafi":"","nomeMunicipio":"","nisFavorecido":"","nomeFavorecido":"","valorParcela":0}')
row2 = json.loads('{"mesReferencia":"","mesCompetencia":"","uf":"","codigoMunicipioSiafi":"","nomeMunicipio":"","nisFavorecido":"","nomeFavorecido":"","valorParcela":0}')
row3 = json.loads('{"mesReferencia":"","mesCompetencia":"","uf":"","codigoMunicipioSiafi":"","nomeMunicipio":"","nisFavorecido":"","nomeFavorecido":"","valorParcela":0}')

for message in consumer:

    row = message.value

    if((row["valorParcela"] > row3["valorParcela"]) and (row["valorParcela"] > row2["valorParcela"])):
        row3 = row

    elif((row2["valorParcela"] > row3["valorParcela"]) and (row2["valorParcela"] > row3["valorParcela"])):
        row3 = row2

    _ = system('clear')

    count += 1

    print(str(row3["nisFavorecido"]), str(row3["nomeFavorecido"]), str(row3["valorParcela"]), str(row3["nomeMunicipio"]), str(row3["uf"]), count)

    row2 = row

