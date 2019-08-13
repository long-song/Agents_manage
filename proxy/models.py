from django.db import models
from sys_config.models import LicenseTb,CustomertypeTb,FinaceTb
from org.models import User

# Create your models here.

class App(models.Model):
    app_id = models.AutoField(primary_key=True)
    app_name = models.CharField(max_length=255, blank=True, null=True)
    app_password = models.CharField(max_length=255, blank=True, null=True)
    keyword = models.ForeignKey('Keyword', models.DO_NOTHING, blank=True, null=True)
    app_a = models.CharField(max_length=255, blank=True, null=True)
    app_b = models.CharField(db_column='app-b', max_length=255, blank=True,
                             null=True)  # Field renamed to remove unsuitable characters.
    app_c = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app'


class Company(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=200, blank=True, null=True)
    tid = models.ForeignKey(CustomertypeTb, models.DO_NOTHING, db_column='tid', blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    lowyer = models.CharField(max_length=200, blank=True, null=True)
    licenseid = models.ForeignKey(LicenseTb, models.DO_NOTHING, db_column='licenseid', blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    fax = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    regtime = models.DateField(blank=True, null=True)
    licensecard = models.CharField(max_length=200, blank=True, null=True)
    sheng = models.CharField(max_length=200, blank=True, null=True)
    shi = models.CharField(max_length=200, blank=True, null=True)
    qu = models.CharField(max_length=200, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    isdelete = models.IntegerField(blank=True, null=True)
    cweb = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    user_name = models.CharField(max_length=20, blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'

class Keyword(models.Model):
    keyword_id = models.AutoField(primary_key=True)
    keyword_name = models.CharField(max_length=255)
    cid = models.ForeignKey('Company', models.DO_NOTHING, db_column='cid', blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    keyword_class = models.CharField(max_length=255, blank=True, null=True)
    keywprd_years = models.IntegerField(blank=True, null=True)
    keyword_price = models.FloatField(blank=True, null=True)
    keyword_newdate = models.CharField(max_length=255, blank=True, null=True)
    keyword_date = models.CharField(max_length=255, blank=True, null=True)
    keyword_apply_state = models.IntegerField(db_column='Keyword_apply_state', blank=True,
                                              null=True)  # Field name made lowercase.
    keyword_check_state = models.IntegerField(blank=True, null=True)
    keyword_use_state = models.IntegerField(blank=True, null=True)
    keyword_app_state = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    isdelete = models.IntegerField(blank=True, null=True)
    keyword_c = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keyword'

class CompanyQu(models.Model):
    qid = models.AutoField(primary_key=True)
    qu = models.CharField(max_length=20, blank=True, null=True)
    hid = models.ForeignKey('CompanyShi', models.DO_NOTHING, db_column='hid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_qu'


class CompanySheng(models.Model):
    sid = models.AutoField(primary_key=True)
    sheng = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_sheng'


class CompanyShi(models.Model):
    hid = models.AutoField(primary_key=True)
    shi = models.CharField(max_length=20, blank=True, null=True)
    sid = models.ForeignKey('CompanySheng', models.DO_NOTHING, db_column='sid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_shi'


class Lianxiren(models.Model):
    lxid = models.AutoField(primary_key=True)
    lxname = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    fax = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    department = models.CharField(max_length=200, blank=True, null=True)
    cid = models.ForeignKey('Company', models.DO_NOTHING, db_column='cid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lianxiren'


class Prepayment(models.Model):
    preid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=200, blank=True, null=True)
    finacetype = models.CharField(db_column='finaceType', max_length=200, blank=True,
                                  null=True)  # Field name made lowercase.
    finacemoney = models.FloatField(blank=True, null=True)
    idbalance = models.FloatField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    finaceid = models.ForeignKey(FinaceTb, models.DO_NOTHING, db_column='finaceid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prepayment'


class Rizhi(models.Model):
    rzid = models.AutoField(primary_key=True)
    rzname = models.CharField(max_length=200, blank=True, null=True)
    rztext = models.TextField(blank=True, null=True)
    rztime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rizhi'
