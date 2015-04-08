from django.shortcuts import render
from models import *
from django.http import HttpResponseRedirect

def pick_server(request):
    return render(request, "pick_server.html")

def statistic(request, server='1', number=3):

    q = '''SELECT characters.obj_Id, characters.char_name, character_subclasses.level, characters.sex, characters.pvpkills, characters.pkkills, characters.online, characters.onlinetime, char_templates.ClassName, clan_data.clan_name, clan_data.clan_id
		FROM `characters`
		LEFT JOIN `character_subclasses` ON characters.obj_Id = character_subclasses.char_obj_id AND character_subclasses.isBase='1'
		LEFT JOIN `char_templates` ON character_subclasses.class_id = char_templates.ClassId
		LEFT JOIN `clan_data` ON characters.clanid = clan_data.clan_id
		WHERE characters.accesslevel='0'
		ORDER BY %s DESC
		LIMIT 20''' % int(number)

    query = Characters.objects.using(server).raw(q)

    return render(request, "statistic.html", {
        'query': query, 'server': server,
    })
