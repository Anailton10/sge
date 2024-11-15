from django.urls import path

from outflows import views

app_name = 'outflow'

urlpatterns = [
    path('list/', views.OutflowListaView.as_view(), name='list'),
    path('create/', views.OutflowCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.OutflowDetailView.as_view(), name='detail'),

    path('api/v1/outflow/', views.OutflowCreateListAPIView.as_view(),
         name='outflow-create-list-api-view'),
    path('api/v1/outflow/<int:pk>/', views.OutflowRetrieveUpdateDestroyAPIView.as_view(),
         name='outflow-detail-api-view'),
]
