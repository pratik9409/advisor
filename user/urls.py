from django.urls import path, include
from . import views

app_name = 'user'
urlpatterns = [
    path('register', views.register_user, name='register_user'),
    path('login', views.login_user,name='login_user'),
    path('<str:user_id>/advisor', views.get_advisor, name='userid'),
    path('<str:user_id>/advisor/booking', views.fetch_bookings, name='userid_booking'),
    path('<str:user_id>/advisor/<str:advisor_id>', views.book_advisor, name='userid_advisorid'),
    path('<str:user_id>', views.test),
]