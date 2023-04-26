from django.urls import path
from .views import manager_booked_view, update_booked_view, manager_message,manager_message_update

app_name = 'manager'

urlpatterns = [
    path('', manager_booked_view, name='booked'),
    path('<int:pk>/', update_booked_view, name='update_booked'),
]

