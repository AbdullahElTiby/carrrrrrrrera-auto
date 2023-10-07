from django.contrib import admin
from .models import RequestingOrder,CustomUser,Ordershistory
# Register your models here.

admin.site.register(RequestingOrder)
admin.site.register(CustomUser)
admin.site.register(Ordershistory)



