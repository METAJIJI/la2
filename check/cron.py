from django_cron import CronJobBase, Schedule
from la2.settings import server_list
from models import State
import socket

class Check(CronJobBase):

    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'check.Check_cron'

    def do(self):
        for i in server_list:
            check_servers(id=int(i[0]), host=i[1], port=i[2],
                      timeout=i[3], server=i[4])


def check_servers(id, host, port, timeout, server):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(float(timeout))

        if sock.connect_ex((host, int(port))) == 0:
            b = State(id=id, active=True, server=server)
            b.save()
        else:
            b = State(id=id, active=False, server=server)
            b.save()