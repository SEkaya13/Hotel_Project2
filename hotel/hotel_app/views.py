from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from hotel_app.models import HotelRooms, Reservations
from datetime import datetime


def index(request):
    return JsonResponse({'message': 'Hotel API is running'})

def room_detail(request, room_id):
    try:
        room = HotelRooms.objects.get(pk=room_id)
        room_data = {
            'id': room.id,
            'description': room.description,
            'price': room.price,
            'date_created': room.date_created.strftime('%Y-%m-%d') if hasattr(room, 'date_created') else None
        }
        return JsonResponse(room_data)
    except HotelRooms.DoesNotExist:
        return JsonResponse({'error': 'Room not found'}, status=404)



def get_list_hotel_room(request):
    sort_by = request.GET.get('sort_by', None)
    order = request.GET.get('order', 'asc')

    if sort_by and sort_by not in ['price', 'date']:
        return JsonResponse({'error': 'sort_by must be "price" or "date"'}, status=400)

    if order not in ['asc', 'desc']:
        return JsonResponse({'error': 'order must be "asc" or "desc"'}, status=400)

    if sort_by == 'price':
        order_field = '-price' if order == 'desc' else 'price'
        rooms = HotelRooms.objects.all().order_by(order_field)
    elif sort_by == 'date':
        order_field = '-date_create' if order == 'desc' else 'date_create'
        rooms = HotelRooms.objects.all().order_by(order_field)
    else:
        rooms = HotelRooms.objects.all()

    rooms_list = [
        {
            'id': room.id,
            'description': room.description,
            'price': room.price,
            'date_created': room.date_create.strftime('%Y-%m-%d')
        }
        for room in rooms
    ]

    return JsonResponse(rooms_list, safe=False)

@csrf_exempt
def new_room(request):

    if request.method == 'POST':
        description = request.POST.get('description', '').strip()
        price = request.POST.get('price', '').strip()


        if not description:
            return JsonResponse({'error': 'description is required'}, status=400)

        if not price:
            return JsonResponse({'error': 'price is required'}, status=400)

        try:
            price = int(price)
            if price < 0:
                return JsonResponse({'error': 'price must be positive'}, status=400)
        except ValueError:
            return JsonResponse({'error': 'price must be an integer'}, status=400)

        # Создание номера
        room = HotelRooms.objects.create(description=description, price=price)
        return JsonResponse({'room_id': room.id}, status=201)

    return JsonResponse({'error': 'POST method required'}, status=405)

@csrf_exempt
def del_room(request, room_id):

    if request.method not in ['DELETE', 'POST']:
        return JsonResponse({'error': 'DELETE or POST method required'}, status=405)

    try:
        room = HotelRooms.objects.get(pk=room_id)
        room.delete()
        return JsonResponse({'message': 'Room deleted'})
    except HotelRooms.DoesNotExist:
        return JsonResponse({'error': 'Room not found'}, status=404)



def reservations(request, room_id):
    try:
        room = HotelRooms.objects.get(pk=room_id)

        reservations = Reservations.objects.filter(room_id=room_id).order_by('check_in_date')

        reservations_list = [
            {
                'booking_id': res.id,
                'date_start': res.check_in_date.strftime('%Y-%m-%d'),
                'date_end': res.check_out_date.strftime('%Y-%m-%d')
            }
            for res in reservations
        ]

        return JsonResponse(reservations_list, safe=False)

    except HotelRooms.DoesNotExist:
        return JsonResponse({'error': 'Room not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def new_reservation(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id', '').strip()
        date_start = request.POST.get('date_start', '').strip()
        date_end = request.POST.get('date_end', '').strip()


        if not room_id:
            return JsonResponse({'error': 'room_id is required'}, status=400)
        if not date_start:
            return JsonResponse({'error': 'date_start is required'}, status=400)
        if not date_end:
            return JsonResponse({'error': 'date_end is required'}, status=400)


        try:
            start = datetime.strptime(date_start, '%Y-%m-%d').date()
            end = datetime.strptime(date_end, '%Y-%m-%d').date()
        except ValueError:
            return JsonResponse({'error': 'Invalid date format, use YYYY-MM-DD'}, status=400)

        if start >= end:
            return JsonResponse({'error': 'date_start must be before date_end'}, status=400)

        try:
            room_id = int(room_id)
            room = HotelRooms.objects.get(pk=room_id)
        except ValueError:
            return JsonResponse({'error': 'room_id must be an integer'}, status=400)
        except HotelRooms.DoesNotExist:
            return JsonResponse({'error': 'Room not found'}, status=404)

        reservation = Reservations.objects.create(
            room=room,
            check_in_date=start,
            check_out_date=end
        )

        return JsonResponse({'booking_id': reservation.id}, status=201)

    return JsonResponse({'error': 'POST method required'}, status=405)

@csrf_exempt
def del_reservation(request, booking_id):
    if request.method not in ['DELETE', 'POST']:
        return JsonResponse({'error': 'DELETE or POST method required'}, status=405)

    try:
        reservation = Reservations.objects.get(pk=booking_id)
        reservation.delete()
        return JsonResponse({'message': 'Booking deleted'})
    except Reservations.DoesNotExist:
        return JsonResponse({'error': 'Booking not found'}, status=404)


def page_not_found(request, exception):
    return JsonResponse({'error': 'Endpoint not found'}, status=404)