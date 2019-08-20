from django.db import models
from sys_config.models import FinaceTb
from org.models import User


# Create your models here.
class ReportFinaceTb(models.Model):
    report = models.ForeignKey('ReportList', models.DO_NOTHING)
    finace = models.ForeignKey(FinaceTb, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'report_finace_tb'
        unique_together = (('report', 'finace'),)


class ReportList(models.Model):
    rep_id = models.AutoField(primary_key=True)
    rep_agentname = models.CharField(max_length=20, blank=True, null=True)
    rep_custerm = models.CharField(max_length=20, blank=True, null=True)
    rep_monty = models.IntegerField(blank=True, null=True)
    rep_nowdate = models.CharField(max_length=30, blank=True, null=True)
    rep_remark = models.CharField(max_length=255, blank=True, null=True)
    rep_finatype = models.ForeignKey(FinaceTb, models.DO_NOTHING, db_column='rep_finatype', blank=True, null=True)
    rep_userid = models.ForeignKey(User, models.DO_NOTHING, db_column='rep_userid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_list'
