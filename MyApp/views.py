from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Post, Category, TodoList
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


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
def Customers(request):
    context = {}
    return render(request, 'customers.html', context)


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


@login_required(login_url='Login')
def Index(request):
    todos = TodoList.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            category = request.POST["category_select"]
            content = title + " -- " + date + " " + category
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()
            return redirect('Index')
        if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))
                todo.delete()
    return render(request, "index.html", {"todos": todos, "categories":categories})


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'news.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'





