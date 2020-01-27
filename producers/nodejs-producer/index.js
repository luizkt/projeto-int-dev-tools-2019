const csv = require('csv-parser');
const fs = require('fs');

var producer = require('./kafka/producer.js');

var dados = [];
index = 0;

fs.createReadStream('./../../files/bolsaFamiliaTestes.csv', 'utf8')
    .pipe(csv({ separator: ';' }))
    .on('data', async (row) => {

        row["VALOR PARCELA"] = parseFloat(row["VALOR PARCELA"].replace(',', '.'));

        dados.push(row);
        await producer.run(JSON.stringify(row)).catch(e => console.error(`[example/producer] ${e.message}`, e));
    })
    .on('end', () => {
        console.log('CSV file successfully processed');
    })
