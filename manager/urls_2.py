from django.urls import path
from .views import manager_message,manager_message_update

app_name = 'manager2'

urlpatterns = [
    path('', manager_message, name='message'),
    path('<int:pk>/', manager_message_update, name='message_update')
]