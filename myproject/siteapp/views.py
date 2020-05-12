from django.shortcuts import render
from siteapp.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    filter_dict = {
        'name':'Hello this my website',
        'des':'this site is all about the ideas'
    }
    return render(request, 'siteapp/index.html', context=filter_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def relative(request):
    return render(request, 'siteapp/relative.html')

def registration(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pics' in request.FILES:
                profile.profile_pics = request.FILES['profile_pics']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'siteapp/registration.html', 
                                {'registered':registered,
                                'user_form':user_form,
                                'profile_form':profile_form})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account Not Active')
        
        else:
            print('Someone tried to login and failed')
            print('Username {} and password {}'.format(username, password))
            return HttpResponse('Login details supplied failed')
    
    else:
        return render(request, 'siteapp/login.html', {})


