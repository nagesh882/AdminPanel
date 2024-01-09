from django.urls import path
from service import views

urlpatterns = [
    path('', views.home, name="homePage"),
    path('savedata/', views.save, name="savedata"),
    path('edit', views.EDIT, name='edit'),
    path('update/<str:id>', views.update, name="update"),
    path('delete/<str:id>', views.Delete, name='delete'),

]
