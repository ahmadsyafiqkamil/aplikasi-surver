from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    if request.session.has_key('login'):
        return render(request, 'pm/dashboard.html')
    else:
        return redirect('login')
    
@login_required
def proyek(request):
    return render(request,'pm/proyek.html')

@login_required
def perangkat(request):
    return render(request,'pm/perangkat.html')
