package br.com.fiap.consumer.kafka.dto;

public class Result {

    private String uf;
    private double totalParcela;
    private Integer qtdeBeneficiarios;

    public Result() {
    }

    public Result(String uf, double totalParcela, Integer qtdeBeneficiarios) {
        this.uf = uf;
        this.totalParcela = totalParcela;
        this.qtdeBeneficiarios = qtdeBeneficiarios;
    }

    public String getUf() {
        return uf;
    }

    public void setUf(String uf) {
        this.uf = uf;
    }

    public double getTotalParcela() {
        return totalParcela;
    }

    public void setTotalParcela(double totalParcela) {
        this.totalParcela = totalParcela;
    }

    public Integer getQtdeBeneficiarios() {
        return qtdeBeneficiarios;
    }

    public void setQtdeBeneficiarios(Integer qtdeBeneficiarios) {
        this.qtdeBeneficiarios = qtdeBeneficiarios;
    }

    public void somaParcelas (Double valorParcela)
    {
        this.totalParcela += valorParcela;
    }

    public void somaBeneficiarios(Integer n)
    {
        this.qtdeBeneficiarios += n;
    }


}
