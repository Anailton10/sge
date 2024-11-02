from django.urls import path

from products import views

app_name = 'product'

urlpatterns = [
    path('list/', views.ProductListaView.as_view(), name='list'),
    path('create/', views.ProductCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete')
]
