# README do projeto-int-dev-tools-2019 34SCJ
Utilização de consumidores e produtores utilizando o Kafka 

Kanban Flow do projeto em https://trello.com/b/NdOw7yv7/fiap

Integrantes:

    Jhonatan Oliveira da Guarda - RM 333990
    
    Logan Mantovani Baruch      - RM 334335
    
    Luiz Keese Tabacow          - RM 334018
    
    Vitor de Menezes Cardoso    - RM 333756
    
    Milton Luiz Ribeiro Junior  - RM 333949
    
## Big Picture da solução
![big_picture](https://github.com/luizkt/projeto-int-dev-tools-2019/blob/master/big_picture.png)
	
## Para executar o processo (execução local ubuntu ou docker) deve seguir os passos abaixo:
  1) Ter instalado as seguintes aplicações:
  
     a) Node js ```sudo apt install nodejs```;
     
     b) Python ```sudo apt-get install python3.6```;
     
     c) Pip ```sudo apt-get install python-pip```;
     
     d) plugin pip kafka-python ```pip install kafka-python```;
	 
     r) Open JDK 11 ```sudo apt install openjdk-11-jdk```
     
     f) terminator (opcional) ```sudo apt-get install terminator``` ;
  
  2) Executar o Kafka (local ou via docker):
  
     a) Realizar o download do Kafka https://kafka.apache.org/quickstart;
     
     b) Descompactar pasta e acessar o diretório kafka_2.12-2.4.0 (via terminal executar: ```cd kafka_2.12-2.4.0```);
     
     c) Iniciar o Zookeeper (em uma sessão do terminal executar: ```bin/zookeeper-server-start.sh config/zookeeper.properties```);
     
     d) Iniciar o Kafka (em uma sessão do terminal executar: ```bin/kafka-server-start.sh config/server.properties```);
     
     ou
     
     e) Executar o comando `docker-compose up` no local do arquivo docker-compose.yml na raiz do projeto. O arquivo vai executar um conteiner de zookeeper e outro de kafka.

  3) Realizar o clone do projeto via git ```https://github.com/luizkt/projeto-int-dev-tools-2019.git``` e utilizar a branch "master";
		
  4) Abrir o terminal e executar o script ```load-kafka-nodejs-unix.sh``` na raiz da pasta clonada. 
  
     a) O script vai resolver as dependencias do node.
     
     a) A aplicação em Node js irá ler o arquivo csv dos beneficiários do bolsa família (2019_01) localizando na pasta ```files```;
      
     b) O Tópico é criado automaticamente no producer com o nome "entrada", mas caso queira criar o tópico antes, executar no terminal após o passo 2.d) o comando ```bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic entrada``` 
     
     c) Aplicação passa a produzir os registros para o tópico "entrada", teste com 10999 registros.
  
  5) Abrir 3 sessões no terminal e executar os seguintes scripts em Python em cada sessão, navegando a partir da raiz do projeto:
  
     a) ```python ./consumers/pythonConsumer.py```; Quantidade de beneficíarios por Estado e somatória do benefício;
     
     b) ```python ./consumers/pythonConsumer2.py```; Beneficiário com maior benefício recebido;
     
     c) ```python ./consumers/pythonConsumer3.py```; Quantidade de registros consumidos;
     
  6) Acompanhar execução conforme video abaixo (Execução com 10999 linhas processadas do arquivo CSV)
  
  ![ExecucaoLocal](https://github.com/luizkt/projeto-int-dev-tools-2019/blob/master/ExecucaoLocal.gif)

## Enunciado do trabalho

Descrição: 
Crie um produtor para carregar os dados do arquivo do bolsa família (referente ao período de janeiro/2019) para um Topic no Kafka e implemente 3 consumidores que irão nos ajudar a responder algumas perguntas. 

Link para download do arquivo: http://www.portaltransparencia.gov.br/download-de-dados/bolsa-familia-pagamentos 

Layout do arquivo: MÊS_REFERÊNCIA, MÊS_COMPETÊNCIA, UF, CÓDIGO_MUNICÍPIO_SIAFI, NOME_MUNICÍPIO, NIS_FAVORECIDO, NOME_FAVORECIDO, VALOR_PARCELA. 

Produtor: Carregar os dados de um arquivo .csv para um Topic do kafka.  ```Realizado no item 4```

Consumidores:  ```Realizado no item 5```

    1) Exibir [UF] + [soma das parcelas] + [qtd de beneficiários] até o momento; 

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
