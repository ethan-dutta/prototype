from django.shortcuts import render
from .models import teacher, college
from .forms import teacherform

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
    context['cg'] = cg

   

    return render(request, "MyApp1/index.html", context)

#p