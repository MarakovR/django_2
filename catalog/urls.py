from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import views_contacts, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', views_contacts, name='contacts'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='item_products'),

]
