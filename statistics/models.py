# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AiParams(models.Model):
    npc_id = models.IntegerField()
    name = models.CharField(max_length=45, blank=True)
    param = models.CharField(max_length=25)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ai_params'


class AllyData(models.Model):
    ally_id = models.IntegerField(primary_key=True)
    ally_name = models.CharField(max_length=45, blank=True)
    leader_id = models.IntegerField()
    expelled_member = models.IntegerField()
    crest = models.CharField(max_length=192, blank=True)

    class Meta:
        managed = False
        db_table = 'ally_data'


class Armor(models.Model):
    item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    additional_name = models.CharField(max_length=128)
    bodypart = models.CharField(max_length=16)
    crystallizable = models.CharField(max_length=5)
    armor_type = models.CharField(max_length=12)
    player_class = models.CharField(max_length=12, blank=True)
    weight = models.IntegerField()
    crystal_type = models.CharField(max_length=4)
    avoid_modify = models.IntegerField()
    durability = models.IntegerField()
    temporal = models.IntegerField()
    p_def = models.IntegerField()
    m_def = models.IntegerField()
    mp_bonus = models.IntegerField()
    price = models.IntegerField()
    crystal_count = models.IntegerField()
    sellable = models.CharField(max_length=5)
    icon = models.CharField(max_length=128)
    dropable = models.IntegerField()
    destroyable = models.IntegerField()
    tradeable = models.IntegerField()
    flags = models.IntegerField()
    skill_id = models.CharField(max_length=20)
    skill_level = models.CharField(max_length=12)
    enchant4_skill_id = models.IntegerField()
    enchant4_skill_lvl = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'armor'


class ArmorEx(models.Model):
    item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    crystal_type = models.CharField(max_length=4)
    uns1 = models.IntegerField()
    uns2 = models.IntegerField()
    uns3 = models.IntegerField()
    foundation = models.IntegerField()
    srare1 = models.IntegerField()
    srare2 = models.IntegerField()
    srare3 = models.IntegerField()
    rare1 = models.IntegerField()
    rare2 = models.IntegerField()
    rare3 = models.IntegerField()
    pvp = models.IntegerField()
    common = models.IntegerField()
    unsc1 = models.IntegerField()
    unsc2 = models.IntegerField()
    unsc3 = models.IntegerField()
    varnish = models.IntegerField()
    unseal = models.IntegerField()
    reseal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'armor_ex'




