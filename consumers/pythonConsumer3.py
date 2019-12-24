from kafka import KafkaConsumer
from json import loads
from os import system, name

consumer = KafkaConsumer('topicoBolsaFamilia',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True)

count = 0

for message in consumer:

    count += 1
    _ = system('clear')
    print(count)
