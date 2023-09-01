import uuid

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, UUIDField
from django.urls import reverse


class User(AbstractUser):
    """
    Default custom user model for Provedor de Integração.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField("Nome do Usuário", blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    uuid = UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="uuid",
    )
    cpf_cnpj = CharField(max_length=18, verbose_name="CPF/CNPJ", null=True, blank=True)
    telefone = CharField(max_length=16, verbose_name="Telefone", null=True, blank=True)

    def get_absolute_url(self) -> str:
        """
        Get URL for user's detail view.

        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"uuid": self.uuid})
