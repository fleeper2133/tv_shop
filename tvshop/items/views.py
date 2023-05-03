from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from math import ceil


class ItemList(ListView):
    model = Tv
    template_name = 'items/items.html'
    context_object_name = 'items'

    def get_queryset(self):
        search = self.request.GET.get('search')
        if not search:
            search = ""

        if self.kwargs.get('model_slug'):
            items = Tv.objects.filter(is_published=True,
                                      model__slug=self.kwargs['model_slug'],
                                      title__iregex=search)
        else:
            items = Tv.objects.filter(is_published=True,
                                      title__iregex=search)
        return items

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        models = Model.objects.all()
        cart = self.request.session.get('cart')

        if self.kwargs.get('model_slug'):
            row_count = ceil(Tv.objects.filter(is_published=True, model__slug=self.kwargs['model_slug']).count() / 4)
            if row_count > 0:
                context['title'] = context['items'][0].model
            else:
                context['title'] = "Категория"
        else:
            row_count = ceil(Tv.objects.filter(is_published=True).count() / 4)
            context['title'] = "Главная страница"

        if cart:
            items_cart = Tv.objects.filter(pk__in=cart)
            context['items_cart'] = items_cart

        context['models'] = models
        context['slug_selected'] = self.kwargs.get('model_slug')
        context['range'] = range(row_count)
        return context


class ItemDetail(DetailView):
    model = Tv
    template_name = 'items/detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        same_items = Tv.objects.filter(~Q(pk=context['item'].pk), is_published=True, model__pk=context['item'].model.pk)
        context['title'] = context['item']
        context['same_items'] = same_items
        return context


