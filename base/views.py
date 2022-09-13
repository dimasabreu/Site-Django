from django.shortcuts import render

rooms = [
    {'id':1, 'name': 'Python'},
    {'id':2, 'name': 'Java'},
    {'id':3, 'name': 'PHP'},
    
]


def home(request):
    contexto = {'rooms': rooms}
    return render(request,'base/home.html', contexto)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
        contexto = {'room': room}
    return render(request, 'base/room.html', contexto)
