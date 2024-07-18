from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
from .models import Photo
from django.conf import settings
from django.db.models import Q

@csrf_exempt
def photo_list(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        date = request.GET.get('date')
        
        # Start with all photos
        photos = Photo.objects.all()
        
        # Filter by name if provided
        if name:
            # Use Q objects to search in both people_in_photo and added_by fields
            photos = photos.filter(Q(people_in_photo__icontains=name) | Q(added_by__icontains=name))
        
        # Filter by date if provided
        if date:
            parsed_date = parse_date(date)
            if parsed_date is not None:
                photos = photos.filter(date_added__date=parsed_date)
            else:
                return HttpResponseBadRequest('Invalid date format.')
        
        # Convert queryset to list of dictionaries
        photo_list = [{
            'id': photo.id,
            'image': f"{settings.MEDIA_URL}{photo.image.name}",
            'date_added': photo.date_added,
            'added_by': photo.added_by,
            'people_in_photo': photo.people_in_photo
        } for photo in photos]
        
        return JsonResponse(photo_list, safe=False)
    else:
        return HttpResponseBadRequest('Invalid request method.')


@csrf_exempt
def photo_create(request):
    if request.method == 'POST':
        try:
            image = request.FILES['image']
            added_by = request.POST['added_by']
            people_in_photo = request.POST['people_in_photo']

            photo = Photo(image=image, added_by=added_by, people_in_photo=people_in_photo)
            photo.save()

            return JsonResponse({
                'id': photo.id,
                'image': photo.image.url,
                'date_added': photo.date_added,
                'added_by': photo.added_by,
                'people_in_photo': photo.people_in_photo
            }, status=201)

        except KeyError:
            return HttpResponseBadRequest('Invalid request. Missing parameters.')

    else:
        return HttpResponseBadRequest('Invalid request method.')


@csrf_exempt
def photo_create(request):
    if request.method == 'POST':
        try:
            image = request.FILES['image']
            added_by = request.POST['added_by']
            people_in_photo = request.POST['people_in_photo']

            photo = Photo(image=image, added_by=added_by, people_in_photo=people_in_photo)
            photo.save()

            return JsonResponse({
                'id': photo.id,
                'image': photo.image.url,
                'date_added': photo.date_added,
                'added_by': photo.added_by,
                'people_in_photo': photo.people_in_photo
            }, status=201)

        except KeyError:
            return HttpResponseBadRequest('Invalid request. Missing parameters.')

    else:
        return HttpResponseBadRequest('Invalid request method.')