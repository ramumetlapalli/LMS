from django.shortcuts import redirect,render,HttpResponse
def index(request):
    return render(request,'index.html')
def AddNewEmployee(request):
    if (request.method=='POST'):
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Employees')
    else:
        form=EmployeeForm
        return render(request,'AddNewEmployee.html')
