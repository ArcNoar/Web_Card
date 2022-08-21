from django.db import models
from django.contrib.auth.models import User



# ABSOLUTE

class Dossier(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=40, null=True)
    
    
    reg_data = models.DateTimeField(auto_now_add = True, null=True)


    def __str__(self):
        return "%s - %s" % (self.name, self.reg_data)
    
    class Meta:
        verbose_name_plural = 'Абсолют - Данные Пользователей.'
        verbose_name = 'Пользователь'
        ordering = ['reg_data']



# HIGH_PERM


# MID_PERM


# LOW_PERM


# ZERO_PERM
