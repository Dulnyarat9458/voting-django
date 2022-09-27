from django.views.generic import *
from votingapp.form import RegisterForm
from votingapp.models import User, Choice
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

class Index(TemplateView):
    template_name = 'index.html'


class Register(CreateView):
    model: User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/register/'


class Login(LoginView):
    template_name = 'login.html'
    form_class: RegisterForm
    success_url = settings.LOGIN_REDIRECT_URL
    redirect_authenticated_user = True


class Home(ListView):
    model = Choice
    template_name = 'home.html'
    queryset = Choice.objects.all()
    context_object_name = 'choice'


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)


class ConfirmVote(View):
    def post(self, request):
        your_choice = Choice.objects.get(id=request.POST['choice-id'])
        your_choice.score = your_choice.score+1
        your_choice.save()

        user = self.request.user
        print(timezone.timedelta(hours=1))
        user.votable_time = timezone.now() + timezone.timedelta(hours=1)
        user.save()
        
        return HttpResponseRedirect(reverse('home'))
