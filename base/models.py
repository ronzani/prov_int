from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(null=False, blank=True, default=timezone.now)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if kwargs.get("update_fields"):
            kwargs["update_fields"] = list(set(list(kwargs["update_fields"]) + ["updated_at"]))
        return super().save(*args, **kwargs)


class Estado(BaseModel):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ["nome"]


class Cidade(BaseModel):
    nome = models.CharField(max_length=200)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        ordering = ["nome"]
