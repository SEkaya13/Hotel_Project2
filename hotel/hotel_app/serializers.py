from rest_framework import serializers
from .models import HotelRooms, Reservations

class HotelRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRooms
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = '__all__'