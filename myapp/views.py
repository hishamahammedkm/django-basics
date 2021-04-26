from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
from .forms import DForm
def error_404_view(request,exception):
    return render(request,'404.html')
def home(request):
     return render(request,'image.html')

def add(request,a,b):
    return HttpResponse(f'<h1>{a+b}</h1>')

def json(request,name,age):
    details = {'name':name,'age':age}
    return JsonResponse(details)
def second(request):
    fruits = ['a','s','e']
    number = 100
    data = {'name':'hisham','data1':fruits,'number':number}
    return render(request,'second.html',context=data)
def form (request):
    return render(request,'form.html')

def form_submit (request):
    print(request)
    print(request.GET)
    form_data = {
         'method':request.method,
         'password':request.POST['password'],
         'email':request.POST['email']
    }
    return JsonResponse(form_data)
def form2(request):
    if request.method == 'POST':
        form = DForm(request.POST)
        if form.is_valid():
            password = request.POST['password']
            email = request.POST['email']
            print(password,email)
            if email != email.upper():
                data = {'form':DForm()}
                data['error'] = True
                data['errormsg'] = 'enter in capital'
                return render(request,'form2.html',context=data)
            else:
                data = {'form':DForm()}
                data['sucsess'] = True
                data['sucsessmsg'] = 'SUCESS'
                return render(request,'form2.html',context=data)

            


        
    form = DForm()
    data = {'form':form}
    return render(request,'form2.html',context=data)
