from django.urls import path
from . import views

app_name = 'BillionaireInsights'

urlpatterns = [
    path('billionaires-combined/', views.billionaires_combined),
]
