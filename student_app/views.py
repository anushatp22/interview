from django.shortcuts import render, redirect
from student_app.models import *
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
def studentform(request):
    return render(request, 'studentform.html')
def studentformaction(request):
    name=request.POST['studentname']
    dob=request.POST['dob']
    physicsmark=request.POST['physics']
    chemistrymark=request.POST['chemistry']
    mathsmark=request.POST['maths']
    csmark=request.POST['cs']
    k=[]
    k.append(int(physicsmark))
    k.append(int(csmark))
    k.append(int(chemistrymark))
    k.append(int(mathsmark))
    totalmark=400
    div=sum(k)/totalmark
    percentage=div*100
    add=student_table(student_name=name,date_of_birth=dob,mark_of_physics=physicsmark,mark_of_chemistry=chemistrymark,mark_of_maths=mathsmark,mark_of_computerscience=csmark,percentage=percentage)
    add.save()
    messages.add_message(request,messages.INFO, 'added successfully')
    return redirect('studentform')
def studentdetails(request):
    studentdata=student_table.objects.all()
    return render(request, 'studentdetails.html', {"studentdetails":studentdata})

# Create your views here.
