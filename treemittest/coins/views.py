import logging
from django.views.generic import (
    TemplateView,
    DetailView,
    FormView
)
from .models import (
    Coin,
    BriefCase
)
from .forms import BuyCoinsForm
from django.shortcuts import redirect
from utils.coins import register_operation
from django.contrib import messages
from .serializers import BriefCaseSerializer

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


class PurchaseCoinPageView(FormView):
    form_class = BuyCoinsForm

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = BuyCoinsForm(request.POST)
            if form.is_valid():
                result = register_operation(request.user, form.data)
                if result:
                    messages.success(request, 'Successful Operation.')
                else:
                    messages.error(request, 'Fail Operation.')
            else:
                messages.error(request, 'Invalid Form.')
        return redirect('coins')


class BriefCasePageView(TemplateView):
    template_name = "coins/briefcase.html"

    def get_context_data(self, **kwargs):
        context = super(BriefCasePageView, self).get_context_data(**kwargs)
        objects_query = BriefCase.objects.filter(user=self.request.user).all()
        objects_serialize = BriefCaseSerializer(objects_query, many=True).data
        total = 0
        for obj in objects_serialize:
            value = obj.get('price') * obj.get('total_quantity')
            total = total + value
            obj.update(value=value)
        context['objects'] = objects_serialize
        context['total'] = total
        return context

