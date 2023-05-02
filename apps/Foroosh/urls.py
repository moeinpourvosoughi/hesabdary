from django.urls import path, include
from . import views
 

urlpatterns =[
    path('',views.site_Foroosh_part.as_view),
    # path('product_sell_list',views.)
    
]