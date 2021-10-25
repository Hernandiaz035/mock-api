"""Clients Class Based Views URLs."""

# Django
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Models
from mock_api.clients.models import Client


class ClientListView(ListView):
    """Client List Class Based View."""

    model = Client
    paginate_by = 20

    template_name = "templates/clients/clients_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # import pdb; pdb.set_trace()
        return context


class ClientDetailView(DetailView):
    """Client Detail Class Based View."""

    model = Client

class ClientCreateView(CreateView):
    """Client Create Class Based View."""
    model = Client

    fields = '__all__'

    success_url = reverse_lazy('clients:clients-list')
