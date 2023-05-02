from django.contrib import admin
from .models import *
from.import views


admin.site.register(ProductsModel)
admin.site.register(GozareshModel)
admin.site.admin_view(views.Items_total_sell_price)