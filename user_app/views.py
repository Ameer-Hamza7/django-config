from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *

# Create your views here.


def unauthorized_user(request):
    return render(request, 'users/unauthorize_user.html')


def user_registration(request):
    # from root_app.views import select_language
    
    registration_form = CreateUserForm()
    users = User.objects.all()

    if request.method == 'POST':
        submitted_form = CreateUserForm(request.POST)
        print('GROUP: ', request.POST.get('groups'))
        
        if submitted_form.is_valid():
            user = submitted_form.save()
            if request.POST.get('groups'):
                user.groups.add(Group.objects.get(id = int(request.POST.get('groups'))))
                
            return redirect('registration')

        else:

            return HttpResponse(submitted_form.errors)

    context = {
        'data' : users,
        'form': registration_form,
        # 'lang_tags': select_language(request),
        'status' : 'add',
        'header' : ['Id', 'Username', 'Email']
    }

    return render(request, 'forms/app_forms/user_form.html', context=context)


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid Credentials")

    return render(request, 'users/login.html')


def user_logout(request):

    logout(request)

    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    # from root_app.views import select_language
    context = {
        # 'lang_tags': select_language(request),
    }
    return render(request, 'dashboard/index.html',context=context)


@login_required(login_url='login')
def create_company_group(request):

    # from root_app.views import select_language

    from django.contrib.auth.models import Permission
    from django.contrib.contenttypes.models import ContentType
    from django.contrib import messages

    if request.user.is_superuser:
        FORM = CreateGroupForm()
        get_perms_ = []
        get_cts_ = ContentType.objects.all()

        if request.method == 'POST':
            posted_group_form = CreateGroupForm(request.POST)
            if posted_group_form.is_valid():
                group = posted_group_form.save()

                perms_ = request.POST.getlist('permission')
                for each_perm in perms_:
                    group.permissions.add(
                        Permission.objects.get(id=int(each_perm)))
                group.save()
                messages.success(request, 'Group Created')
            else:
                messages.warning(request, posted_group_form.errors)

        for each_ct in get_cts_:
            get_perms_.append({'contentType': each_ct, 'perms': ''})
            perms = Permission.objects.filter(content_type=each_ct)
            get_perms_[-1]['perms'] = perms
    else:
        perms = [each_perm for each_perm in [each_grp.permissions.all()
                                             for each_grp in request.user.groups.all()]]
        get_cts_ = []
        get_perms_ = []

        for each_qs in perms:
            for each_perm in each_qs:
                get_cts_.append(each_perm.content_type.id)

        for each_ct in set(get_cts_):
            get_perms_.append(
                {'contentType': ContentType.objects.get(id=each_ct), 'perms': ''})
            perms = Permission.objects.filter(content_type=each_ct)
            get_perms_[-1]['perms'] = perms

        FORM = CreateGroupForm()

        if request.method == 'POST':
            posted_group_form = CreateGroupForm(request.POST)
            if posted_group_form.is_valid():
                group = posted_group_form.save()
                perms_ = request.POST.getlist('permission')
                for each_perm in perms_:
                    group.permissions.add(
                        Permission.objects.get(id=int(each_perm)))

                group.save()

                messages.success(request, 'Group Created')
            else:
                print(posted_group_form.errors)
                messages.warning(request, posted_group_form.errors)

    DATA = Group.objects.all()

    # if request.method == 'POST':
    #     FORM_ = CreateGroupForm(request.POST, request.FILES)

    #     if FORM_.is_valid():
    #         FORM_.save()

    #         return redirect('create_company_designation')

    #     else:
    #         print(FORM_.errors)
    #         return HttpResponse(FORM_.errors)

    context = {
        # 'lang_tags': select_language(request),
        'form': FORM,
        'status': 'add',
        'data': DATA,
        'perms_': get_perms_,
        'header': ['Id', 'Group Name']
    }

    return render(request, 'users/groups_perms.html', context=context)