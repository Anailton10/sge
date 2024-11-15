from django.urls import path

from categories import views

app_name = 'category'

urlpatterns = [
    path('list/', views.CategoryListaView.as_view(), name='list'),
    path('create/', views.CategoryCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.CategoryDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.CategoryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete'),

    path('api/v1/categories/', views.SupplierCreateListAPIView.as_view(),
         name='category-create-list-api-view'),
    path('api/v1/categories/<int:pk>/', views.SupplierRetrieveUpdateDestroyAPIView.as_view(),
         name='category-detail-api-view'),
]
