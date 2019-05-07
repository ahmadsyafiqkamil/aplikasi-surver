from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    return render(request,'pm/dashboard.html')
    # if request.session.has_key('login'):
    #     if request.method == 'POST':
    #         nama_proyek = request.POST['nama_proyek']
    #         nama_pj_proyek= request.POST['nama_pj_proyek']
    #
    #         print(nama_proyek)
    #         print(nama_pj_proyek)
    #
    #         return redirect('pm:dashboard')
    #
    #
    #     else:
    #         return redirect('pm:dashboard')
    # else:
    #     return redirect('accounts:login')
    #
@login_required
def proyek(request):
    return render(request,'pm/proyek.html')

@login_required
def perangkat(request):
    return render(request,'pm/perangkat.html')
