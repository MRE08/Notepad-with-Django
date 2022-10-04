from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('create/', views.create, name= 'create'),
    path('create/createnote/', views.createnote, name= 'createnote'),
    path('update/<int:id>', views.update, name = 'update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name = 'updaterecord'),
    path('update/deleterecord/<int:id>', views.deleterecord, name = 'deleterecord'),
]
