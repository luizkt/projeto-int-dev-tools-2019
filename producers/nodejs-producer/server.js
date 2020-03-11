const express = require('express');
const app = express();
const port = process.env.APP_PORT || 3000;
const parser = require('./kafka/parser.js');

// name of the csv file
const inputFile = './files/bolsaFamiliaTestes.csv';

app.get('/load', function (request, response) {
    console.log("Starting producer loader");
    parser.execute(inputFile);

    response.status(202).send();
        /*.then(() => {
        response.status(204).send();
    }).catch((error) => {
        response.status(500).send(error);
    });*/
})

app.listen(port, () => {
    console.log(`Server is up in port ${port}`);
});