from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Currency(BaseModel):
    pass


class CurrencyPair(BaseModel):
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
