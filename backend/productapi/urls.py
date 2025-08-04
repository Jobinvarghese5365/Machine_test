# products/urls.py (or project-level urls.py)
from django.urls import path
from products import views

urlpatterns = [
    path("search/", views.search_products),
    path("product/<str:pk>/", views.product_detail),
    path("products/", views.list_products),  # 👈 new endpoint
]
