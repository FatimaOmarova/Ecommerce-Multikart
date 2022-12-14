from core.forms import Subscribe
from django.shortcuts import render

from django.http import HttpRequest


def subscribe_form(request):
    if request.method == 'POST':
        form = Subscribe(request.POST)
        if form.is_valid():
            form.save()

    return {'subscribe_form': Subscribe}