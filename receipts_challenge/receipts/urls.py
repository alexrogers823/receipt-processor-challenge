from django.urls import path
from receipts import views

urlpatterns = [
    path('receipts/process/', views.ReceiptProcess.as_view()),
    path('receipts/<str:pk>/points/', views.ReceiptPoints.as_view())
]