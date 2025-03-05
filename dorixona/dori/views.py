from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView, CreateView, DetailView, UpdateView

from .forms import DoriForm, ContactForm
from .models import Dori


# Create your views here.

def home(request):
    return render(request, 'home.html')

class DoriUpdate(UpdateView):
    model = Dori
    form_class = DoriForm
    template_name = 'dori/dori_update.html'
    context_object_name = 'dori'

    def get_success_url(self):
        return reverse_lazy('dori-detail', kwargs={'pk': self.object.pk})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Dori

class DoriDelete(DeleteView):
    model = Dori
    form_class = DoriForm
    success_url = reverse_lazy('dori-list')
    template_name = 'dori/dori_delete.html'
    context_object_name = 'dori'

    def get_success_url(self):
        return reverse_lazy('dori-list', kwargs={'pk': self.object.pk})


def contact_form(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        phone_number = form.cleaned_data['phone_number']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        print(f'Name: {name}, Phone: {phone_number}, Email: {email}, Message: {message}')
        return redirect('home')
    return render(request, 'contact.html', {'form': form})


class DoriList(ListView):
    model = Dori
    template_name = 'dori/dori_list.html'
    context_object_name = 'dori'


class DoriCreate(View):
    def get(self, request):
        form = DoriForm()
        return render(request, 'dori/dori_create.html', {'form': form})

    def post(self, request):
        form = DoriForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dori_list')
        return render(request, 'dori/dori_create.html', {'form': form})


class DoriDetail(DetailView):
    model = Dori
    template_name = 'dori/dori_detail.html'
    context_object_name = 'dori'

