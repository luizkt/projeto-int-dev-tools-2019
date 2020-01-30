package br.com.fiap.consumer;

import br.com.fiap.consumer.kafka.dto.KafkaMessage;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@SpringBootApplication
@RestController
public class ConsumerApplication {

	KafkaMessage msg;

	@GetMapping("/")
	public KafkaMessage consumeMsgs(){
		return msg;
	}

	@KafkaListener(groupId = "my-app", topics = "entrada", containerFactory = "kafkaListenerContainerFactory")
	public KafkaMessage getMsgFromTopic(@Payload KafkaMessage data){
		msg = data;
		return msg;
	}


	public static void main(String[] args) {
		SpringApplication.run(ConsumerApplication.class, args);
	}

}
