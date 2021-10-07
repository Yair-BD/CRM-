from django.urls import path
from .views import *


urlpatterns = [
    path('', LeadList.as_view(), name='lead_list'),
    path('create/', LeadCreate.as_view(), name='lead_create'),
    path('update/<str:pk>/', LeadUpdate.as_view(), name='update_lead'),
    path('delete/<str:pk>/', LeadDelete.as_view(), name='delete_lead'),
    path('<str:pk>/', LeadDetail.as_view(), name='detail'),

]
