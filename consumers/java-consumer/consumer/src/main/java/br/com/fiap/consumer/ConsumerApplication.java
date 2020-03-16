package br.com.fiap.consumer;

import br.com.fiap.consumer.kafka.dto.KafkaMessage;
import br.com.fiap.consumer.kafka.dto.Result;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

@SpringBootApplication
@RestController
public class ConsumerApplication {

    HashMap<String, Result> result;

    public ConsumerApplication() {
        result = new HashMap<>();
    }

    KafkaMessage msg;

    @GetMapping("/")
    public KafkaMessage consumeMsgs() {
        return msg;
    }

    @KafkaListener(groupId = "my-app", topics = "entrada", containerFactory = "kafkaListenerContainerFactory")
    public KafkaMessage getMsgFromTopic(@Payload KafkaMessage data) {
        msg = data;
        if (!data.getUf().isEmpty()) {
            calculaParcelas(data);
        }

        return msg;
    }


    private void calculaParcelas(KafkaMessage data) {

        Result res = new Result();
        if (!result.containsKey(data.getUf())) {
            result.put(data.getUf(), new Result(data.getUf(), data.getValorParcela(), 1));
        } else {
            res = result.get(data.getUf());
            res.somaParcelas(data.getValorParcela());
            res.somaBeneficiarios(1);
            result.replace(data.getUf(), res);
        }

        result.forEach((k, v) -> {
            System.out.println("UF: " + v.getUf());
            System.out.println("Valor total: " + v.getTotalParcela());
            System.out.println("Quantidade de beneficiarios: " + v.getQtdeBeneficiarios());
        });
    }


	public static void main(String[] args) {
        SpringApplication.run(ConsumerApplication.class, args);
    }

}
