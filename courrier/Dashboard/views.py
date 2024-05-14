from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from Dashboard.forms import CourrierForm, RappelForm
from Dashboard.models import Courrier, Rappel
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.

class IndexView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'courriers'
    paginate_by = 10  # Optionnel : définir le nombre de courriers par page

    def get_queryset(self):
        # Récupérer les courriers destinés à l'utilisateur connecté
        return Courrier.objects.filter(destinataire=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajouter les rappels créés par l'utilisateur connecté au contexte
        context['rappels'] = Rappel.objects.filter(createur=self.request.user)
        return context

class AddCourrierView(LoginRequiredMixin, CreateView):
    model= Courrier
    form_class= CourrierForm
    template_name='courrier.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.expediteur= self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('index')


class CourrierDetailView(LoginRequiredMixin, DetailView):
    model = Courrier
    template_name = 'details_courrier.html'
    context_object_name = 'courrier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courriers_envoyes'] = Courrier.objects.filter(expediteur=self.request.user)
        context['courriers_recus'] = Courrier.objects.filter(destinataire=self.request.user)
        return context

class CreateRappelView(LoginRequiredMixin, CreateView):
    model = Rappel
    form_class = RappelForm
    template_name = 'create_rappel.html'

    def form_valid(self, form):
        courrier_id = self.kwargs['courrier_id']
        courrier = Courrier.objects.get(id=courrier_id)
        form.instance.createur = self.request.user
        form.instance.courrier = courrier
        return super().form_valid(form)

    def get_success_url(self):
        return '/index/'

class UpdateRappelView(LoginRequiredMixin, UpdateView):
    model = Rappel
    form_class = RappelForm
    template_name = 'update_rappel.html'

    def get_success_url(self):
        return '/index/'

def delete_rappel(request, rappel_id):
    rappel = Rappel.objects.get(id=rappel_id)
    rappel.delete()
    return redirect('index') 