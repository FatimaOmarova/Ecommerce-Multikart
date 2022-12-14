from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from Multikart.oauth import oauth
from users.forms import UserRegisterForm
from users.services.user import create_user_if_not_exist
from .models import *
from django.contrib import messages
import uuid
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

# # Create your views here.
# def login(request):
#     return render(request, 'users/login.html')

# def register(request):
#     return render(request, 'users/register.html')

#def forget(request):
#    return render(request, 'users/forget_pwd.html')

def profile(request):
    return render(request, 'users/profile.html')

def wishlist(request):
    return render(request, 'users/wishlist.html')



UserModel = get_user_model()


def register_user(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    form = UserRegisterForm()
    return render(request, "users/register.html", context={"form": form})


def login_user(request: HttpRequest) -> HttpResponse:
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("users:auth-callback"))
    )


def auth_callback(request: HttpRequest) -> HttpResponse:
    user: dict = oauth.auth0.authorize_access_token(request)

    create_user_if_not_exist(
        first_name=user["userinfo"]["given_name"],
        last_name=user["userinfo"]["family_name"],
        email=user["userinfo"]["email"]
    )

    request.session["user"] = user
    return redirect(request.build_absolute_uri(reverse("core:home")))


def logout(request: HttpRequest) -> HttpResponse:
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("core:home")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

def password_reset_request(request):
    
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = UserModel.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "users/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'elyanoraaa195@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="users/password_reset.html", context={"password_reset_form":password_reset_form})