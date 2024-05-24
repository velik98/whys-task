from django.urls import path
from . import views

urlpatterns = [
    path('import/', views.ImportView.as_view(), name='import'),
    path('detail/<str:model_name>/', views.DetailListView.as_view(), name='detail-list'),
    path('detail/<str:model_name>/<int:pk>/', views.DetailDetailView.as_view(), name='detail-detail'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('import/', views.ImportView.as_view(), name='import'),
    path('detail/<str:model_name>/', views.DetailListView.as_view(), name='detail-list'),
    path('detail/<str:model_name>/<int:pk>/', views.DetailDetailView.as_view(), name='detail-detail'),
]
