from django.urls import path, include
from users.views import login_user, register_user, auth_callback, logout, profile,wishlist, password_reset_request
from django.contrib.auth import views as auth_views
app_name = 'users'
urlpatterns = [
    path('login/',login_user, name='login'),
    path('register',register_user, name='register'),
    path("auth-callback", auth_callback, name="auth-callback"),
    path("logout", logout, name="logout"),
    path('profile', profile),
    path('wishlist', wishlist),
    path("password_reset/", password_reset_request, name="password_reset"),
]