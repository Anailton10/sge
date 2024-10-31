from django.urls import path

from suppliers import views

app_name = 'supplier'

urlpatterns = [
    path('list/', views.SupplierListaView.as_view(), name='list'),
    path('create/', views.SupplierCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.SupplierDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.SupplierUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.SupplierDeleteView.as_view(), name='delete')
]
