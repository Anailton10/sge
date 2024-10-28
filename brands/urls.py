from django.urls import path

from brands import views

app_name = 'brand'

urlpatterns = [
    path('list/', views.BrandListaView.as_view(), name='list'),
]
