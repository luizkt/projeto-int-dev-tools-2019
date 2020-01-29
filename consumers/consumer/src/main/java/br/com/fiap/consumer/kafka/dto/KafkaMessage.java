package br.com.fiap.consumer.kafka.dto;


public class KafkaMessage {

    private String attribute;

    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
}
