from . import views
from django.urls import path

urlpatterns = [
    #This is for the test_ids
    path('<test_id>', views.index, name='index'),
    path('',views.home, name = 'home'),
    path('map',views.visualisation, name='visualisation')

]