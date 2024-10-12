from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp, Testimonial
from .forms import FeedbackForm, EmpForm
# Create your views here.

def emp_record(request):
    emps = Emp.objects.all()
    return render(request, 'emp/index.html',{
        'emps':emps
    })
    # return HttpResponse("Hello Globe")

def add_emp(request):
    #validate

    # Data fetch
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        emp_id = request.POST.get("emp_id")
        department = request.POST.get("department")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        working = request.POST.get("working")

    # Create model object and set the data 
        e=Emp(name=name, age=age, emp_id=emp_id, department=department, email=email, phone=phone, address=address )
        if working is None:
           e.working=False
        else:
           e.working=True
    
    # Save the object            
        e.save()
    
    # Prepare messsage
        return redirect ("/emp/")
    form=EmpForm()

    return render(request, 'emp/add_emp.html', {'form':form})

def delete_emp(request, emp_id):
    try:
        var = Emp.objects.get(id=emp_id)  # Corrected to 'id' assuming 'id' is the primary key
        var.delete()
        return redirect('/emp/')
    except Emp.DoesNotExist:
        return render(request, 'emp/not_found.html')  # Handle case where employee is not found


def update_emp(request,emp_id):
    
        emp = Emp.objects.get(pk=emp_id)
        return render(request, 'emp/update_emp.html',{
            'emp':emp
        })

def do_update_emp(request, emp_id):
    if request.method == 'POST':
        name = request.POST.get("name")
        age = request.POST.get("age")
        emp_id_temp = request.POST.get("emp_id")
        department = request.POST.get("department")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        working = request.POST.get("working")

        e = Emp.objects.get(id=emp_id)
        e.name=name
        e.age=age
        e.emp_id=emp_id_temp
        e.department=department
        e.email=email
        e.phone=phone
        e.address=address 
        if working is None:
            e.working = False
        else:
            e.working = True

        e.save()
    return redirect('/emp/')

def testimonial(request):
    ret = Testimonial.objects.all()
    return render (request, 'emp/testimonial.html',{
         "ret":ret
         })

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['phone'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['feedback'])
            print("save successful")
            # return redirect('/emp/')
        else:
            return render(request, 'emp/feedback.html', {'form':form})
    else:
        form = FeedbackForm()
        return render(request, 'emp/feedback.html', {'form':form})