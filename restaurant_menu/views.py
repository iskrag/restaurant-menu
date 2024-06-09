from django.shortcuts import render
from django.views import generic
from .models import Item


class MenuList(generic.ListView):
    """Connect db model to the view, and the view to the html frontend."""
    # Variable names must not change
    queryset = Item.objects.order_by('-date_created')
    template_name = 'index.html'


class MenuItemDetail(generic.DetailView):
    # Variable names must not change
    model = Item
    template_name = 'menu_item_details.html'
