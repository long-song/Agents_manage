from django.db import models


# Create your models here.
class StateTb(models.Model):
    id = models.IntegerField(primary_key=True)
    st_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state_tb'
    def __str__(self):
        return self.st_name
