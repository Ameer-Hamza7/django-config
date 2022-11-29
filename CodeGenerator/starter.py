def write_views_file(STRUCTURED_STR):
    with open('views.py', 'a') as f:
        f.write(STRUCTURED_STR)

def write_path_file(STRUCTURED_STR):
    with open('urls.py', 'a') as f:
        f.write(STRUCTURED_STR)

def write_forms_file(STRUCTURED_STR):
    with open('forms.py', 'a') as f:
        f.write(STRUCTURED_STR)

def ConstructViewsPY(*args):
    write_views_file(f'''
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
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
######################################################
############### {itr['model_name'].upper()} MODULE ##################
######################################################

@login_required(login_url = 'login')
def create_{itr['model_name'].lower()}(request):
    FORM = {itr['model_name']}Form()

    if request.method == 'POST':
        FORM_ = {itr['model_name']}Form(request.POST)

        if FORM_.is_valid():
            FORM_.save()

            return redirect('view_{itr['model_name'].lower()}') 
        
        else:

            return HttpResponse(FORM_.errors)

    context = [
        'form' : FORM,
        'status' : 'add'
    ]

    return render(request, 'forms/app_forms/{itr['model_name']}_form.html', context=context)



@login_required(login_url = 'login')
def view_{itr['model_name'].lower()}(request):
    OBJ = reversed({itr['model_name']}.objects.all())

    context = [
        'data' : OBJ,
        'header' : [

        ]
    ]

    return render(request, 'views/{itr['model_name']}_view.html', context=context)

@login_required(login_url = 'login')
def delete_{itr['model_name'].lower()}(request, pk):
    
    OBJ = {itr['model_name']}.objects.get(id = pk)

    if request.method == "POST":
        OBJ.delete()

        return redirect('view_{itr['model_name'].lower()}')

    context = [
        'data' : OBJ
    ]

    return render(request, 'extra/deletepage.html', context=context)

@login_required(login_url = 'login')
def update_{itr['model_name'].lower()}(request, pk):

    OBJ = {itr['model_name']}.objects.get(id = pk)

    FORM = {itr['model_name']}Form(instance = OBJ)

    if request.method == 'POST':
        FORM_ = {itr['model_name']}Form(request.POST, instance = OBJ)

        if FORM_.is_valid():
            FORM_.save()

            return redirect('view_{itr['model_name'].lower()}') 
        
        else:

            return HttpResponse(FORM_.errors)

    context = [
        'form' : FORM,
        'status' : 'edit'
    ]

    return render(request, 'forms/app_forms/{itr['model_name']}_form.html', context=context)

######################################################
############### {itr['model_name'].upper()} MODULE ##################
######################################################
'''
        )

        write_path_file(
            f'''
    path('create_{itr['model_name'].lower()}', create_{itr['model_name'].lower()}, name="create_{itr['model_name'].lower()}"),
    path('view_{itr['model_name'].lower()}', view_{itr['model_name'].lower()}, name="view_{itr['model_name'].lower()}"),
    path('delete_{itr['model_name'].lower()}', delete_{itr['model_name'].lower()}, name="delete_{itr['model_name'].lower()}"),
    path('update_{itr['model_name'].lower()}', update_{itr['model_name'].lower()}, name="update_{itr['model_name'].lower()}"),
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
    {'model_name' : 'RequestType'},
    {'model_name' : 'ExcuseType'},
    {'model_name' : 'ReasonType'},
    {'model_name' : 'ExcuseRequest'},
    {'model_name' : 'AssetType'},
    {'model_name' : 'AssetRequest'},
    {'model_name' : 'ExitReentryVisaType'},
    {'model_name' : 'VisaPeriod'},
    {'model_name' : 'ExitReentryVisaRequest'},
    {'model_name' : 'PuchCorrectionRequest'},
    {'model_name' : 'ResignationReason'},
    {'model_name' : 'ResignationRequest'},
    {'model_name' : 'DelegationRequest'}
)
