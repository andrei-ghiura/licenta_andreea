from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Profile, Meeting

# add a view for a new meeting that is only available to consultants and return the newmeeting.html page


@login_required(login_url="/login/")
def newmeeting(request):
    context = {'segment': 'newmeeting'}
    html_template = loader.get_template('home/newmeeting.html')
    return HttpResponse(html_template.render(context, request))


# add a normal view function that takes in a meeting id as an argument and return the notes of that meeting
@login_required(login_url="/login/")
def notes(request, id):
    context = {'segment': 'notes'}
    # add the meeting to the context
    context['meeting'] = Meeting.objects.get(id=id)
    html_template = loader.get_template('home/notes.html')
    return HttpResponse(html_template.render(context, request))


# add a calendar view function that takes in a username as an argument and return the calendar.html page
@login_required(login_url="/login/")
def calendar(request, username):
    context = {'segment': 'calendar'}
    # get the user object from the username
    user = Profile.objects.get(user__username=username)
    # add all the meetings that the user is assigned as a consultant to the context
    context['meetings'] = Meeting.objects.filter(
        consultant__username=username)
    print(context['meetings'])
    print(username)
    # add the user to the context
    context['user'] = user
    html_template = loader.get_template('home/calendar.html')
    return HttpResponse(html_template.render(context, request))


# add a profile view that takes the username as an argument and return the profile.html page
@login_required(login_url="/login/")
def profile(request, username):
    context = {'segment': 'profile'}
    # get the user object from the username
    user = Profile.objects.get(user__username=username)
    # add the user to the context
    context['user'] = user
    # add to the context the profile for the user
    context['meetNr'] = len(Meeting.objects.filter(
        consultant__username=username))
    context['meetings'] = Meeting.objects.filter(
        consultant__username=username)
    context['profile'] = Profile.objects.get(user__username=username)

    html_template = loader.get_template('home/profile.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        print(load_template)
        # switch case statement for load_template when it is listConsult.html, return null
        if load_template == 'listConsult.html':
            # add the users to the context where the position is consultant
            context['profiles'] = Profile.objects.filter(position='CO')
            return HttpResponse(html_template.render(context, request))
        if load_template == 'listClient.html':
            # add the users to the context where the position is consultant
            context['profiles'] = Profile.objects.filter(position='CL')
            return HttpResponse(html_template.render(context, request))

        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
