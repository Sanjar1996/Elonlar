from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegistrationForm, LoginForm, ProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from config.mixins import LogoutRequiredMixin


class RegistrationView(LogoutRequiredMixin, View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = "Ro'yxatdan o'tish"

    def get(self, request):
        context = {
            'form': RegistrationForm()
        }
        return render(request, 'user/registration.html', context)

    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Ro'yxatdan muvoffaqiyatli o'tdingiz.")
            return redirect("articles:index")
        return render(request, 'user/registration.html', {
            'form': form
        })


class LoginView(LogoutRequiredMixin, View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = "Tizimga kirish"

    def get(self, request):
        return render(request, 'user/login.html', {
            'form': LoginForm()
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "{} xush kelibsiz".format(user.get_short_name()))
                return redirect('articles:index')
        form.add_error('password', "Login va/yoki parol xato!!!")

        return render(request, 'user/login.html', {
            'form': form
        })

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, 'Kelib turing!!')
        return redirect('articles:index')



class ProfileView(LogoutRequiredMixin, View):

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = "Profil"

    def get(self, request):
        return render(request, 'user/profile.html', {
            'form': ProfileForm(instance=request.user)
        })

    def post(self, request):
        pass