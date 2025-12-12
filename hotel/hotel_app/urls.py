from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.get_list_hotel_room, name='list_rooms'),
    path('rooms/add/', views.add_room, name='add_room'),
    path('rooms/<int:room_id>/delete/', views.delete_room, name='delete_room'),
    path('rooms/<int:room_id>/bookings/', views.get_reservations, name='list_reservations'),
    path('bookings/create/', views.create_reservation, name='create_booking'),
    path('bookings/<int:booking_id>/delete/', views.delete_reservation, name='delete_booking'),
    path('rooms/<int:room_id>/', views.get_room_detail, name='get_room'),
]