"""Clients Class Based Views URLs."""

# Django
from django.db import models
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Models
from mock_api.clients.models import Client


class ClientListView(ListView):
    """Client List Class Based View."""

    model = Client
    paginate_by = 20

    template_name = "templates/clients/clients_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ClientDetailView(DetailView):
    """Client Detail Class Based View."""

    model = Client
