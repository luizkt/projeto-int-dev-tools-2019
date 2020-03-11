// Kafka configuration
var kafka = require('kafka-node')
var Producer = kafka.Producer
// instantiate client with as connectstring host:port for  the ZooKeeper for the Kafka cluster
var client = new kafka.KafkaClient({kafkaHost: process.env.KAFKA_CLIENT_ADDRESS || "localhost:9092"})

// name of the topic to produce to
var kafkaTopic = "entrada";

KeyedMessage = kafka.KeyedMessage,
    producer = new Producer(client),
    km = new KeyedMessage('key', 'message'),
    countryProducerReady = false ;

producer.on('ready', function () {
    console.log("Producer for message is ready");
    countryProducerReady = true;
});

producer.on('error', function (err) {
    console.error("Problem with producing Kafka message "+err);
});

function produceKafkaMessage(dataMessage) {
    KeyedMessage = kafka.KeyedMessage,
        dataMessageKM = new KeyedMessage(dataMessage.code, JSON.stringify(dataMessage)),
        payloads = [
            {topic: kafkaTopic, messages: dataMessageKM, partition: 0},
        ];
    if (countryProducerReady) {
        producer.send(payloads, function (err, data) {
            console.log(data);
        });
    } else {
        // the exception handling can be improved, for example schedule this message to be tried again later on
        console.error("sorry, producer is not ready yet, failed to produce message to Kafka.");
    }
}

exports.produceKafkaMessage = produceKafkaMessage;