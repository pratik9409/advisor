from django.urls import path
from . import views


app_name = "admins"

urlpatterns = [
    path('advisor',views.add_advisor, name='add_advisor'),
    path('truncate',views.truncate_tables,name='truncate')
]

