from django.urls import path

from . import views

app_name = 'registry'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:gift_id>/', views.detail, name='detail'),
    path('<int:gift_id>/purchase/', views.purchase, name='purchase'),
]