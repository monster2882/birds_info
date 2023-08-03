from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Bird


def add_bird(request):
    if request.method == 'POST':
        name = request.POST['name']
        color = request.POST['color']
        sightings = request.POST['sightings']

        photo = request.FILES.get('photo')

        if sightings == 'yes':
            sightings_count = 1
        else:
            sightings_count = 0
        bird = Bird(name=name, color=color, photo=photo, sightings=sightings_count)
        bird.save()

    return render(request, 'bird/add_bird.html')


def bird_list(request):
    birds = Bird.objects.all()
    if len(birds) == 0:
        return HttpResponse('Записей нет')
    return render(request, 'bird/birds_list.html', {'birds': birds})


def one_bird(request, id):
    bird = get_object_or_404(Bird, id=id)
    return render(request, 'bird/one_bird.html', {'bird': bird})


def increment_sightings(request, id):
    bird = get_object_or_404(Bird, id=id)
    bird.sightings += 1
    bird.save()
    return JsonResponse({'new_sightings': bird.sightings})


def main(request):
    return render(request, 'bird/main.html')