import logging
from django.views.generic import (
    TemplateView,
    DetailView
)
from .models import Coin

# Get an instance of a logger
logger = logging.getLogger(__name__)


class ListCoinsPageView(TemplateView):
    template_name = "coins/list.html"

    def get_context_data(self, **kwargs):
        context = super(ListCoinsPageView, self).get_context_data(**kwargs)
        row_list = Coin.objects.all()
        context['row_list'] = row_list
        return context


class DetailCoinsPageView(DetailView):
    template_name = "coins/detail.html"
    model = Coin
