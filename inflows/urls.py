from django.urls import path

from inflows import views

app_name = 'inflow'

urlpatterns = [
    path('list/', views.InflowListaView.as_view(), name='list'),
    path('create/', views.InflowCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.InflowDetailView.as_view(), name='detail'),
]
