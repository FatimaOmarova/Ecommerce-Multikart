from django.shortcuts import render
from core.services.about_page import list_staff
from core.forms import ContactForm, Subscribe
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation



def home(request):
    return render(request, 'core/index.html')



def about(request):
    staff = list_staff()
    context = {
        "staff": staff,
    }
    return render(request, 'core/about-page.html',context)


class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class FaqView(TemplateView):
    template_name = 'core/faq.html'


class ErrorView(TemplateView):
    template_name = 'core/404.html'

def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response