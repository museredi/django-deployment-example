from django.shortcuts import render
from django.http import HttpResponse
#from ninth_app.models import Usersss
from ninth_app.forms import NewUserForm

# Create your views here.

def index(request):
    return HttpResponse("<h1>this is index, now go to signup/ to signup</h1>")

def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'ninth_app/users.html', {'form':form})
    
