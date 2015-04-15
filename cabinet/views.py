from register.models import Accounts
from register.form import ChangePasswordForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from extend_user.models import ServerLogin
import whirlpool
import base64
import hashlib
from la2.settings import hash_type, server_names
from statistics.models import Characters, Items
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def change_password(request, login):
    login = login[:-1]
    acc = Accounts.objects.get(login=login)
    query = ServerLogin.objects.using('default').filter(user_id=request.user.id, login=login)
    if query:
        if request.method == 'POST':
            form = ChangePasswordForm(request.POST)
            if form.is_valid():
                password = request.POST.get('password1', '')
                oldpass = request.POST.get('oldpassword', '')
                if hash_type == 'whirlpool':
                    password = base64.b64encode(whirlpool.new(password).digest())
                    if acc.password == base64.b64encode(whirlpool.new(oldpass).digest()):
                        acc_obj = Accounts(login=login, password=password)
                        acc_obj.save()
                        return HttpResponseRedirect("/changed/")
                elif hash_type == 'sha1':
                    password = base64.b64encode(hashlib.sha1(password).digest())
                    if acc.password == base64.b64encode(hashlib.sha1(oldpass).digest()):
                        acc_obj = Accounts(login=login, password=password)
                        acc_obj.save()

                        return HttpResponseRedirect("/changed/")
                return render(request, "change.html", {
                    'form': form, 'acc': acc,
                })
        else:
            form = ChangePasswordForm()
    else:
        return HttpResponseRedirect("/cabinet/")
    return render(request, "change.html", {
        'form': form, 'acc': acc, 'server_names': server_names,
    })


def changed(request):
    return render(request, 'changed.html')


def cabinet(request, server=server_names[0]):
    query = ServerLogin.objects.using('default').filter(user_id=request.user.id)

    return render(request, "cabinet.html", {
        'query': query, 'server': server, 'servers': server_names
    })


def show_account(request, server, login):
    check = ServerLogin.objects.using('default').filter(user_id=request.user.id, login=login)

    q = '''SELECT characters.obj_Id, characters.account_name,  characters.char_name,
character_subclasses.level, characters.accesslevel, characters.lastAccess, char_templates.ClassName
FROM `characters`
LEFT JOIN `character_subclasses` ON characters.obj_Id = character_subclasses.char_obj_id
LEFT JOIN `char_templates` ON character_subclasses.class_id = char_templates.ClassId
WHERE characters.account_name = %s '''
    if check:
        query = Characters.objects.using(server).raw(q, [login])
    else:
        return HttpResponseRedirect("/cabinet/")
    return render(request, "account.html", {
        'query': query, 'login': login, 'server': server,
    })


def show_character(request, server, login, login_id, sort='3', order='ASC'):
    # login = login
    # login_id = login_id
    page = request.GET.get('page')
    if page:
        page = int(page)
    print page
    check = ServerLogin.objects.using('default').filter(user_id=request.user.id, login=login)
    check2 = Characters.objects.using(server).filter(account_name=login, obj_id=login_id)
    character = '''SELECT characters.obj_Id, characters.account_name, characters.char_name,
character_subclasses.level, characters.sex, character_subclasses.class_id, characters.online,
character_subclasses.exp, character_subclasses.sp, characters.karma, characters.pvpkills,
characters.pkkills, characters.accesslevel, characters.onlinetime, characters.lastAccess,
char_templates.ClassName, clan_data.clan_name
		FROM `characters`
		LEFT JOIN `character_subclasses` ON characters.obj_Id = character_subclasses.char_obj_id AND character_subclasses.isBase='1'
		LEFT JOIN `char_templates` ON character_subclasses.class_id = char_templates.ClassId
		LEFT JOIN `clan_data` ON characters.clanid = clan_data.clan_id
		WHERE characters.obj_Id= %s '''
    items = '''
SELECT items.object_id, items.item_id, items.count,items.enchant_level,items.loc,
			CASE WHEN armor.name != '' THEN armor.name
			WHEN weapon.name != '' THEN weapon.name
			WHEN etcitem.name != '' THEN etcitem.name
			END AS name,
			CASE WHEN armor.crystal_type != '' THEN 'armor'
			WHEN weapon.crystal_type != '' THEN 'weapon'
			WHEN etcitem.crystal_type != '' THEN 'etc'
			END AS `type`
		FROM `items`
		LEFT JOIN `armor` ON armor.item_id = items.item_id
		LEFT JOIN weapon ON weapon.item_id = items .item_id
		LEFT JOIN etcitem ON etcitem.item_id = items.item_id
		WHERE items.owner_id=%s
		ORDER BY %s
    '''
    if order == 'asc' or order == 'desc':
        items += str(order)
    if check and check2:
        char_query = Characters.objects.using(server).raw(character, [login_id])
        items_query = Items.objects.using(server).raw(items, [login_id, int(sort)])
        paginator = Paginator(items_query, 10)
        paginator._count = len(list(items_query))

        try:
            items_pag = paginator.page(page)
        except PageNotAnInteger:
            items_pag = paginator.page(1)
        except EmptyPage:
            items_pag = paginator.page(paginator.num_pages)
    else:
        return HttpResponseRedirect("/cabinet/" + server + '/' + login + '/')
    return render(request, "show_character.html", {
        'char_query': char_query, 'items_pag': items_pag, 'login': login, 'id': id, 'server': server,

    })