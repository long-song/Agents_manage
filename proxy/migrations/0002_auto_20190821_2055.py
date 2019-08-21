# Generated by Django 2.1.8 on 2019-08-21 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.CharField(max_length=15)),
                ('code_a', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='区县邮编')),
                ('name', models.CharField(max_length=20, verbose_name='区县名称')),
            ],
            options={
                'verbose_name': '城市联动(区县)',
                'verbose_name_plural': '城市联动(区县)',
                'db_table': 'area',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.CharField(max_length=15)),
                ('code_c', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='城市邮编')),
                ('name', models.CharField(max_length=20, verbose_name='城市名称')),
            ],
            options={
                'verbose_name': '城市联动(市级)',
                'verbose_name_plural': '城市联动(市级)',
                'db_table': 'city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.CharField(max_length=15)),
                ('code_p', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='省邮编')),
                ('name', models.CharField(max_length=20, verbose_name='省份名称')),
            ],
            options={
                'verbose_name': '城市联动(省级)',
                'verbose_name_plural': '城市联动(省级)',
                'db_table': 'province',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'managed': False, 'verbose_name': '代理商客户管理', 'verbose_name_plural': '代理商客户管理'},
        ),
        migrations.AlterModelOptions(
            name='lianxiren',
            options={'managed': False, 'verbose_name': '联系人', 'verbose_name_plural': '联系人'},
        ),
        migrations.AlterModelOptions(
            name='prepayment',
            options={'managed': False, 'verbose_name': '代理商预付款', 'verbose_name_plural': '代理商预付款'},
        ),
        migrations.AlterModelOptions(
            name='rizhi',
            options={'managed': False, 'verbose_name': '操作日志', 'verbose_name_plural': '操作日志'},
        ),
    ]