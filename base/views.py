from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Room, Topic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RoomForm
from django.db.models import Q


def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Usuário não encontrado')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Senha incorreta')
            
    contexto = {}
    return render(request, 'base/login_register.html', contexto)


def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | 
        Q(name__icontains=q) |
        Q(description__icontains=q))
    
    topics = Topic.objects.all()
    room_count = rooms.count()
    contexto = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
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