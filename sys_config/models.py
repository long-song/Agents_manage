from django.db import models


# Create your models here.
class AppTb(models.Model):
    id = models.IntegerField(primary_key=True)
    aname = models.CharField(max_length=255)
    anumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app_tb'


class CustomertypeTb(models.Model):
    cstmtype = models.CharField(db_column='cstmType', max_length=100)  # Field name made lowercase.
    state = models.IntegerField()
    isdelete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customertype_tb'
    def __str__(self):
        return self.cstmtype


class DiscountTb(models.Model):
    dscttype = models.CharField(db_column='dsctType', max_length=100)  # Field name made lowercase.
    dsctyear = models.IntegerField(db_column='dsctYear')  # Field name made lowercase.
    realyear = models.IntegerField(db_column='realYear')  # Field name made lowercase.
    state = models.IntegerField()
    isdelete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'discount_tb'


class FinaceTb(models.Model):
    finacetype = models.CharField(db_column='finaceType', max_length=50)  # Field name made lowercase.
    state = models.IntegerField()
    isdelete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'finace_tb'
    def __str__(self):
        return self.finacetype


class LicenseTb(models.Model):
    licstype = models.CharField(db_column='licsType', max_length=100)  # Field name made lowercase.
    state = models.IntegerField()
    isdelete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'license_tb'


class SerYearTb(models.Model):
    id = models.IntegerField(primary_key=True)
    ser_name = models.CharField(max_length=255, blank=True, null=True)
    ser_year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ser_year_tb'


class ServinceTb(models.Model):
    svctype = models.CharField(db_column='svcType', max_length=100)  # Field name made lowercase.
    money = models.CharField(max_length=255)
    state = models.IntegerField()
    caozuo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'servince_tb'
