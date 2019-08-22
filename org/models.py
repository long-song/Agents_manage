from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_realname = models.CharField(max_length=20, blank=True, null=True)
    user_logname = models.CharField(max_length=20, blank=True, null=True)
    user_password = models.CharField(max_length=20, blank=True, null=True)
    user_idcard = models.CharField(db_column='user_Idcard', max_length=100, blank=True,
                                   null=True)  # Field name made lowercase.
    user_sex = models.CharField(max_length=10, blank=True, null=True)
    user_address = models.CharField(max_length=100, blank=True, null=True)
    user_email = models.CharField(max_length=100, blank=True, null=True)
    user_starttime = models.DateField(blank=True, null=True)
    user_phone = models.CharField(max_length=50, blank=True, null=True)
    user_state = models.IntegerField(blank=True, null=True)
    user_caiwu = models.IntegerField(blank=True, null=True)
    user_caozuo = models.IntegerField(blank=True, null=True)
    user_isdel = models.IntegerField(blank=True, null=True)
    user_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return self.user_realname

    def user_state1(self):
        """
        判断状态
        :return:
        """
        if self.user_state == 1:
            return '启用'
        else:
            return '禁用'


class UserRole(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey('Role', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_role'
        unique_together = (('user', 'role'),)


class Menu(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    menu_name = models.CharField(max_length=30)
    menu_firstmenu = models.IntegerField()
    menu_intro = models.CharField(max_length=255, blank=True, null=True)
    menu_state = models.IntegerField()
    menu_url = models.CharField(max_length=255, blank=True, null=True)
    menu_flag = models.CharField(max_length=255, blank=True, null=True)
    menu_isdel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'menu'

    def menu_firstmenu1(self):
        """
        判断菜单
        :return:
        """
        if self.menu_firstmenu == -1:
            return '菜单'
        elif self.menu_firstmenu == 0:
            return '上级菜单'
        else:
            return '下级菜单'

    def menu_intro1(self):
        """
        判断简介
        :return:
        """
        if self.menu_intro:
            return self.menu_intro
        else:
            return '无内容'

    def menu_state1(self):
        """
        判断状态 1 启用  0禁用
        :return:
        """
        if self.menu_state == 1:
            return '启用'
        else:
            return '禁用'


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100)
    role_state = models.IntegerField()
    role_remark = models.CharField(max_length=100)
    role_isdel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'role'

    def role_state1(self):
        """
        判断状态  1 启用 0 禁用
        :return:
        """
        if self.role_state == 1:
            return '启用'
        else:
            return '禁用'


class RoleMenu(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, primary_key=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'role_menu'
        unique_together = (('role', 'menu'),)


class Pic(models.Model):
    my_header = models.ImageField()
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'org_pic'
