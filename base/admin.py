from django.contrib import admin

from .models import Cidade, Estado


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla")
    search_fields = ("nome", "sigla")
    exclude = ["created_at", "updated_at"]


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "estado")
    search_fields = ("nome", "estado")
    exclude = ["created_at", "updated_at"]
    # raw_id_fields = ("estado",)
