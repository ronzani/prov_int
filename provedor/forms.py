from django.forms import ModelForm

from provedor.models import Lead


class LeadForm(ModelForm):
    class Meta:
        model = Lead
        exclude = ["created_at", "updated_at"]
