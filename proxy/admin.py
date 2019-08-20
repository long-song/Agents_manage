from django.contrib import admin

# Register your models here.
from proxy.models import *
admin.site.register(App)
admin.site.register(Company)
admin.site.register(Lianxiren)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Area)
admin.site.register(Rizhi)
admin.site.register(Prepayment)
admin.site.register(Keyword)

