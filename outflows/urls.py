from django.urls import path

from outflows import views

app_name = 'outflow'

urlpatterns = [
    path('list/', views.OutflowListaView.as_view(), name='list'),
    path('create/', views.OutflowCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.OutflowDetailView.as_view(), name='detail'),
]
