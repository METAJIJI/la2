from django.shortcuts import render
from models import *
from django.http import HttpResponseRedirect
from la2.settings import server_names



def players(request, server=server_names[0], number=5):
    q = '''SELECT characters.obj_Id, characters.char_name, character_subclasses.level, characters.sex,
          characters.pvpkills, characters.pkkills, characters.online, characters.onlinetime,
          char_templates.ClassName, clan_data.clan_name,  clan_data.clan_id
		FROM `characters`
		LEFT JOIN `character_subclasses` ON characters.obj_Id = character_subclasses.char_obj_id
		AND character_subclasses.isBase='1'
		LEFT JOIN `char_templates` ON character_subclasses.class_id = char_templates.ClassId
		LEFT JOIN `clan_data` ON characters.clanid = clan_data.clan_id
		WHERE characters.accesslevel='0'
		ORDER BY %s DESC
		LIMIT 10'''

    query = Characters.objects.using(server).raw(q, [int(number)])

    return render(request, "player_statistic.html", {
        'query': query, 'server': server, 'number': number, 'servers': server_names
    })

def castles(request, server=server_names[0]):
    q = '''
        SELECT castle.name, castle.id, castle.taxPercent, castle.siegeDate,
        clan_data.clan_name, clan_data.clan_id
		FROM castle
		LEFT JOIN clan_data ON clan_data.hasCastle = castle.id
        '''
    query = Castle.objects.using(server).raw(q)
    return render(request, "castle_statistic.html", {
        'query': query, 'server': server, 'servers': server_names
    })