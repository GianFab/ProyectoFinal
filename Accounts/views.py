from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

from Accounts.forms import UserRegisterForm, UserUpdateForm, AvatarUpdateForm
from Accounts.models import Avatar


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)

        return redirect('principal')

    form = AuthenticationForm()
    contexto = {
        "form": form
    }
    return render(request, "Accounts/login.html", contexto)


def logout_view(request):
    logout(request)

    return redirect('login')


def register_request(request):
    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('principal')

    form = UserRegisterForm()
    contexto = {
        "form": form,
    }
    return render(request, "Accounts/registro.html", contexto)


@login_required
def editar_request(request):
    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('principal')

    form = UserRegisterForm()
    contexto = {
        "form": form,
    }
    return render(request, "Accounts/registro.html", contexto)


@login_required
def editar_avatar(request):

    user = request.user

    if request.method == "POST":
        form = AvatarUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            try:
                avatar = user.avatar
                avatar.imagen = data["imagen"]
                avatar.descripcion = data["descripcion"]
                avatar.pagina = data["pagina"]
                avatar.save()
            except:
                avatar = Avatar(
                    user=user,
                    imagen=data['imagen'],
                    descripcion=data['descripcion'],
                    pagina=data['pagina']
                )
                avatar.save()
            return redirect('editar_avatar')
    else:
        form = AvatarUpdateForm()

    contexto = {
        "form": form,
    }
    return render(request, "Accounts/avatar.html", contexto)

