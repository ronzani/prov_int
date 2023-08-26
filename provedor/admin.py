from django.contrib import admin

from .models import Lead, Provedor


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone", "provedor_nome", "fechou_contrato")
    list_filter = ("fechou_contrato", "provedor__nome")
    search_fields = ("nome", "cpf_cnpj", "email", "telefone")
    exclude = ["created_at", "updated_at"]

    @admin.display(description="Nome do Provedor")
    def provedor_nome(self, obj):
        return obj.provedor.nome


@admin.register(Provedor)
class ProvedorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone", "cidade_nome")
    list_filter = ("ativo", "cidade__nome")
    search_fields = ("nome", "email", "telefone")
    exclude = ["created_at", "updated_at"]
    raw_id_fields = ("cidade",)

    @admin.display(description="Nome da Cidade")
    def cidade_nome(self, obj):
        return obj.cidade.nome
