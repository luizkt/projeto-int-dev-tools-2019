from kafka import KafkaConsumer
from json import loads
from os import system, name

consumer = KafkaConsumer('entrada',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest')

count = 0

for message in consumer:

    count += 1
    _ = system('clear')
    print(count)
