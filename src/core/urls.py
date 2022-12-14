from django.urls import path
from .views import ContactView, home, about, FaqView,ErrorView

app_name = "core"

urlpatterns = [
    path('', home, name='home'),
    path('about-page', about, name='about'),
    path('faq',FaqView.as_view(), name='faq'),
    path('contact/', ContactView.as_view(), name="contact"),
    path('404', ErrorView.as_view(), name='404')
]
