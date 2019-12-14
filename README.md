# projeto-int-dev-tools-2019
Utilização de consumidores e produtores utilizando o Kafka


Descrição: 
Crie um produtor para carregar os dados do arquivo do bolsa família (referente ao período de janeiro/2019) para um Topic no Kafka e implemente 3 consumidores que irão nos ajudar a responder algumas perguntas. 

Link para download do arquivo: http://www.portaltransparencia.gov.br/download-de-dados/bolsa-familia-pagamentos 

Layout do arquivo: MÊS_REFERÊNCIA, MÊS_COMPETÊNCIA, UF, CÓDIGO_MUNICÍPIO_SIAFI, NOME_MUNICÍPIO, NIS_FAVORECIDO, NOME_FAVORECIDO, VALOR_PARCELA. 

Produtor: Carregar os dados de um arquivo .csv para um Topic do kafka.  

Consumidores: 

    1) Exibir [UF] + [somar da parcela] + [qtd de beneficiários] até o momento; 

    2) Mostrar dados do beneficiário que tenha a maior parcela até o momento: 

    a. NIS_FAVORECIDO 

    b. NOME_FAVORECIDO 

    c. VALOR_PARCELA 

    d. NOME_MUNICIPIO 

    e. UF 

    3) Quantidade de registros lidos do Topic: 

    Retornar um valor Inteiro para a quantidade de registros consumidos.  

Obs. Consumidor 1: Deve exibir no console o resultado calculado para cada registro consultado do Topic. Desta forma, a quantidade de UF retornadas no console vai aumentar na medida que forem processados os registros dos beneficiários vinculados a novas UFs. 

Obs. Consumidor 2: Ele deve exibir o primeiro beneficiário consultado como sendo o de maior parcela, e usar esse valor para verificar se é menor ou maior que o próximo registro e somente imprimir no console quando obter uma parcela superior. 


Artefatos para Entrega:  

   1) Link do repositório do projeto no GitHub. 

   2) README.md completo e detalhado. 

    a. Uma Big Picture da solução. 

    b. Screenshot do resultado dos consumidores. 

    c. Screenshot do Trello com as atividades necessárias para a implementação dos consumidores e produtor. 

 

Importante: 

    > Use pelo menos duas linguagens neste projeto, por exemplo: produtor em NodeJS e os consumidores em Python. (podem usar Java, C#, Go, etc..) 

    > Descrever de uma maneira bem clara no README.md do seu projeto para que possa ser feito o pull e execução do projeto. Deve conter as configurações do Kafka, criação do Topic, instalação/configuração do ambiente de execução. Assim como os screenshots dos consumidores e das atividades no Trello. Não esqueça de escrever o objetivo do projeto para que a comunidade de desenvolvedores possa entender e quem sabe fazer um fork do seu repositório. 

    > Podem usar alguma Base de Dados NoSQL ou Relacional para carregar o arquivo e então conectar na base com o Produtor (não esqueça de descrever esse processo). O PDI (Pentaho Data Integration) pode ser útil nessa etapa. 

    > De preferência use o Docker por facilitar na configuração dos serviços. 

    > O arquivo original tem 13.872.315 registros, você pode usar uma quantidade limitada para fazer o desenvolvimento. 

    > Será analisada a branch Master, crie uma branch para cada membro do time afim aplicar os conceitos de integração e colaboração, submeta os commits da branch individual para a Master por PR (Pull Request) pela interface do GitHub. Se preferirem podem fazer o fork de um repositório e submeter via PR. 

    > É primordial o uso do Kafka nessa atividade assim como GitHub. O uso de banco de dados NoSQL ou Relacional é opcional assim como o Docker e o Kettle (PDI). 


Qualquer dúvida favor entre em contato, e-mail, hangouts:
hesketh.carlos@gmail.com
