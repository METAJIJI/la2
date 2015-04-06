from django.shortcuts import render, HttpResponse
from models import State
import socket
import json

def show(request):
    check_servers()

    result_lst = list()
    for state in State.objects.all():
        result_lst.append([state.server, state.active])

    return HttpResponse(json.dumps(result_lst), content_type='application/javascript')

def check_servers(host='ls.la2.metajiji.tk', port=2106, timeout=1):
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