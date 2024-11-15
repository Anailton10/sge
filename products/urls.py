from django.urls import path

from products import views

app_name = 'product'

urlpatterns = [
    path('list/', views.ProductListaView.as_view(), name='list'),
    path('create/', views.ProductCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete'),

    path('api/v1/products/', views.ProductCreateListAPIView.as_view(),
         name='product-create-list-api-view'),
    path('api/v1/products/<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(),
         name='product-detail-api-view'),

]
