from django.shortcuts import render
from .models import Students
# Create your views here.

def test(request):
    student = Students.objects.all()
    context = {

        'student' : student
    }

    return render(request,'test.html',context)
