from rest_framework import generics, filters
from .models import Reservations, HotelRooms
from .serializers import HotelRoomSerializer, ReservationSerializer

class HotelRoomsList(generics.ListCreateAPIView):
    queryset = HotelRooms.objects.all()
    serializer_class = HotelRoomSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price', 'created_at']
    ordering = ['price']


class HotelRoomsUpdate(generics.RetrieveUpdateAPIView):
    queryset = HotelRooms.objects.all()
    serializer_class = HotelRoomSerializer

class HotelRoomsDestroy(generics.RetrieveDestroyAPIView):
    queryset = HotelRooms.objects.all()
    serializer_class = HotelRoomSerializer


class ReservationsList(generics.ListCreateAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationSerializer


class ReservationsUpdate(generics.RetrieveUpdateAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationSerializer


class ReservationsDestroy(generics.RetrieveDestroyAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationSerializer

