from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, FormView, ListView
from .form import proyekForm, organisasiFormSet
from .models import organisasi, proyek


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
			proyeks = formProyek.save()
			for form in formOrganisasi:
				dataOrganisasi= form.save(commit=False)
				dataOrganisasi.proyek = proyeks
				dataOrganisasi.save()
				# print(dataOrganisasi)
			return redirect('pm:list_organisasi')
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
