from django.contrib import messages
from .forms import ControlForm, ItemsForm, RegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView, DeleteView, CreateView
from .models import Controls, Items


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def controller(request):
    controller_list = Controls.objects.all()
    return render(request, 'main/controller.html', {'controller_list': controller_list})


def items(request):
    items_list = Items.objects.all()
    return render(request, 'main/items.html', {'items_list': items_list})


class ControllerDetailsView(DetailView):
    model = Controls
    template_name = 'main/controller_details.html'
    context_object_name = 'controller_detail'


class ItemsDetailsView(DetailView):
    model = Items
    template_name = 'main/items_details.html'
    context_object_name = 'items_detail'


class ControllerUpdateView(UpdateView):
    model = Controls
    template_name = 'main/add_controller.html'
    form_class = ControlForm


class ItemsUpdateView(UpdateView):
    model = Items
    template_name = 'main/add_items.html'
    form_class = ItemsForm


class ControllerDeleteView(DeleteView):
    model = Controls
    success_url = '/controllers/'
    template_name = 'main/controller_delete.html'


class ItemsDeleteView(DeleteView):
    model = Items
    success_url = '/items/'
    template_name = 'main/items_delete.html'


def register_request(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Успішна реєстрація!")
            return redirect("home")
        messages.error(request, "Введені дані неправильні. Спробуйте ще раз")
    form = RegistrationForm()
    return render(request=request, template_name="main/registration.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Ви увійшли як {username}')
                return redirect("home")
            else:
                messages.error(request, "Некоректний логін або пароль")
        else:
            messages.error(request, "Некоректний логін або пароль")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Успішний вихід із акаунту")
    return redirect('home')


def add_controller(request):
    error = ''
    if request.method == 'POST':
        form = ControlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('controllers')
        else:
            error = 'Ви ввели некоректні дані! Спробуйте ще раз'

    form = ControlForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_controller.html', data)


def add_items(request):
    error = ''
    if request.method == 'POST':
        form = ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items')
        else:
            error = 'Ви ввели некоректні дані! Спробуйте ще раз'

    form = ItemsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_items.html', data)
