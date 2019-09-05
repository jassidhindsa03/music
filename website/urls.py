from django.urls import path
from . import views


app_name = 'website'


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('album_store', views.album_store, name='album_store'),
    path('add_album', views.add_album, name='add_album'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('change_password', views.change_password, name='change_password'),
    path('contact', views.contact, name='contact'),

]
