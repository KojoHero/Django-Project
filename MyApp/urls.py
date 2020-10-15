from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import (
    Signup,
    LoginUser,
    Home,
    LogoutUser,
    LandingPage,
    ContactUs,
    AboutUs,
    News,
    Customers,
    Index
)


urlpatterns = [
    path('signup/', Signup, name="Signup"),
    path('login/', LoginUser, name="Login"),
    path('logout/', LogoutUser, name="Logout"),
    path('', Home, name="Home"),
    path('landingpage/', LandingPage, name='LandingPage'),
    path('todo/', Index, name='Index'),
    path('contact/', ContactUs, name='ContactUs'),
    path('about/', AboutUs, name='AboutUs'),
    path('customers/', Customers, name='Customers'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_done.html"),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_form.html"),
         name='password_reset_complete'),
    path('news/', views.PostList.as_view(), name='News'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]

