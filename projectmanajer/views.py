from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, FormView, ListView
from .form import proyekForm, organisasiFormSet
from .models import organisasi, proyek


# from extra_views import FormSetView


# Create your views here.
# @login_required
# def dashboard(request):
#     return render(request,'pm/dashboard.html')
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
#
# @login_required
# def perangkat(request):
#     return render(request,'pm/perangkat.html')

class listOrganisasiView(ListView):
	model = proyek
	context_object_name = 'proyeks'
	template_name = 'pm/list_organisasi.html'


def proyek(request):
	if request.method == 'GET':
		formProyek = proyekForm(request.GET or None)
		formOrganisasi = organisasiFormSet(queryset=organisasi.objects.none())
	elif request.method == 'POST':
		formProyek = proyekForm(request.POST)
		formOrganisasi = organisasiFormSet(request.POST)
		if formProyek.is_valid() and formOrganisasi.is_valid():
			pr = formProyek.save()
			
			for frOrg in formOrganisasi:
				org = frOrg.save(commit=False)
				org.proyek = pr
				org.save()
			return redirect('pm:list_organisasi')
		else:
			print(formProyek.errors)
			print(formOrganisasi.errors)
	return render(request, 'pm/proyek.html', {
		'formProyek': formProyek,
		'formOrganisasi': formOrganisasi,
	})


# @method_decorator(login_required, name='dispatch')
# class proyekView(FormView):
#     template_name = 'pm/proyek.html'
#     form_class = proyekForm
#     success_url = '/thanks/'
#
#     def form_valid(self, form):


@method_decorator(login_required, name='dispatch')
class dashboardView(TemplateView):
	template_name = 'pm/dashboard.html'


@method_decorator(login_required, name='dispatch')
class perangkatView(TemplateView):
	template_name = 'pm/perangkat.html'
