from django.shortcuts import render
from models import ClanData, Characters
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
		LIMIT 100'''

    query = Characters.objects.using(server).raw(q, [int(number)])

    return render(request, "player_statistic.html", {
        'query': query, 'server': server, 'number': number, 'servers': server_names
    })

def castles(request, server=server_names[0]):

    castles = '''
        SELECT castle.name, castle.id, castle.taxPercent, castle.siegeDate,
        clan_data.clan_name, clan_data.clan_id
		FROM castle
		LEFT JOIN clan_data ON clan_data.hasCastle = castle.id
        '''

    castles_data = '''SELECT siege_clans.unit_id as castle_id,  siege_clans.type, clan_data.clan_name
		FROM siege_clans
		LEFT JOIN clan_data ON clan_data.clan_id = siege_clans.clan_id
		WHERE unit_id=1
    '''


    # query = Castle.objects.using(server).raw(castles)
    # query2 = SiegeClans.objects.using(server).raw(castles_data)


    return render(request, "castle_statistic.html", {
       # 'query': query, 'query2': query2, 'server': server, 'servers': server_names
    })


def clans(request, server=server_names[0]):
    q = '''SELECT clan_data.clan_name, clan_data.clan_id, ally_data.ally_name,
clan_data.clan_level, clan_data.reputation_score, clan_data.hasCastle, characters.char_name, ccount
		FROM `clan_data`
		LEFT JOIN `characters` ON characters.obj_Id = clan_data.leader_id
		LEFT JOIN (
			SELECT clanid, count(0) AS ccount
			FROM characters
			WHERE clanid GROUP BY clanid
			) AS levels ON clan_data.clan_id = levels.clanid
		LEFT JOIN `ally_data` ON clan_data.ally_id = ally_data.ally_id
		ORDER BY clan_data.clan_level DESC, clan_data.reputation_score DESC
		'''

    query = ClanData.objects.using(server).raw(q)

    return render(request, "clans_statistic.html", {
        'query': query, 'server': server, 'servers': server_names
    })

def clan_members(request, server=server_names[0], clanid=0):

    q = '''SELECT characters.char_name, character_subclasses.level, characters.sex,
characters.pvpkills, characters.pkkills, characters.online, characters.onlinetime,
char_templates.ClassName, clan_data.clan_name, clan_data.clan_id
		FROM `characters`
		LEFT JOIN `character_subclasses` ON characters.obj_Id = character_subclasses.char_obj_id
		AND character_subclasses.isBase='1'
		LEFT JOIN `char_templates` ON character_subclasses.class_id = char_templates.ClassId
		LEFT JOIN `clan_data` ON characters.clanid = clan_data.clan_id
		WHERE characters.clanid=%s
		ORDER BY character_subclasses.level DESC
		'''

    query = ClanData.objects.using(server).raw(q, [clanid])

    return render(request, "clan_members.html", {
        'query': query, 'server': server, 'servers': server_names
    })