from django.db import models

class HotelRooms(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    price = models.IntegerField()
    date_create = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Room #{self.id} - {self.price}$ per night"

    class Meta:
        db_table = 'hotel_rooms'
        ordering = ['-date_create']


class Reservations(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(HotelRooms, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking #{self.id} - Room {self.room.id} ({self.check_in_date} to {self.check_out_date})"

    class Meta:
        db_table = 'reservations'
        ordering = ['check_in_date']
        indexes = [
            models.Index(fields=['room', 'check_in_date']),
        ]