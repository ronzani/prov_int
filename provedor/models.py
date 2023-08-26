from django.db import models

from base.models import BaseModel


class Provedor(BaseModel):
    nome = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    token = models.CharField(max_length=45)
    aplicacao = models.CharField(max_length=30)
    telefone = models.CharField(max_length=14)
    email = models.EmailField(max_length=100)
    pagamento_cartao = models.BooleanField(default=False)
    cidade = models.ForeignKey("base.Cidade", on_delete=models.PROTECT, null=True, blank=True)
    bairro = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.CharField(max_length=400, null=True, blank=True)
    numero = models.CharField(max_length=15, null=True, blank=True)
    logo = models.ImageField(upload_to="provedor")
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Provedor"
        verbose_name_plural = "Provedores"
        ordering = ["nome"]


class Lead(BaseModel):
    nome = models.CharField(max_length=200)
    cpf_cnpj = models.CharField(max_length=18, null=True, blank=True)
    telefone = models.CharField(max_length=14)
    email = models.EmailField(max_length=100, null=True, blank=True)
    cidade = models.ForeignKey("base.Cidade", on_delete=models.PROTECT)
    endereco = models.CharField(max_length=400, null=True, blank=True)
    provedor = models.ForeignKey(Provedor, on_delete=models.PROTECT)
    cpf_cnpj_indicador = models.CharField(max_length=18, null=True, blank=True)
    nome_indicador = models.CharField(max_length=200, null=True, blank=True)
    fechou_contrato = models.BooleanField(default=False)
    bonus_pago = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Leads"
        ordering = ["nome"]
