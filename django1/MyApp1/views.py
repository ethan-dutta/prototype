from calendar import c
from encodings.punycode import T
from django.shortcuts import render
from .models import teacher, college
from .forms import teacherform
from .forms import loginform
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import ValidationError
from django.shortcuts import redirect
from pypdf import PdfWriter, PdfReader #Joining PDFs
from reportlab.pdfgen import canvas #Generating PDfs
from reportlab.platypus import Paragraph,Image,Table #Generating PDfs
from django.http import FileResponse #Downloading files
from django.contrib.staticfiles.storage import staticfiles_storage #Working with static files
from io import BytesIO #Using Byte streams
import io
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch


def venue_pdf(request):
    buf=io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottumup=0)
    lines = [('Name: ', 'Teaching Area:')]

    teachers = teacher.objects.select_related('college').all()

    for teach in teachers:
        lines.append((teach.name, teach.teaching_area)) 

    table = Table(lines)
    table.wrapOn(c, inch, inch)
    table.drawOn(c, inch, inch)
    c.showPage()
    c.save()
    buf.seek(0)
    return buf



def login(request):
    context = {}
    form = loginform()
    context['form'] = form
    #if request.method == "POST":
    #error = "ddddd"
    if 'submit' in request.POST:
            form = loginform(request, data=request.POST)
            if form.has_changed():

                if form.is_valid():
                    error = print("Login successful, redirecting you to main page...")
                    user = form.get_user()
                    auth_login(request, user)
                    return redirect('/index')
#                else:
#                    try:
#                        raise ValidationError()
#                    except ValidationError as e:
#                                            print(e)
                if not form.data['username']:
                    errorr = "Please enter username"
                    context['errorr'] = errorr
                elif not form.data['password']:
                        errorr = "Please enter password"
                        context['errorr'] = errorr
                elif len(form.data['password']) < 8 or len(form.data['password']) > 20:
                    errorr = "Password must be between 8 and 20 characters"
                    context['errorr'] = errorr
                elif len(form.data['username']) < 8 or len(form.data['username']) > 20:
                    errorr = "Username must be between 8 and 20 characters"
                    context['errorr'] = errorr
                else:
                    errorr = "Invalid username or password"
                    context['errorr'] = errorr
            else:
                errorr = "Please enter username and password"
                context['errorr'] = errorr
    #context['error'] = error


    return render(request, 'MyApp1/login.html', context)

def index(request):
    context = {}
    form = teacherform()
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
    context['form']=form

   

    return render(request, "MyApp1/index.html", context)

#p