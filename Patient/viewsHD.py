from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect

from Patient.forms import PatientForm
from Patient.models import Patient

# class AddNewView(LoginRequiredMixin,CreateView):
class PatientAddNewView(CreateView):
    # login_url = '/admin/'
    model = Patient
    # fields = '__all__'
    form_class = PatientForm
    template_name = 'Patient/AddNew.html'    
    success_url = reverse_lazy('Patient:List')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.DataUser = self.request.user
        self.object.save()
        messages.info(self.request,"Save Success")
        return HttpResponseRedirect(self.get_success_url())

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         obj = form.save(commit=False)
    #         obj.DataUser = request.user
    #         obj.save()
    #         messages.success(request, f'Your order has been placed.')
    #     return redirect('Patient:List')

class PatientListView(ListView):
    model = Patient
    template_name = 'Patient/List.html'
    paginate_by = 5
    ordering = ['Date',]

    def get_template_names(self):
        # print(self.request.user)
        # print(self.request.user.has_perm('UserData.User_AF_CMO'))
        if self.request.user.has_perm('UserData.User_AF_CMO'):
            return 'Patient/List.html'
        else:
            return 'Patient/ListAFCMO.html'

# class PatientUpdateView(PermissionRequiredMixin,UpdateView):
class PatientUpdateView(UpdateView):
    # permission_required = 'Patient.change_patient'

    model = Patient
    # fields = '__all__'
    form_class = PatientForm
    template_name = 'Patient/Update.html'    
    success_url = reverse_lazy('Patient:List')


def UpdatePatientData(request, pk):
    context ={}

    obj = get_object_or_404(Patient, id = pk)
 
    form = PatientForm(request.POST or None, request.FILES or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return redirect(reverse_lazy('Patient:List'))
 
    context["form"] = form
 
    return render(request, "Patient/Update.html", context)