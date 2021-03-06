from django.contrib.postgres.fields import ArrayField, JSONField, IntegerRangeField
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, editable=False)
    modified_date = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=50, editable=False)

    class Meta:
        abstract = True


class Currency(BaseModel):
    name = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=50)
    display_format = models.CharField(max_length=50)
    flag = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "currencies"


class CurrencyPair(BaseModel):
    name = models.CharField(max_length=10, unique=True)
    display_format = models.CharField(max_length=50)
    base_ccy = models.CharField(max_length=10)
    alt_ccy = models.CharField(max_length=10)
    pass


class Exchange(BaseModel):
    pass


class Calendar(BaseModel):
    pass


class InterestRate(BaseModel):
    pass


class BusinessEntity(BaseModel):
    pass


class Instrument(BaseModel):
    pass


class Security(BaseModel):
    pass


class HelloWorldEntity(BaseModel):
    name = models.CharField(max_length=10, unique=True)
    array_field = ArrayField(models.CharField(max_length=10), size=8, null=True)
    json_field = JSONField(null=True)
    integer_range_field = IntegerRangeField(null=True)

    def __str__(self):
        return self.name
