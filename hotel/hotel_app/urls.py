from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.get_list_hotel_room, name='list_rooms'),
    path('rooms/add/', views.new_room, name='new_room'),
    path('rooms/<int:room_id>/delete/', views.del_room, name='del_room'),
    path('rooms/<int:room_id>/bookings/', views.reservations, name='list_reservations'),
    path('bookings/create/', views.new_reservation, name='new_booking'),
    path('bookings/<int:booking_id>/delete/', views.del_reservation, name='del_booking'),
    path('rooms/<int:room_id>/', views.room_detail, name='get_room'),
]