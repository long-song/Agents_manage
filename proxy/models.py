from django.db import models
from sys_config.models import LicenseTb, CustomertypeTb, FinaceTb
from org.models import User
from website.models import StateTb


# Create your models here.

class App(models.Model):
    app_id = models.AutoField(primary_key=True)
    app_name = models.CharField(max_length=255, blank=True, null=True)
    app_password = models.CharField(max_length=255, blank=True, null=True)
    keyword = models.ForeignKey('Keyword', on_delete=models.CASCADE , blank=True, null=True)
    app_a = models.CharField(max_length=255, blank=True, null=True)
    app_b = models.CharField(db_column='app-b', max_length=255, blank=True,
                             null=True)  # Field renamed to remove unsuitable characters.
    app_c = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app'


class Company(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=200, blank=True, null=True, verbose_name='企业名称')
    tid = models.ForeignKey(CustomertypeTb, on_delete=models.CASCADE, db_column='tid', blank=True, null=True,
                            verbose_name='企业类型')
    # state = models.ForeignKey(StateTb, models.DO_NOTHING, db_column='state', blank=True, default=0,verbose_name='是否启用')
    state = models.IntegerField(blank=True, null=True, default=0, verbose_name='是否启用')
    lowyer = models.CharField(max_length=200, blank=True, null=True, verbose_name='法人代表')
    licenseid = models.ForeignKey(LicenseTb, on_delete=models.CASCADE, db_column='licenseid', blank=True, null=True,
                                  verbose_name='证件类型')
    country = models.CharField(max_length=200, blank=True, null=True, verbose_name='国家')
    fax = models.CharField(max_length=200, blank=True, null=True, verbose_name='公司传真')
    phone = models.CharField(max_length=200, blank=True, null=True, verbose_name='公司电话')
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name='公司地址')
    regtime = models.DateField(blank=True, null=True, verbose_name='注册日期')
    licensecard = models.CharField(max_length=200, blank=True, null=True, verbose_name='证件号码')
    sheng = models.CharField(max_length=200, blank=True, null=True, verbose_name='省')
    shi = models.CharField(max_length=200, blank=True, null=True, verbose_name='市')
    qu = models.CharField(max_length=200, blank=True, null=True, verbose_name='区')
    remark = models.TextField(blank=True, null=True, verbose_name='备注')
    isdelete = models.IntegerField(blank=True, null=True, verbose_name='是否删除')
    cweb = models.CharField(max_length=200, blank=True, null=True, verbose_name='注册网站')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='注册用户')
    user_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='客户名称')
    balance = models.IntegerField(blank=True, null=True, verbose_name='余额')

    class Meta:
        managed = False
        db_table = 'company'
        verbose_name = '代理商客户管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cname


class Keyword(models.Model):
    keyword_id = models.AutoField(primary_key=True)
    keyword_name = models.CharField(max_length=255)
    cid = models.ForeignKey('Company', on_delete=models.CASCADE, db_column='cid', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
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


class Province(models.Model):
    id = models.CharField(max_length=15)
    code_p = models.CharField(primary_key=True, max_length=15, verbose_name='省邮编')
    name = models.CharField(max_length=20, verbose_name='省份名称')

    class Meta:
        managed = False
        db_table = 'province'
        verbose_name = '城市联动(省级)'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.CharField(max_length=15)
    code_c = models.CharField(primary_key=True, max_length=15, verbose_name='城市邮编')
    name = models.CharField(max_length=20, verbose_name='城市名称')
    code_p = models.ForeignKey('Province',on_delete=models.CASCADE, db_column='code_p', blank=True, null=True,
                               verbose_name='所属省份')

    class Meta:
        managed = False
        db_table = 'city'
        verbose_name = '城市联动(市级)'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Area(models.Model):
    id = models.CharField(max_length=15)
    code_a = models.CharField(primary_key=True, max_length=15, verbose_name='区县邮编')
    name = models.CharField(max_length=20, verbose_name='区县名称')
    code_c = models.ForeignKey('City', on_delete=models.CASCADE, db_column='code_c', blank=True, null=True,
                               verbose_name='所属城市')

    class Meta:
        managed = False
        db_table = 'area'
        verbose_name = '城市联动(区县)'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lianxiren(models.Model):
    lxid = models.AutoField(primary_key=True)
    lxname = models.CharField(max_length=200, blank=True, null=True, verbose_name='姓名')
    phone = models.CharField(max_length=200, blank=True, null=True, verbose_name='电话')
    fax = models.CharField(max_length=200, blank=True, null=True, verbose_name='传真')
    email = models.CharField(max_length=200, blank=True, null=True, verbose_name='邮箱')
    department = models.CharField(max_length=200, blank=True, null=True, verbose_name='职位')
    cid = models.ForeignKey('Company', on_delete=models.CASCADE, db_column='cid', blank=True, null=True, verbose_name='代理商')

    class Meta:
        managed = False
        db_table = 'lianxiren'
        verbose_name = '联系人'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.lxname


class Prepayment(models.Model):
    preid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=200, blank=True, null=True, verbose_name='企业名称')
    finacetype = models.CharField(db_column='finaceType', max_length=200, blank=True,
                                  null=True, verbose_name='财务类型')  # Field name made lowercase.
    finacemoney = models.FloatField(blank=True, null=True, verbose_name='财务资金')
    idbalance = models.FloatField(blank=True, null=True, verbose_name='账户余额')
    remark = models.TextField(blank=True, null=True, verbose_name='备注信息')
    user_id = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    finaceid = models.ForeignKey(FinaceTb, on_delete=models.CASCADE, db_column='finaceid', blank=True, null=True,
                                 verbose_name='财务类型')

    class Meta:
        managed = False
        db_table = 'prepayment'
        verbose_name = '代理商预付款'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.remark


class Rizhi(models.Model):
    rzid = models.AutoField(primary_key=True)
    rzname = models.CharField(max_length=200, blank=True, null=True, verbose_name='操作人')
    rztext = models.TextField(blank=True, null=True, verbose_name='操作信息')
    rztime = models.DateTimeField(blank=True, null=True, verbose_name='操作时间')

    class Meta:
        managed = False
        db_table = 'rizhi'
        verbose_name = '操作日志'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.rztext
