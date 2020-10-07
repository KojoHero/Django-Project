from django.urls import path
from . import views
from .views import Signup, LoginUser, Home, LogoutUser, LandingPage, Datascience, Developers, Testers, ContactUs, AboutUs, News


urlpatterns = [
    path('signup/', Signup, name="Signup"),
    path('login/', LoginUser, name="Login"),
    path('logout/', LogoutUser, name="Logout"),
    path('', Home, name="Home"),
    path('landingpage/', LandingPage, name='LandingPage'),
    path('contact/', ContactUs, name='ContactUs'),
    path('about/', AboutUs, name='AboutUs'),
    path('testers/', Testers, name='Testers'),
    path('developers/', Developers, name='Developers'),
    path('datascience/', Datascience, name='Datascience'),
    path('news/', views.PostList.as_view(), name='News'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail')

]
