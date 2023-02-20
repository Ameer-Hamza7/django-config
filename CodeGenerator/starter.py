def write_views_file(STRUCTURED_STR):
    with open('main/views.py', 'a') as f:
        f.write(STRUCTURED_STR)

def write_path_file(STRUCTURED_STR):
    with open('main/urls.py', 'a') as f:
        f.write(STRUCTURED_STR)

def write_forms_file(STRUCTURED_STR):
    with open('main/forms.py', 'a') as f:
        f.write(STRUCTURED_STR)

app = "root_app"

def ConstructViewsPY(*args):
    write_views_file(f'''
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
            ''')

    write_path_file(f'''
from django.urls import path
from .views import *


urlpatterns = [
    
]
    ''')
    
    write_forms_file(f'''
from django.forms import ModelForm
from .models import *
    ''')
    for itr in args:
        write_views_file(
            f'''
##
### {itr['model_name'].upper()} MODULE
##

@login_required(login_url = 'login')
@permission_required(perm='{app}.add_{itr['model_name'].lower()}', login_url='unauthorized_user', raise_exception=False)
def create_{itr['model_name'].lower()}(request):
    
    FORM = {itr['model_name']}Form()
    DATA = {itr['model_name']}.objects.all()
    
    if request.method == 'POST':
        FORM_ = {itr['model_name']}Form(request.POST, request.FILES)


        if FORM_.is_valid():
            FORM_.save()

            return redirect('create_{itr['model_name'].lower()}') 
        
        else:

            return HttpResponse(FORM_.errors)

    context = [
        'form' : FORM,
        'status' : 'add',
        'data' : DATA
    ]

    return render(request, 'forms/app_forms/{itr['model_name']}_form.html', context=context)



@login_required(login_url = 'login')
@permission_required(perm='{app}.view_{itr['model_name'].lower()}', login_url='unauthorized_user', raise_exception=False)
def view_{itr['model_name'].lower()}(request, pk):
    OBJ = {itr['model_name']}.objects.get(id = pk)

    context = [
        'data' : OBJ
    ]

    return render(request, 'views/app_views/{itr['model_name']}_view.html', context=context)

@login_required(login_url = 'login')
@permission_required(perm='{app}.delete_{itr['model_name'].lower()}', login_url='unauthorized_user', raise_exception=False)
def delete_{itr['model_name'].lower()}(request, pk):
    
    OBJ = {itr['model_name']}.objects.get(id = pk)

    if request.method == "POST":
        OBJ.delete()

        return redirect('create_{itr['model_name'].lower()}')

    context = [
        'data' : OBJ
    ]

    return render(request, 'extra/deletepage.html', context=context)

@login_required(login_url = 'login')
@permission_required(perm='{app}.change_{itr['model_name'].lower()}', login_url='unauthorized_user', raise_exception=False)
def update_{itr['model_name'].lower()}(request, pk):

    OBJ = {itr['model_name']}.objects.get(id = pk)

    FORM = {itr['model_name']}Form(instance = OBJ)

    if request.method == 'POST':
        FORM_ = {itr['model_name']}Form(request.POST, instance = OBJ)

        if FORM_.is_valid():
            FORM_.save()

            return redirect('create_{itr['model_name'].lower()}') 
        
        else:

            return HttpResponse(FORM_.errors)

    context = [
        'form' : FORM,
        'status' : 'edit'
    ]

    return render(request, 'forms/app_forms/{itr['model_name']}_form.html', context=context)

##
### {itr['model_name'].upper()} MODULE
##
'''
        )

        write_path_file(
            f'''
    path('create_{itr['model_name'].lower()}', create_{itr['model_name'].lower()}, name="create_{itr['model_name'].lower()}"),
    path('view_{itr['model_name'].lower()}/<str:pk>', view_{itr['model_name'].lower()}, name="view_{itr['model_name'].lower()}"),
    path('delete_{itr['model_name'].lower()}/<str:pk>', delete_{itr['model_name'].lower()}, name="delete_{itr['model_name'].lower()}"),
    path('update_{itr['model_name'].lower()}/<str:pk>', update_{itr['model_name'].lower()}, name="update_{itr['model_name'].lower()}"),
            '''
        )

        write_forms_file(
            f'''
class {itr['model_name']}Form(ModelForm):
    class Meta:
        model = {itr['model_name']}
        fields = '__all__'

            '''
        )



ConstructViewsPY(
    {'model_name' : 'disciplinary_action'}
)
