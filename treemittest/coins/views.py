from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class ListCoinsPageView(TemplateView):
    template_name = "coins/list.html"

    def get_context_data(self, **kwargs):
        context = super(ListCoinsPageView, self).get_context_data(**kwargs)
        return context