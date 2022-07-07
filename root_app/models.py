from django.db import models
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _


class DummyModel(models.Model):
    model_name = models.CharField(_("Modal Name"), max_length=50)
    model_type = models.CharField(_("Modal Type"), max_length=50)

    def __str__(self) -> str:
        return self.model_name