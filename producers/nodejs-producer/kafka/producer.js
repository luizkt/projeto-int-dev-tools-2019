const { Kafka } = require('kafkajs')

const kafka = new Kafka({
    clientId: 'my-app',
    brokers: ['localhost:9092']
})

const producer = kafka.producer()

const sendMessage = async (data) => {
    // Producing
    await producer.connect()
    await producer.send({
        topic: 'entrada',
        messages: [
            {value: data},
        ],
    })
}

exports.sendMessage = sendMessage;