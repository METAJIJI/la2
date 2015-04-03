from django.shortcuts import render
from models import State
import socket


def check(request):
    check_login_server()
    check_game_server()

    status = State.objects.values('server','active')
    return render(request, 'status.html', {'status': status})


def check_login_server(host='ls.la2.metajiji.tk', port=2106, timeout=1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(float(timeout))

        if sock.connect_ex((host, int(port))) == 0:
            b = State(id=1, active=True, server='login')
            b.save()
        else:
            b = State(id=1, active=False, server='login')
            b.save()


def check_game_server(host='gs.la2.metajiji.tk', port=7777, timeout=1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(float(timeout))

        if sock.connect_ex((host, int(port))) == 0:
            b = State(id=2, active=True, server='game')
            b.save()
        else:
            b = State(id=2, active=False, server='game')
            b.save()