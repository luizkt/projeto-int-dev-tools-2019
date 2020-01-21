const csv = require('csv-parser');
const fs = require('fs');

var producer = require('./kafka/producer.js');

var dados = [];

fs.createReadStream('./../../files/bolsaFamiliaTestes.csv', 'utf8')
    .pipe(csv({ separator: ';' }))
    .on('data', (row) => {

        row["VALOR PARCELA"] = parseFloat(row["VALOR PARCELA"].replace(',', '.'));

        dados.push(row);
        // row format
        // {
        //     'MÊS REFERÊNCIA': '201901',
        //     'MÊS COMPETÊNCIA': '201809',
        //     'UF': 'PB',
        //     'CÓDIGO MUNICÍPIO SIAFI': '1913',
        //     'NOME MUNICÍPIO': 'SAO JOAO DO RIO DO PEIXE',
        //     'NIS FAVORECIDO': '21057414397',
        //     'NOME FAVORECIDO': 'EGIDIO BANDEIRA DANTAS',
        //     'VALOR PARCELA': 89.1
        // }


    })
    .on('end', () => {
        console.log('CSV file successfully processed');
        producer.sendMessage(dados.toString()).then(
            console.log('Data send to kafka')
        );
    })
