from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index (request):
    isActive = True
    if request.method == 'POST':
        check = request.POST.get('check')
        print(check)
        if check is None:
            isActive=False
        else:
            isActive=True
            
            


    name = 'Ram'
    date = datetime.now()
    
    age = 19
    list_of_programs=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime number from 1 to 100',
        'WAP to print pascals triangle',
        'WAP to print fibonaci series',

    ]

    student = {
        'student_college' : 'ABC',
        'student_name' : 'Mohit',
        'student_age'  : '20',
    }
    
    data={
        'list_of_program': list_of_programs,
        'date': date,
        'student': student,
        'isActive':isActive,

        
        'name':name,
    }
    return render(request, 'index.html', data)

def about (request):
    return render(request, 'about.html')

def services (request):
    return render(request, 'services.html')

def login (request):
    return render(request, 'login.html')


