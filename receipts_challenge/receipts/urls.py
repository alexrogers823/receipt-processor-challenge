from django.urls import path
from receipts import views

urlpatterns = [
    path('receipts/process/', views.receipts),
    path('receipts/<str:pk>/points/', views.receipt_points)
]