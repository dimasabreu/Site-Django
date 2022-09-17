from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | 
        Q(name__icontains=q) |
        Q(description__icontains=q))
    
    topics = Topic.objects.all()
    contexto = {'rooms': rooms, 'topics': topics}
    return render(request,'base/home.html', contexto)


def room(request, pk):
    room = Room.objects.get(id=pk)
    contexto = {'room': room}
    return render(request, 'base/room.html', contexto)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form  = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    contexto = {'form': form}
    return render(request, 'base/room_form.html', contexto)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    contexto = {'form': form}
    return render(request, 'base/room_form.html', contexto)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})