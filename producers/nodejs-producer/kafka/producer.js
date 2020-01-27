const { Kafka } = require('kafkajs')

const kafka = new Kafka({
    clientId: 'my-app',
    brokers: ['localhost:9092']
})

const producer = kafka.producer()

const sendMessage = (data) => {
    return producer.send({
        topic: 'entrada',
        messages: [
            {value: data},
        ],
    })
    .then(console.log)
    .catch(e => console.error(`[example/producer] ${e.message}`, e))
}

const run = async (data) => {
    await producer.connect()
    setInterval(sendMessage(data), 3000)
}

exports.run = run;