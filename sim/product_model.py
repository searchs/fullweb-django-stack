from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        "Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    ingredients = models.TextField(max_length=1024)
    insights = models.TextField(max_length=1024)
    protein_moisture = models.TextField(max_length=1024)
    hairtype = models.TextField(max_length=1024)
    porosity = models.TextField(max_length=1024)
    texture = models.TextField(max_length=1024)
    special_instruction = models.TextField(max_length=1024)
    link = models.TextField(max_length=1024, null=True)
    hair_goals = models.TextField(max_length=1024)
    hair_issues = models.TextField(max_length=1024)
    internal_insights = models.TextField(max_length=1024)
    # TODO: fix duplicate category
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(max_length=1024, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
