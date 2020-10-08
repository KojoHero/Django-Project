from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Post, Project
from django.views import generic


def Signup(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        form = CreateUserForm
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Hello, ' + user + ' your account has been created.')
                return redirect('Login')
        context = {
            'form': form
        }

        return render(request, 'signup.html', context)


def LoginUser(request):
    if request.user.is_authenticated:
        return redirect('LandingPage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('Login')
            else:
                messages.info(request, 'Username OR password is incorrect, Retry')

    context = {}
    return render(request, 'login.html', context)


def LogoutUser(request):
    logout(request)
    return redirect('Login')



def Home(request):
    context = {}
    return render(request, 'home.html', context)


@login_required(login_url='Login')
def News(request):
    context = {
    }
    return render(request, 'news.html', context)


@login_required(login_url='Login')
def ContactUs(request):
    context = {
    }
    return render(request, 'contactus.html', context)


@login_required(login_url='Login')
def Ecommerce(request):
    context = {}
    return render(request, 'ecommerce.html', context)


@login_required(login_url='Login')
def LandingPage(request):
    context = {
    }
    return render(request, 'landingpage.html', context)


def AboutUs(request):
    context = {
    }
    return render(request, 'aboutus.html', context)


@login_required(login_url='Login')
def Testers(request):
    context = {
    }
    return render(request, 'testers.html', context)


@login_required(login_url='Login')
def Developers(request):
    context = {
    }
    return render(request, 'developers.html', context)


@login_required(login_url='Login')
def Datascience(request):
    context = {
    }
    return render(request, 'datascience.html', context)

@login_required(login_url='Login')
def News(request):
    context = {
    }
    return render(request, 'news.html', context)


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'news.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)