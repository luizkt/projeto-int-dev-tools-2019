var fs = require('fs');
var parse = require('csv-parse');

var producer = require('./kafka/producer.js');

// name of the csv file
const inputFile = './../../files/bolsaFamiliaTestes.csv';

let RecordArray;

const parser = parse({delimiter: ';'}, function (err, data) {
    RecordArray = data;
    // when all data are available,then process the first one
    // note: array element at index 0 contains the row of headers that we should skip
    handleCurrentRecord(1);
});

// read the inputFile, feed the contents to the parser
fs.createReadStream(inputFile).pipe(parser);

// handle the current record
function handleCurrentRecord(currentRecord) {
    var line = RecordArray[currentRecord];

    line[7] = parseFloat(line[7].replace(',', '.'));

    var record = {
        "mesReferencia": line[0]
        ,"mesCompetencia": line[1]
        ,"uf": line[2]
        ,"codigoMunicipioSiafi": line[3]
        ,"nomeMunicipio": line[4]
        ,"nisFavorecido": line[5]
        ,"nomeFavorecido": line[6]
        ,"valorParcela": line[7]
    };
    console.log(JSON.stringify(record));
    // produce message to Kafka
    producer.produceKafkaMessage(record);

    setTimeout(handleCurrentRecord.bind(null, currentRecord + 1), 1);
}
