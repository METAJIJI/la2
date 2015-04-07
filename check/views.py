from django.shortcuts import render, HttpResponse
from models import State
import socket
import json
from la2.settings import server_list


def show(request):
    # for i in server_list:
    #     check_servers(id=int(i[0]), host=i[1], port=i[2],
    #                   timeout=i[3], server=i[4])

    result_lst = []
    for state in State.objects.all():
        result_lst.append([state.server, state.active])

    return HttpResponse(json.dumps(result_lst), content_type='application/javascript')


# def check_servers(id, host, port, timeout, server):
#
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.settimeout(float(timeout))
#
#         if sock.connect_ex((host, int(port))) == 0:
#             b = State(id=id, active=True, server=server)
#             b.save()
#         else:
#             b = State(id=id, active=False, server=server)
#             b.save()
