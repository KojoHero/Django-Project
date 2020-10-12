from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import (
    Signup,
    LoginUser,
    Home,
    LogoutUser,
    LandingPage,
    Datascience,
    Developers,
    Testers,
    ContactUs,
    AboutUs,
    News,
    Ecommerce
)


urlpatterns = [
    path('signup/', Signup, name="Signup"),
    path('login/', LoginUser, name="Login"),
    path('logout/', LogoutUser, name="Logout"),
    path('', Home, name="Home"),
    path('landingpage/', LandingPage, name='LandingPage'),
    path('contact/', ContactUs, name='ContactUs'),
    path('about/', AboutUs, name='AboutUs'),
    path('market/', Ecommerce, name='Ecommerce'),
    path("projectindex/", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path('news/', views.PostList.as_view(), name='News'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]

