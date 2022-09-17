from django.shortcuts import render
from .models import Room



def home(request):
    rooms = Room.objects.all()
    contexto = {'rooms': rooms}
    return render(request,'base/home.html', contexto)


def room(request, pk):
    room = Room.objects.get(id=pk)
    contexto = {'room': room}
    return render(request, 'base/room.html', contexto)


def createRoom(request):
    contexto = {}
    return render(request, 'base/room_form.html', contexto)