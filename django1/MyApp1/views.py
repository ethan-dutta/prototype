from calendar import c
from django.shortcuts import render
from .models import teacher, college
from .forms import teacherform, loginform
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import ValidationError
from django.shortcuts import redirect
from django.contrib.staticfiles.storage import staticfiles_storage #Working with static files
from django.core.files.storage import FileSystemStorage
from django.forms.formsets import BaseFormSet
from django.forms import modelformset_factory 
import time

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'MyApp1/upload.html', context)
    
def login(request):
    context = {} 
    counter = 0
    form = loginform(request, data=request.POST)
    if request.method == "POST":
        if 'submit' in request.POST:
            
            if form.is_valid():
                print("Login successful, redirecting you to main page...")
                user = form.get_user()
                auth_login(request, user)
                return redirect('/index')
            else:

                counter += 1
                # loginform()
                print(counter)
                if counter > 3:
                    counter = 0
    context['counter'] = counter

    context['form'] = form

    return render(request, 'MyApp1/login.html', context)

def index(request):
    context = {}
    form = teacherform()
    formsetter = modelformset_factory(teacher, fields=('name','area','college'), extra = 4)
    formset = formsetter(queryset=teacher.objects.none(), initial = 
                         [{"name":request.POST.get('name') or None, 
                            "area":request.POST.get('area') or None, 
                            "college":request.POST.get('college') or None} for i in range(5)])
    context['formset']=formset
    teach = teacher.objects.select_related('college').all()
    cg = college.objects.all()
    context['teach']=teach
    if request.method == "POST":
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = teacherform(request.POST)
            else:
                teach = teacher.objects.get(id=pk)
                form = teacherform(request.POST, instance=teach)
            form.save()
            form = teacherform()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            teach = teacher.objects.get(id=pk)
            teach.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            teach = teacher.objects.get(id=pk)
            form = teacherform(instance=teach)
        elif 'submit_all' in request.POST:
            formset = formsetter(request.POST)
            if formset.is_valid():
                for form in formset:
                    form.save()
            else:
                formset = loginform()
                print("nosorr")
    context['form']=form

    return render(request, "MyApp1/index.html", context)
