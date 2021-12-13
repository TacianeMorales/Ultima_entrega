from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        help_text="Nome da Categoria",
        unique=True,
        max_length=80,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.name = self.name.upper()

        super(Category, self).save(*args, **kwargs)

class Infos(models.Model):
    Produtname = models.CharField(
        help_text="Nome do produto",
        unique=True,
        max_length=80,
    )
    ProdutPeso = models.CharField(help_text="Peso do Produto", max_length=50)
    ProdutMarca = models.CharField(help_text="Marca do Produto", max_length=50)
    ProdutUso = models.TextField(
        help_text="Modo de uso do Produto",
        null=True,
        blank=True,
    )