class Auction(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sellerid = models.IntegerField(db_column='sellerId')  # Field name made lowercase.
    sellername = models.CharField(db_column='sellerName', max_length=50)  # Field name made lowercase.
    sellerclanname = models.CharField(db_column='sellerClanName', max_length=50)  # Field name made lowercase.
    itemname = models.CharField(db_column='itemName', max_length=40)  # Field name made lowercase.
    startingbid = models.BigIntegerField(db_column='startingBid')  # Field name made lowercase.
    currentbid = models.BigIntegerField(db_column='currentBid')  # Field name made lowercase.
    enddate = models.DecimalField(db_column='endDate', max_digits=20, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auction'




class AutoChat(models.Model):
    groupid = models.IntegerField(db_column='groupId')  # Field name made lowercase.
    npcid = models.IntegerField(db_column='npcId')  # Field name made lowercase.
    chatdelay = models.IntegerField(db_column='chatDelay')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auto_chat'


class AutoChatText(models.Model):
    groupid = models.IntegerField(db_column='groupId')  # Field name made lowercase.
    chattext = models.CharField(db_column='chatText', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auto_chat_text'


class Bans(models.Model):
    account_name = models.CharField(max_length=45, blank=True)
    obj_id = models.IntegerField(db_column='obj_Id')  # Field name made lowercase.
    baned = models.CharField(max_length=20, blank=True)
    unban = models.CharField(max_length=20, blank=True)
    reason = models.CharField(max_length=200, blank=True)
    gm = models.CharField(db_column='GM', max_length=35, blank=True)  # Field name made lowercase.
    endban = models.IntegerField(blank=True, null=True)
    karma = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bans'


class Bonus(models.Model):
    obj_id = models.IntegerField()
    bonus_name = models.CharField(max_length=30)
    bonus_value = models.IntegerField()
    bonus_expire_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bonus'


class Castle(models.Model):
    id = models.IntegerField()
    name = models.CharField(primary_key=True, max_length=25)
    taxpercent = models.IntegerField(db_column='taxPercent')  # Field name made lowercase.
    treasury = models.BigIntegerField()
    siegedate = models.IntegerField(db_column='siegeDate')  # Field name made lowercase.
    siegedayofweek = models.IntegerField(db_column='siegeDayOfWeek')  # Field name made lowercase.
    siegehourofday = models.IntegerField(db_column='siegeHourOfDay')  # Field name made lowercase.
    townid = models.IntegerField(db_column='townId')  # Field name made lowercase.
    skills = models.CharField(max_length=32)
    flags = models.CharField(max_length=32)
    owndate = models.IntegerField(db_column='ownDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'castle'


class CastleManorProcure(models.Model):
    castle_id = models.IntegerField()
    crop_id = models.IntegerField()
    can_buy = models.BigIntegerField()
    start_buy = models.BigIntegerField()
    price = models.BigIntegerField()
    reward_type = models.IntegerField()
    period = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'castle_manor_procure'


class CastleManorProduction(models.Model):
    castle_id = models.IntegerField()
    seed_id = models.IntegerField()
    can_produce = models.BigIntegerField()
    start_produce = models.BigIntegerField()
    seed_price = models.BigIntegerField()
    period = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'castle_manor_production'


class CharTemplates(models.Model):
    classid = models.IntegerField(db_column='ClassId', primary_key=True)  # Field name made lowercase.
    classname = models.CharField(db_column='ClassName', max_length=20)  # Field name made lowercase.
    raceid = models.IntegerField(db_column='RaceId')  # Field name made lowercase.
    parent = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    str = models.IntegerField(db_column='STR')  # Field name made lowercase.
    con = models.IntegerField(db_column='CON')  # Field name made lowercase.
    dex = models.IntegerField(db_column='DEX')  # Field name made lowercase.
    field_int = models.IntegerField(db_column='_INT')  # Field name made lowercase. Field renamed because it started with '_'.
    wit = models.IntegerField(db_column='WIT')  # Field name made lowercase.
    men = models.IntegerField(db_column='MEN')  # Field name made lowercase.
    p_atk = models.IntegerField(db_column='P_ATK')  # Field name made lowercase.
    p_def = models.IntegerField(db_column='P_DEF')  # Field name made lowercase.
    m_atk = models.IntegerField(db_column='M_ATK')  # Field name made lowercase.
    m_def = models.IntegerField(db_column='M_DEF')  # Field name made lowercase.
    p_spd = models.IntegerField(db_column='P_SPD')  # Field name made lowercase.
    m_spd = models.IntegerField(db_column='M_SPD')  # Field name made lowercase.
    acc = models.IntegerField(db_column='ACC')  # Field name made lowercase.
    critical = models.IntegerField(db_column='CRITICAL')  # Field name made lowercase.
    evasion = models.IntegerField(db_column='EVASION')  # Field name made lowercase.
    run_spd = models.IntegerField(db_column='RUN_SPD')  # Field name made lowercase.
    walk_spd = models.IntegerField(db_column='WALK_SPD')  # Field name made lowercase.
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    cancraft = models.IntegerField(db_column='canCraft')  # Field name made lowercase.
    m_unk1 = models.DecimalField(db_column='M_UNK1', max_digits=4, decimal_places=2)  # Field name made lowercase.
    m_unk2 = models.DecimalField(db_column='M_UNK2', max_digits=8, decimal_places=6)  # Field name made lowercase.
    m_col_r = models.DecimalField(db_column='M_COL_R', max_digits=3, decimal_places=1)  # Field name made lowercase.
    m_col_h = models.DecimalField(db_column='M_COL_H', max_digits=4, decimal_places=1)  # Field name made lowercase.
    f_unk1 = models.DecimalField(db_column='F_UNK1', max_digits=4, decimal_places=2)  # Field name made lowercase.
    f_unk2 = models.DecimalField(db_column='F_UNK2', max_digits=8, decimal_places=6)  # Field name made lowercase.
    f_col_r = models.DecimalField(db_column='F_COL_R', max_digits=3, decimal_places=1)  # Field name made lowercase.
    f_col_h = models.DecimalField(db_column='F_COL_H', max_digits=4, decimal_places=1)  # Field name made lowercase.
    items1 = models.IntegerField()
    items2 = models.IntegerField()
    items3 = models.IntegerField()
    items4 = models.IntegerField()
    items5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_templates'


class CharacterBlocklist(models.Model):
    obj_id = models.IntegerField(db_column='obj_Id')  # Field name made lowercase.
    target_id = models.IntegerField(db_column='target_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'character_blocklist'


class CharacterBookmarks(models.Model):
    char_id = models.IntegerField(db_column='char_Id')  # Field name made lowercase.
    idx = models.IntegerField()
    name = models.CharField(max_length=32)
    acronym = models.CharField(max_length=4)
    icon = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_bookmarks'


class CharacterCash(models.Model):
    char_obj_id = models.IntegerField(primary_key=True)
    char_name = models.CharField(max_length=35, blank=True)
    cash = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_cash'


class CharacterEffectsSave(models.Model):
    char_obj_id = models.IntegerField()
    skill_id = models.IntegerField()
    skill_level = models.IntegerField()
    effect_count = models.IntegerField()
    effect_cur_time = models.IntegerField()
    duration = models.IntegerField()
    order = models.IntegerField()
    class_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_effects_save'


class CharacterFriends(models.Model):
    char_id = models.IntegerField()
    friend_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_friends'


class CharacterHennas(models.Model):
    char_obj_id = models.IntegerField()
    symbol_id = models.IntegerField()
    slot = models.IntegerField()
    class_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_hennas'


class CharacterL2TopVotes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=20)
    time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_l2top_votes'



class CharacterMmotopVotes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=20)
    time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_mmotop_votes'


class CharacterQuests(models.Model):
    char_id = models.IntegerField()
    name = models.CharField(max_length=40)
    var = models.CharField(max_length=20)
    value = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'character_quests'




class CharacterShortcuts(models.Model):
    char_obj_id = models.IntegerField()
    slot = models.IntegerField()
    page = models.IntegerField()
    type = models.IntegerField(blank=True, null=True)
    shortcut_id = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    class_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_shortcuts'


class CharacterSkills(models.Model):
    char_obj_id = models.IntegerField()
    skill_id = models.IntegerField()
    skill_level = models.IntegerField()
    skill_name = models.CharField(max_length=40, blank=True)
    class_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_skills'


class CharacterSkillsSave(models.Model):
    char_obj_id = models.IntegerField()
    skill_id = models.IntegerField()
    class_index = models.IntegerField()
    end_time = models.BigIntegerField()
    reuse_delay_org = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_skills_save'


class CharacterSubclasses(models.Model):
    char_obj_id = models.IntegerField()
    class_id = models.IntegerField()
    level = models.IntegerField()
    exp = models.BigIntegerField()
    sp = models.BigIntegerField()
    curhp = models.DecimalField(db_column='curHp', max_digits=9, decimal_places=4)  # Field name made lowercase.
    curmp = models.DecimalField(db_column='curMp', max_digits=9, decimal_places=4)  # Field name made lowercase.
    curcp = models.DecimalField(db_column='curCp', max_digits=11, decimal_places=4)  # Field name made lowercase.
    maxhp = models.IntegerField(db_column='maxHp')  # Field name made lowercase.
    maxmp = models.IntegerField(db_column='maxMp')  # Field name made lowercase.
    maxcp = models.IntegerField(db_column='maxCp')  # Field name made lowercase.
    active = models.IntegerField()
    isbase = models.IntegerField(db_column='isBase')  # Field name made lowercase.
    death_penalty = models.IntegerField()
    skills = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'character_subclasses'


class CharacterVariables(models.Model):
    obj_id = models.IntegerField()
    type = models.CharField(max_length=86)
    name = models.CharField(max_length=86)
    value = models.TextField()
    expire_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_variables'


class Characters(models.Model):
    account_name = models.CharField(max_length=45)
    obj_id = models.IntegerField(db_column='obj_Id', primary_key=True)  # Field name made lowercase.
    char_name = models.CharField(unique=True, max_length=35)
    face = models.IntegerField(blank=True, null=True)
    hairstyle = models.IntegerField(db_column='hairStyle', blank=True, null=True)  # Field name made lowercase.
    haircolor = models.IntegerField(db_column='hairColor', blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(blank=True, null=True)
    heading = models.IntegerField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    z = models.IntegerField(blank=True, null=True)
    karma = models.IntegerField(blank=True, null=True)
    pvpkills = models.IntegerField(blank=True, null=True)
    pkkills = models.IntegerField(blank=True, null=True)
    clanid = models.IntegerField(blank=True, null=True)
    createtime = models.IntegerField()
    deletetime = models.IntegerField()
    title = models.CharField(max_length=16, blank=True)
    rec_have = models.IntegerField()
    rec_left = models.IntegerField()
    accesslevel = models.IntegerField(blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)
    onlinetime = models.IntegerField()
    lastaccess = models.IntegerField(db_column='lastAccess')  # Field name made lowercase.
    leaveclan = models.IntegerField()
    deleteclan = models.IntegerField()
    nochannel = models.IntegerField()
    pledge_type = models.IntegerField()
    pledge_rank = models.IntegerField()
    lvl_joined_academy = models.IntegerField()
    apprentice = models.IntegerField()
    key_bindings = models.CharField(max_length=8192, blank=True)
    pcbangpoints = models.IntegerField(db_column='pcBangPoints')  # Field name made lowercase.
    vitality = models.IntegerField()
    fame = models.IntegerField()
    bookmarks = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'characters'


class ClanData(models.Model):
    clan_id = models.IntegerField(primary_key=True)
    clan_name = models.CharField(max_length=45, blank=True)
    clan_level = models.IntegerField()
    hascastle = models.IntegerField(db_column='hasCastle')  # Field name made lowercase.
    hasfortress = models.IntegerField(db_column='hasFortress')  # Field name made lowercase.
    hashideout = models.IntegerField(db_column='hasHideout')  # Field name made lowercase.
    ally_id = models.IntegerField()
    leader_id = models.IntegerField()
    crest = models.CharField(max_length=256, blank=True)
    largecrest = models.CharField(max_length=8192, blank=True)
    reputation_score = models.IntegerField()
    warehouse = models.IntegerField()
    expelled_member = models.IntegerField()
    leaved_ally = models.IntegerField()
    dissolved_ally = models.IntegerField()
    auction_bid_at = models.IntegerField()
    airship = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_data'


class ClanNotices(models.Model):
    clanid = models.IntegerField(db_column='clanID', primary_key=True)  # Field name made lowercase.
    notice = models.CharField(max_length=512)
    enabled = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'clan_notices'


class ClanPrivs(models.Model):
    clan_id = models.IntegerField()
    rank = models.IntegerField()
    privilleges = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_privs'


class ClanSkills(models.Model):
    clan_id = models.IntegerField()
    skill_id = models.IntegerField()
    skill_level = models.IntegerField()
    skill_name = models.CharField(max_length=26, blank=True)

    class Meta:
        managed = False
        db_table = 'clan_skills'


class ClanSubpledges(models.Model):
    clan_id = models.IntegerField()
    type = models.IntegerField()
    name = models.CharField(max_length=45)
    leader_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_subpledges'


class ClanWars(models.Model):
    clan1 = models.IntegerField()
    clan2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_wars'


class ClassList(models.Model):
    class_name = models.CharField(max_length=19)
    id = models.IntegerField(primary_key=True)  # AutoField?
    parent_id = models.IntegerField()
    parent_id2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'class_list'


class Couples(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    player1id = models.IntegerField(db_column='player1Id')  # Field name made lowercase.
    player2id = models.IntegerField(db_column='player2Id')  # Field name made lowercase.
    maried = models.CharField(max_length=5, blank=True)
    affianceddate = models.BigIntegerField(db_column='affiancedDate', blank=True, null=True)  # Field name made lowercase.
    weddingdate = models.BigIntegerField(db_column='weddingDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'couples'


class Craftcount(models.Model):
    char_id = models.IntegerField()
    item_id = models.IntegerField()
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'craftcount'


class CursedWeapons(models.Model):
    item_id = models.IntegerField(primary_key=True)
    player_id = models.IntegerField()
    player_karma = models.IntegerField()
    player_pkkills = models.IntegerField()
    nb_kills = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    end_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cursed_weapons'


class Dropcount(models.Model):
    char_id = models.IntegerField()
    item_id = models.IntegerField()
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dropcount'


class Droplist(models.Model):
    mobid = models.IntegerField(db_column='mobId')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId')  # Field name made lowercase.
    min = models.IntegerField()
    max = models.IntegerField()
    sweep = models.IntegerField()
    chance = models.IntegerField()
    category = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'droplist'


class EpicBossSpawn(models.Model):
    bossid = models.IntegerField(db_column='bossId', primary_key=True)  # Field name made lowercase.
    respawndate = models.IntegerField(db_column='respawnDate')  # Field name made lowercase.
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'epic_boss_spawn'


class Etcitem(models.Model):
    item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    additional_name = models.CharField(max_length=128)
    class_field = models.CharField(db_column='class', max_length=10)  # Field renamed because it was a Python reserved word.
    crystallizable = models.CharField(max_length=5)
    item_type = models.CharField(max_length=12)
    weight = models.IntegerField()
    consume_type = models.CharField(max_length=12)
    crystal_type = models.CharField(max_length=4)
    durability = models.IntegerField()
    temporal = models.IntegerField()
    price = models.IntegerField()
    crystal_count = models.IntegerField()
    sellable = models.CharField(max_length=5)
    skill_id = models.CharField(max_length=20)
    skill_level = models.CharField(max_length=12)
    icon = models.CharField(max_length=128)
    dropable = models.IntegerField()
    destroyable = models.IntegerField()
    tradeable = models.IntegerField()
    flags = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'etcitem'





class Fishreward(models.Model):
    fishid = models.IntegerField()
    rewardid = models.IntegerField()
    min = models.IntegerField()
    max = models.IntegerField()
    chance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fishreward'


class Forts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=45)
    lastsiegedate = models.IntegerField(db_column='lastSiegeDate')  # Field name made lowercase.
    siegedate = models.IntegerField(db_column='siegeDate')  # Field name made lowercase.
    skills = models.CharField(max_length=32)
    owndate = models.IntegerField(db_column='ownDate')  # Field name made lowercase.
    state = models.IntegerField()
    castleid = models.IntegerField(db_column='castleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forts'


class FourSepulchersSpawnlist(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    location = models.CharField(max_length=19)
    count = models.IntegerField()
    npc_templateid = models.IntegerField()
    locx = models.IntegerField()
    locy = models.IntegerField()
    locz = models.IntegerField()
    randomx = models.IntegerField()
    randomy = models.IntegerField()
    heading = models.IntegerField()
    respawn_delay = models.IntegerField()
    key_npc_id = models.IntegerField()
    spawntype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'four_sepulchers_spawnlist'


class GameLog(models.Model):
    serv_id = models.IntegerField()
    act_time = models.IntegerField()
    log_id = models.IntegerField()
    actor = models.IntegerField()
    actor_type = models.CharField(max_length=75)
    target = models.IntegerField()
    target_type = models.CharField(max_length=75)
    location_x = models.IntegerField(blank=True, null=True)
    location_y = models.IntegerField(blank=True, null=True)
    location_z = models.IntegerField(blank=True, null=True)
    etc_str1 = models.CharField(max_length=50, blank=True)
    etc_str2 = models.CharField(max_length=50, blank=True)
    etc_str3 = models.CharField(max_length=50, blank=True)
    etc_num1 = models.IntegerField()
    etc_num2 = models.IntegerField()
    etc_num3 = models.IntegerField()
    etc_num4 = models.IntegerField()
    etc_num5 = models.IntegerField()
    etc_num6 = models.IntegerField()
    etc_num7 = models.IntegerField()
    etc_num8 = models.IntegerField()
    etc_num9 = models.BigIntegerField()
    etc_num10 = models.BigIntegerField()
    str_actor = models.CharField(db_column='STR_actor', max_length=50, blank=True)  # Field name made lowercase.
    str_actor_account = models.CharField(db_column='STR_actor_account', max_length=50, blank=True)  # Field name made lowercase.
    str_target = models.CharField(db_column='STR_target', max_length=50, blank=True)  # Field name made lowercase.
    str_target_account = models.CharField(db_column='STR_target_account', max_length=50, blank=True)  # Field name made lowercase.
    item_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_log'



class GlobalTasks(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    task = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    last_activation = models.IntegerField()
    param1 = models.CharField(max_length=100)
    param2 = models.CharField(max_length=100)
    param3 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'global_tasks'


class Henna(models.Model):
    symbol_id = models.IntegerField(primary_key=True)
    symbol_name = models.CharField(max_length=15, blank=True)
    dye_id = models.IntegerField()
    dye_amount = models.IntegerField()
    price = models.IntegerField()
    stat_int = models.IntegerField(db_column='stat_INT')  # Field name made lowercase.
    stat_str = models.IntegerField(db_column='stat_STR')  # Field name made lowercase.
    stat_con = models.IntegerField(db_column='stat_CON')  # Field name made lowercase.
    stat_mem = models.IntegerField(db_column='stat_MEM')  # Field name made lowercase.
    stat_dex = models.IntegerField(db_column='stat_DEX')  # Field name made lowercase.
    stat_wit = models.IntegerField(db_column='stat_WIT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'henna'


class HennaTrees(models.Model):
    class_id = models.IntegerField()
    symbol_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'henna_trees'


class Heroes(models.Model):
    char_id = models.IntegerField(primary_key=True)
    count = models.IntegerField()
    played = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'heroes'


class ItemAttributes(models.Model):
    itemid = models.IntegerField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    augattributes = models.IntegerField(db_column='augAttributes')  # Field name made lowercase.
    augskillid = models.IntegerField(db_column='augSkillId')  # Field name made lowercase.
    augskilllevel = models.IntegerField(db_column='augSkillLevel')  # Field name made lowercase.
    elemtype = models.IntegerField(db_column='elemType')  # Field name made lowercase.
    elemvalue = models.IntegerField(db_column='elemValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_attributes'


class ItemMall(models.Model):
    ord = models.IntegerField()
    name = models.CharField(max_length=255, blank=True)
    itemid = models.IntegerField(db_column='itemId')  # Field name made lowercase.
    count = models.IntegerField()
    price = models.IntegerField()
    icategory2 = models.IntegerField(db_column='iCategory2')  # Field name made lowercase.
    onsale = models.IntegerField(db_column='onSale')  # Field name made lowercase.
    istartsale = models.IntegerField(db_column='iStartSale')  # Field name made lowercase.
    iendsale = models.IntegerField(db_column='iEndSale')  # Field name made lowercase.
    istarthour = models.IntegerField(db_column='iStartHour')  # Field name made lowercase.
    istartmin = models.IntegerField(db_column='iStartMin')  # Field name made lowercase.
    iendhour = models.IntegerField(db_column='iEndHour')  # Field name made lowercase.
    iendmin = models.IntegerField(db_column='iEndMin')  # Field name made lowercase.
    istock = models.IntegerField(db_column='iStock')  # Field name made lowercase.
    imaxstock = models.IntegerField(db_column='iMaxStock')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_mall'


class Items(models.Model):
    object_id = models.IntegerField(primary_key=True)
    owner_id = models.IntegerField()
    item_id = models.IntegerField()
    name = models.CharField(max_length=65, blank=True)
    count = models.BigIntegerField()
    enchant_level = models.IntegerField()
    class_field = models.CharField(db_column='class', max_length=10)  # Field renamed because it was a Python reserved word.
    loc = models.CharField(max_length=9)
    loc_data = models.IntegerField(blank=True, null=True)
    custom_type1 = models.IntegerField()
    custom_type2 = models.IntegerField()
    shadow_life_time = models.IntegerField()
    flags = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'items'


class ItemsDelayed(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    owner_id = models.IntegerField()
    item_id = models.IntegerField()
    count = models.IntegerField()
    enchant_level = models.IntegerField()
    attribute = models.IntegerField()
    attribute_level = models.IntegerField()
    flags = models.IntegerField()
    payment_status = models.IntegerField()
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'items_delayed'


class Killcount(models.Model):
    char_id = models.IntegerField()
    npc_id = models.IntegerField()
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'killcount'


class LastimperialtombSpawnlist(models.Model):
    count = models.IntegerField()
    npc_templateid = models.IntegerField()
    locx = models.IntegerField()
    locy = models.IntegerField()
    locz = models.IntegerField()
    heading = models.IntegerField()
    respawn_delay = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lastimperialtomb_spawnlist'


class Locations(models.Model):
    loc_id = models.IntegerField()
    name = models.CharField(max_length=50)
    loc_x = models.IntegerField()
    loc_y = models.IntegerField()
    loc_zmin = models.IntegerField()
    loc_zmax = models.IntegerField()
    radius = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'locations'


class Lvlupgain(models.Model):
    classid = models.IntegerField(primary_key=True)
    defaulthpbase = models.DecimalField(max_digits=5, decimal_places=1)
    defaulthpadd = models.DecimalField(max_digits=4, decimal_places=2)
    defaulthpmod = models.DecimalField(max_digits=4, decimal_places=2)
    defaultcpbase = models.DecimalField(max_digits=5, decimal_places=1)
    defaultcpadd = models.DecimalField(max_digits=4, decimal_places=2)
    defaultcpmod = models.DecimalField(max_digits=4, decimal_places=2)
    defaultmpbase = models.DecimalField(max_digits=5, decimal_places=1)
    defaultmpadd = models.DecimalField(max_digits=4, decimal_places=2)
    defaultmpmod = models.DecimalField(max_digits=4, decimal_places=2)
    class_lvl = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lvlupgain'


class Mail(models.Model):
    messageid = models.IntegerField(db_column='messageId', primary_key=True)  # Field name made lowercase.
    sender = models.IntegerField()
    receiver = models.IntegerField()
    expire = models.DateTimeField()
    topic = models.CharField(max_length=30)
    body = models.TextField()
    attachments = models.IntegerField()
    needspayment = models.IntegerField(db_column='needsPayment')  # Field name made lowercase.
    price = models.BigIntegerField()
    system = models.IntegerField()
    unread = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mail'


class MailAttachments(models.Model):
    messageid = models.IntegerField(db_column='messageId')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mail_attachments'


class Mapregion(models.Model):
    y10_plus = models.IntegerField(primary_key=True)
    x11 = models.IntegerField()
    x12 = models.IntegerField()
    x13 = models.IntegerField()
    x14 = models.IntegerField()
    x15 = models.IntegerField()
    x16 = models.IntegerField()
    x17 = models.IntegerField()
    x18 = models.IntegerField()
    x19 = models.IntegerField()
    x20 = models.IntegerField()
    x21 = models.IntegerField()
    x22 = models.IntegerField()
    x23 = models.IntegerField()
    x24 = models.IntegerField()
    x25 = models.IntegerField()
    x26 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mapregion'


class MerchantAreasList(models.Model):
    merchant_area_id = models.IntegerField(primary_key=True)
    merchant_area_name = models.CharField(max_length=25)
    tax = models.FloatField()
    chaotic = models.IntegerField(db_column='Chaotic')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'merchant_areas_list'


class Minions(models.Model):
    boss_id = models.IntegerField()
    minion_id = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'minions'


class Npc(models.Model):
    ordinal = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=45, blank=True)
    title = models.CharField(max_length=35)
    class_field = models.CharField(db_column='class', max_length=50, blank=True)  # Field renamed because it was a Python reserved word.
    collision_radius = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    collision_height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    level = models.IntegerField()
    sex = models.CharField(max_length=6)
    type = models.CharField(max_length=30)
    ai_type = models.CharField(max_length=50)
    attackrange = models.IntegerField()
    hp = models.IntegerField()
    base_hp_regen = models.FloatField()
    mp = models.IntegerField()
    base_mp_regen = models.FloatField()
    str = models.IntegerField()
    con = models.IntegerField()
    dex = models.IntegerField()
    int = models.IntegerField()
    wit = models.IntegerField()
    men = models.IntegerField()
    exp = models.IntegerField()
    sp = models.IntegerField()
    patk = models.IntegerField()
    pdef = models.IntegerField()
    matk = models.IntegerField()
    mdef = models.IntegerField()
    atkspd = models.IntegerField()
    aggro = models.IntegerField()
    matkspd = models.IntegerField()
    rhand = models.IntegerField()
    lhand = models.IntegerField()
    armor = models.IntegerField()
    walkspd = models.IntegerField()
    runspd = models.IntegerField()
    faction_id = models.CharField(max_length=40)
    faction_range = models.IntegerField()
    displayid = models.IntegerField(db_column='displayId')  # Field name made lowercase.
    shield_defense_rate = models.IntegerField()
    shield_defense = models.IntegerField()
    corpse_time = models.IntegerField()
    base_rand_dam = models.IntegerField()
    base_critical = models.IntegerField()
    physical_hit_modify = models.IntegerField()
    base_reuse_delay = models.IntegerField()
    physical_avoid_modify = models.IntegerField()
    hit_time_factor = models.FloatField()
    isdropherbs = models.CharField(db_column='isDropHerbs', max_length=5)  # Field name made lowercase.
    shots = models.CharField(max_length=12)
    map_flag = models.IntegerField()
    boss_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'npc'


class Npcskills(models.Model):
    npcid = models.IntegerField()
    skillid = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'npcskills'


class OlympiadNobles(models.Model):
    char_id = models.IntegerField(primary_key=True)
    class_id = models.IntegerField()
    char_name = models.CharField(max_length=35)
    olympiad_points = models.IntegerField()
    olympiad_points_past = models.IntegerField()
    olympiad_points_past_static = models.IntegerField()
    competitions_done = models.IntegerField()
    competitions_win = models.IntegerField()
    competitions_loose = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'olympiad_nobles'




class Petitions(models.Model):
    serv_id = models.IntegerField()
    act_time = models.IntegerField()
    petition_type = models.IntegerField()
    actor = models.IntegerField()
    location_x = models.IntegerField(blank=True, null=True)
    location_y = models.IntegerField(blank=True, null=True)
    location_z = models.IntegerField(blank=True, null=True)
    petition_text = models.TextField()
    str_actor = models.CharField(db_column='STR_actor', max_length=50, blank=True)  # Field name made lowercase.
    str_actor_account = models.CharField(db_column='STR_actor_account', max_length=50, blank=True)  # Field name made lowercase.
    petition_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'petitions'


class Pets(models.Model):
    item_obj_id = models.IntegerField(primary_key=True)
    objid = models.IntegerField(db_column='objId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=12, blank=True)
    level = models.IntegerField(blank=True, null=True)
    curhp = models.IntegerField(db_column='curHp', blank=True, null=True)  # Field name made lowercase.
    curmp = models.IntegerField(db_column='curMp', blank=True, null=True)  # Field name made lowercase.
    exp = models.BigIntegerField(blank=True, null=True)
    sp = models.IntegerField(blank=True, null=True)
    fed = models.IntegerField(blank=True, null=True)
    max_fed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pets'


class PetsSkills(models.Model):
    templateid = models.IntegerField(db_column='templateId')  # Field name made lowercase.
    minlvl = models.IntegerField(db_column='minLvl')  # Field name made lowercase.
    skillid = models.IntegerField(db_column='skillId')  # Field name made lowercase.
    skilllvl = models.IntegerField(db_column='skillLvl')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pets_skills'


class Prices(models.Model):
    item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    additional_name = models.CharField(max_length=40)
    price = models.IntegerField()
    weight = models.IntegerField()
    crystal_type = models.CharField(max_length=4)
    crystal_count = models.IntegerField()
    crystallizable = models.CharField(max_length=5)
    item_type = models.CharField(max_length=11)
    consume_type = models.CharField(max_length=9)
    class_field = models.CharField(db_column='class', max_length=10)  # Field renamed because it was a Python reserved word.
    icon = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'prices'


class RaidbossPoints(models.Model):
    owner_id = models.IntegerField()
    boss_id = models.IntegerField()
    points = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'raidboss_points'


class RaidbossStatus(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    current_hp = models.IntegerField(blank=True, null=True)
    current_mp = models.IntegerField(blank=True, null=True)
    respawn_delay = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'raidboss_status'


class RandomSpawn(models.Model):
    groupid = models.IntegerField(db_column='groupId', primary_key=True)  # Field name made lowercase.
    npcid = models.IntegerField(db_column='npcId')  # Field name made lowercase.
    count = models.IntegerField()
    initialdelay = models.BigIntegerField(db_column='initialDelay')  # Field name made lowercase.
    respawndelay = models.BigIntegerField(db_column='respawnDelay')  # Field name made lowercase.
    despawndelay = models.BigIntegerField(db_column='despawnDelay')  # Field name made lowercase.
    broadcastspawn = models.CharField(db_column='broadcastSpawn', max_length=5)  # Field name made lowercase.
    randomspawn = models.CharField(db_column='randomSpawn', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'random_spawn'


class RandomSpawnLoc(models.Model):
    groupid = models.IntegerField(db_column='groupId')  # Field name made lowercase.
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    heading = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'random_spawn_loc'


class Recipes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=40, blank=True)
    item = models.IntegerField()
    foundation = models.IntegerField()
    q = models.IntegerField()
    lvl = models.IntegerField()
    success = models.IntegerField()
    recid = models.IntegerField()
    mp = models.IntegerField()
    exp = models.IntegerField()
    sp = models.IntegerField()
    dwarven = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recipes'


class Recitems(models.Model):
    rid = models.IntegerField()
    item = models.IntegerField()
    q = models.IntegerField()
    has_recipe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recitems'





class ServerVariables(models.Model):
    name = models.CharField(primary_key=True, max_length=86)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'server_variables'


class SevenSigns(models.Model):
    char_obj_id = models.IntegerField(primary_key=True)
    cabal = models.CharField(max_length=8)
    seal = models.IntegerField()
    dawn_red_stones = models.IntegerField()
    dawn_green_stones = models.IntegerField()
    dawn_blue_stones = models.IntegerField()
    dawn_ancient_adena_amount = models.IntegerField()
    dawn_contribution_score = models.IntegerField()
    dusk_red_stones = models.IntegerField()
    dusk_green_stones = models.IntegerField()
    dusk_blue_stones = models.IntegerField()
    dusk_ancient_adena_amount = models.IntegerField()
    dusk_contribution_score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'seven_signs'


class SevenSignsFestival(models.Model):
    festivalid = models.IntegerField(db_column='festivalId')  # Field name made lowercase.
    cabal = models.CharField(max_length=4)
    cycle = models.IntegerField()
    date = models.BigIntegerField(blank=True, null=True)
    score = models.IntegerField()
    members = models.CharField(max_length=255)
    names = models.TextField()

    class Meta:
        managed = False
        db_table = 'seven_signs_festival'


class SevenSignsStatus(models.Model):
    current_cycle = models.IntegerField()
    festival_cycle = models.IntegerField()
    active_period = models.IntegerField()
    date = models.IntegerField()
    previous_winner = models.IntegerField()
    dawn_stone_score = models.BigIntegerField()
    dawn_festival_score = models.BigIntegerField()
    dusk_stone_score = models.BigIntegerField()
    dusk_festival_score = models.BigIntegerField()
    avarice_owner = models.IntegerField()
    gnosis_owner = models.IntegerField()
    strife_owner = models.IntegerField()
    avarice_dawn_score = models.IntegerField()
    gnosis_dawn_score = models.IntegerField()
    strife_dawn_score = models.IntegerField()
    avarice_dusk_score = models.IntegerField()
    gnosis_dusk_score = models.IntegerField()
    strife_dusk_score = models.IntegerField()
    accumulated_bonus0 = models.BigIntegerField()
    accumulated_bonus1 = models.BigIntegerField()
    accumulated_bonus2 = models.BigIntegerField()
    accumulated_bonus3 = models.BigIntegerField()
    accumulated_bonus4 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'seven_signs_status'


class SiegeClans(models.Model):
    unit_id = models.IntegerField()
    clan_id = models.IntegerField()
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'siege_clans'


class SiegeDoor(models.Model):
    unitid = models.IntegerField(db_column='unitId')  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'siege_door'


class SiegeDoorupgrade(models.Model):
    doorid = models.IntegerField(db_column='doorId', primary_key=True)  # Field name made lowercase.
    hp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'siege_doorupgrade'


class SiegeGuards(models.Model):
    unitid = models.IntegerField(db_column='unitId')  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)  # AutoField?
    npcid = models.IntegerField(db_column='npcId')  # Field name made lowercase.
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    heading = models.IntegerField()
    respawndelay = models.IntegerField(db_column='respawnDelay')  # Field name made lowercase.
    ishired = models.IntegerField(db_column='isHired')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'siege_guards'


class SiegeTerritoryMembers(models.Model):
    obj_id = models.IntegerField(db_column='obj_Id', primary_key=True)  # Field name made lowercase.
    side = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'siege_territory_members'


class SkillLearn(models.Model):
    npc_id = models.IntegerField()
    class_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skill_learn'


class SkillSpellbooks(models.Model):
    skill_id = models.IntegerField()
    level = models.IntegerField()
    item_id = models.IntegerField()
    item_count = models.IntegerField()
    min_level = models.IntegerField()
    item_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'skill_spellbooks'


class SkillTrees(models.Model):
    class_id = models.IntegerField()
    skill_id = models.IntegerField()
    level = models.IntegerField()
    name = models.CharField(max_length=50)
    sp = models.IntegerField()
    min_level = models.IntegerField()
    rep = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skill_trees'



class Spawnlist(models.Model):
    location = models.CharField(max_length=35)
    count = models.IntegerField()
    npc_templateid = models.IntegerField()
    locx = models.IntegerField()
    locy = models.IntegerField()
    locz = models.IntegerField()
    heading = models.IntegerField()
    respawn_delay = models.IntegerField()
    respawn_delay_rnd = models.IntegerField()
    loc_id = models.IntegerField()
    periodofday = models.IntegerField(db_column='periodOfDay')  # Field name made lowercase.
    reflection = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'spawnlist'


class TournamentClassList(models.Model):
    class_name = models.CharField(max_length=19)
    class_id = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tournament_class_list'


class TournamentTable(models.Model):
    category = models.IntegerField(blank=True, null=True)
    team1id = models.IntegerField(blank=True, null=True)
    team1name = models.CharField(max_length=255, blank=True)
    team2id = models.IntegerField(blank=True, null=True)
    team2name = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'tournament_table'


class TournamentTeams(models.Model):
    obj_id = models.IntegerField()
    type = models.IntegerField(blank=True, null=True)
    team_id = models.IntegerField()
    team_name = models.CharField(max_length=255, blank=True)
    leader = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField()
    losts = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tournament_teams'


class TournamentVariables(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    value = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'tournament_variables'


class Weapon(models.Model):
    item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    additional_name = models.CharField(max_length=128)
    bodypart = models.CharField(max_length=16)
    crystallizable = models.CharField(max_length=5)
    weight = models.IntegerField()
    soulshots = models.IntegerField()
    spiritshots = models.IntegerField()
    crystal_type = models.CharField(max_length=4)
    p_dam = models.IntegerField()
    rnd_dam = models.IntegerField()
    weapontype = models.CharField(db_column='weaponType', max_length=12)  # Field name made lowercase.
    critical = models.IntegerField()
    hit_modify = models.IntegerField()
    avoid_modify = models.IntegerField()
    shield_def = models.IntegerField()
    shield_def_rate = models.IntegerField()
    atk_speed = models.IntegerField()
    mp_consume = models.IntegerField()
    m_dam = models.IntegerField()
    durability = models.IntegerField()
    temporal = models.IntegerField()
    price = models.IntegerField()
    crystal_count = models.IntegerField()
    sellable = models.CharField(max_length=5)
    icon = models.CharField(max_length=128)
    dropable = models.IntegerField()
    destroyable = models.IntegerField()
    tradeable = models.IntegerField()
    flags = models.IntegerField()
    skill_id = models.CharField(max_length=20)
    skill_level = models.CharField(max_length=12)
    enchant4_skill_id = models.IntegerField()
    enchant4_skill_lvl = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'weapon'


class WeaponEx(models.Model):
    item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    crystal_type = models.CharField(max_length=4)
    foundation = models.IntegerField()
    rare = models.IntegerField()
    sa1 = models.IntegerField()
    sa2 = models.IntegerField()
    sa3 = models.IntegerField()
    raresa1 = models.IntegerField()
    raresa2 = models.IntegerField()
    raresa3 = models.IntegerField()
    pvp1 = models.IntegerField()
    pvp2 = models.IntegerField()
    pvp3 = models.IntegerField()
    rarepvp1 = models.IntegerField()
    rarepvp2 = models.IntegerField()
    rarepvp3 = models.IntegerField()
    common = models.IntegerField()
    kamaex = models.IntegerField()
    sacry1 = models.IntegerField()
    sacry2 = models.IntegerField()
    sacry3 = models.IntegerField()
    varnish = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'weapon_ex'
