from django.shortcuts import redirect,render,HttpResponse
def index(request):
    return render(request,'index.html')
def AddNewEmployee(request):
    if (request.method=='POST'):
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(Employee)
    else:
        form=EmployeeForm
        return render(request,'AddNewEmployee.html')
def Employee(request):
    Employees=Employee.object.order_by('-ID')
    return render(request,'employees.html')