from register.models import Accounts
from register.form import UserCreationForm, ChangePasswordForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from extend_user.models import ServerLogin
import whirlpool
import base64
import hashlib
from la2.settings import hash_type
from statistics.models import *


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
        'form': form, 'acc': acc,
    })


def changed(request):
    return render(request, 'changed.html')


def cabinet(request):
    query = ServerLogin.objects.using('default').filter(user_id=request.user.id)

    return render(request, "cabinet.html", {
        'query': query,
    })


def show_account(request, login):
    login = login
    # server = ['1', '2']
    check = ServerLogin.objects.using('default').filter(user_id=request.user.id, login=login)

    q = '''SELECT characters.obj_Id, characters.account_name,  characters.char_name,
character_subclasses.level, characters.accesslevel, characters.lastAccess, char_templates.ClassName
FROM `characters`
LEFT JOIN `character_subclasses` ON characters.obj_Id = character_subclasses.char_obj_id
LEFT JOIN `char_templates` ON character_subclasses.class_id = char_templates.ClassId
WHERE characters.account_name = '%s' ''' % login
    if check:
        query1 = Characters.objects.using('1').raw(q)
        query2 = Characters.objects.using('2').raw(q)
    else:
        return HttpResponseRedirect("/cabinet/")
    return render(request, "account.html", {
        'query1': query1, 'query2': query2, 'login': login
    })


def show_character(request, login, id):
    # login = login[:-1]
    # id = id
    check = ServerLogin.objects.using('default').filter(user_id=request.user.id, login=login)

    q = '''SELECT characters.obj_Id, characters.account_name, characters.char_name, character_subclasses.level, characters.sex, character_subclasses.class_id, characters.online, character_subclasses.exp, character_subclasses.sp, characters.karma, characters.pvpkills, characters.pkkills, characters.accesslevel, characters.onlinetime, characters.lastAccess, char_templates.ClassName, clan_data.clan_name
		FROM `characters`
		LEFT JOIN `character_subclasses` ON characters.obj_Id = character_subclasses.char_obj_id AND character_subclasses.isBase='1'
		LEFT JOIN `char_templates` ON character_subclasses.class_id = char_templates.ClassId
		LEFT JOIN `clan_data` ON characters.clanid = clan_data.clan_id
		WHERE characters.obj_Id='%s' ''' % id
    # if check:
    query1 = Characters.objects.using('1').raw(q)
    query2 = Characters.objects.using('2').raw(q)
    # else:
    #     return HttpResponseRedirect("/cabinet/")
    return render(request, "show_character.html", {
        'query1': query1, 'query2': query2, 'login': login, 'id': id,
    })