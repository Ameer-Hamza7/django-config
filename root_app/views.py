from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'login')
def index(request):
    return render(request, 'dashboard/index.html')




from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .forms import GroupCreation

def groups_permissions(request):
    if request.user.is_superuser:
        group_creation_form = GroupCreation()
        get_perms_ = []
        get_cts_ = ContentType.objects.all()

        if request.method == 'POST':
            posted_group_form = GroupCreation(request.POST)
            if posted_group_form.is_valid():
                group = posted_group_form.save()
                perms_ = request.POST.getlist('permission')
                for each_perm in perms_:
                    group.permissions.add(Permission.objects.get(id = int(each_perm)))
                group.save()
                messages.success(request, 'Group Created')
            else:
                messages.warning(request, posted_group_form.errors)

        for each_ct in get_cts_:
            get_perms_.append({'contentType' : each_ct, 'perms' : ''})
            perms = Permission.objects.filter(content_type = each_ct)
            get_perms_[-1]['perms'] = perms 
    else:
        perms = [each_perm for each_perm in [each_grp.permissions.all() for each_grp in request.user.groups.all()]]
        get_cts_ = []
        get_perms_ = []

        for each_qs in perms:
            for each_perm in each_qs:
                # get_perms_.append({'contentType' : each_ct, 'perms' : ''})
                get_cts_.append(each_perm.content_type.id)
                # print(each_perm.content_type.id)

        for each_ct in set(get_cts_):
            get_perms_.append({'contentType' : ContentType.objects.get(id = each_ct), 'perms' : ''})
            perms = Permission.objects.filter(content_type = each_ct)
            get_perms_[-1]['perms'] = perms 

        group_creation_form = GroupCreation()

        if request.method == 'POST':
            posted_group_form = GroupCreation(request.POST)
            if posted_group_form.is_valid():
                group = posted_group_form.save()
                perms_ = request.POST.getlist('permission')
                for each_perm in perms_:
                    group.permissions.add(Permission.objects.get(id = int(each_perm)))

                group.save()

                # clinic = ClinicUser.objects.get(user_instance = request.user).clinic_instance
                # print(group, clinic)
                # ClinicGroups.objects.create(
                #     clinic = clinic,
                #     group = group
                # )
                
                messages.success(request, 'Group Created')
            else:
                messages.warning(request, posted_group_form.errors)


    context = {
        'perms' : get_perms_,
        'group_creation_form' : group_creation_form,
    }

    return render(request, 'Settings/groups-permissions.html', context=context)
