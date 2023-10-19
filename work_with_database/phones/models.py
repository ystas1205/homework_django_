from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование")
    price = models.IntegerField(verbose_name="Цена")
    image = models.ImageField(upload_to="image/%Y/%m/%d", verbose_name="Фото")
    release_date = models.DateField(verbose_name="Дата выпуска")
    lte_exists = models.BooleanField(default=None, verbose_name="Наличие")
    slug = models.SlugField(max_length=200, unique=True, db_index=True,
                            verbose_name="URL")

    def __str__(self):
        return f"{self.name}"
