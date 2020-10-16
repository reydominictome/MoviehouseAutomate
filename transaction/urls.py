from django.urls import path
from . import views

app_name = 'transaction'

urlpatterns = [
    path('index', views.TransactionIndexView.as_view(), name='transaction_index'),
    path('transact', views.TransactionView.as_view(), name='transact'),
]